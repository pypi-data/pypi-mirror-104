.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_gallery_tutorials_0100_forecast_tutorial.py>`     to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _sphx_glr_gallery_tutorials_0100_forecast_tutorial.py:


Tune your first forecast model
==============================

This is a basic tutorial for creating and tuning a forecast model.
It is intended to provide a basic sense of a forecast process without
assuming background knowledge in forecasting.

You can use the ``PROPHET`` or ``SILVERKITE`` model.
In this tutorial, we focus on ``SILVERKITE``.
However, the basic ideas of tuning are similar to both models.
You may see detailed information about ``PROPHET`` at
`Prophet <../../pages/model_components/0100_introduction.html#prophet>`_.


``SILVERKITE`` decomposes time series into various components, and it
creates time-based features, autoregressive features,
together with user-provided features such as macro-economic features
and their interactions, then performs a machine learning regression
model to learn the relationship between the time series and these
features. The forecast is based on the learned relationship and
the future values of these features. Therefore, including the correct
features is the key to success.

Common features include:

    Datetime derivatives:
        Including features derived from datetime such as ``day of year``,
        ``hour of day``, ``weekday``, ``is_weekend`` and etc.
        These features are useful in capturing special patterns.
        For example, the patterns of weekdays and weekends are different
        for most business related time series, and this can be modeled with ``is_weekend``.
    Growth:
        First defines the basic feature ``ct1`` that counts how
        long has passed in terms of years (could be fraction)
        since the first day of training data.
        For example, if the training data starts with "2018-01-01",
        then the date has ``ct1=0.0``, and "2018-01-02" has ``ct1=1/365``.
        "2019-01-01" has ``ct1=1.0``. This ``ct1`` can be as granular
        as needed. A separate growth function can be applied to ``ct1``
        to support different types of growth model. For example, ``ct2``
        is defined as the square of ``ct1`` to model quadratic growth.
    Trend:
        Trend describes the average tendency of the time series.
        It is defined through the growth term with possible changepoints.
        At every changepoint, the growth rate could change (faster or slower).
        For example, if ``ct1`` (linear growth) is used with changepoints,
        the trend is modeled as piece-wise linear.
    Seasonality:
        Seasonality describes the periodical pattern of the time series.
        It contains multiple levels including daily seasonality, weekly seasonality,
        monthly seasonality, quarterly seasonality and yearly seasonality.
        Seasonality are defined through Fourier series with different orders.
        The greater the order, the more detailed periodical pattern the model
        can learn. However, an order that is too large can lead to overfitting.
    Events:
        Events include holidays and other short-term occurrences that could
        temporarily affect the time series, such as Thanksgiving long weekend.
        Typically, events are regular and repeat at know times in the future.
        These features made of indicators that covers the event day and their neighbor days.
    Autoregression:
        Autoregressive features include the time series observations
        in the past and their aggregations. For example, the past day's observation,
        the same weekday on the past week, or the average of the past 7 days, etc.
        can be used. Note that autoregression features are very useful in short term
        forecasts, however, this should be avoided in long term forecast.
        The reason is that long-term forecast focuses more on the correctness
        of trend, seasonality and events. The lags and autoregressive terms in
        a long-term forecast are calculated based on the forecasted values.
        The further we forecast into the future, the more forecasted values we
        need to create the autoregressive terms, making the forecast less stable.
    Custom:
        Extra features that are relevant to the time series such as macro-ecomonic
        features that are expected to affect the time series.
        Note that these features need to be manually provided for both
        the training and forecasting periods.
    Interactions:
        Any interaction between the features above.

Now let's use an example to go through the full forecasting and tuning process.
In this example, we'll load a dataset representing ``log(daily page views)``
on the Wikipedia page for Peyton Manning.
It contains values from 2007-12-10 to 2016-01-20. More dataset info
`here <https://facebook.github.io/prophet/docs/quick_start.html>`_.


.. code-block:: default
   :lineno-start: 87


    import datetime

    import numpy as np
    import pandas as pd
    import plotly

    from greykite.algo.changepoint.adalasso.changepoint_detector import ChangepointDetector
    from greykite.algo.forecast.silverkite.constants.silverkite_holiday import SilverkiteHoliday
    from greykite.algo.forecast.silverkite.constants.silverkite_seasonality import SilverkiteSeasonalityEnum
    from greykite.algo.forecast.silverkite.forecast_simple_silverkite_helper import cols_interact
    from greykite.common import constants as cst
    from greykite.common.features.timeseries_features import build_time_features_df
    from greykite.common.features.timeseries_features import convert_date_to_continuous_time
    from greykite.framework.benchmark.data_loader_ts import DataLoaderTS
    from greykite.framework.templates.autogen.forecast_config import EvaluationPeriodParam
    from greykite.framework.templates.autogen.forecast_config import ForecastConfig
    from greykite.framework.templates.autogen.forecast_config import MetadataParam
    from greykite.framework.templates.autogen.forecast_config import ModelComponentsParam
    from greykite.framework.templates.forecaster import Forecaster
    from greykite.framework.templates.model_templates import ModelTemplateEnum
    from greykite.framework.utils.result_summary import summarize_grid_search_results


    # Loads dataset into UnivariateTimeSeries
    dl = DataLoaderTS()
    ts = dl.load_peyton_manning_ts()
    df = ts.df  # cleaned pandas.DataFrame








Exploratory data analysis (EDA)
--------------------------------
After reading in a time series, we could first do some exploratory data analysis.
The `~greykite.framework.input.univariate_time_series.UnivariateTimeSeries` class is
used to store a timeseries and perform EDA.


.. code-block:: default
   :lineno-start: 122


    # describe
    print(ts.describe_time_col())
    print(ts.describe_value_col())





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    {'data_points': 2964, 'mean_increment_secs': 86400.0, 'min_timestamp': Timestamp('2007-12-10 00:00:00'), 'max_timestamp': Timestamp('2016-01-20 00:00:00')}
    count    2905.000000
    mean        8.138958
    std         0.845957
    min         5.262690
    25%         7.514800
    50%         7.997999
    75%         8.580168
    max        12.846747
    Name: y, dtype: float64




The df has two columns, time column "ts" and value column "y".
The data is daily that ranges from 2007-12-10 to 2016-01-20.
The data value ranges from 5.26 to 12.84

Let's plot the original timeseries.
(The interactive plot is generated by ``plotly``: **click to zoom!**)


.. code-block:: default
   :lineno-start: 134


    fig = ts.plot()
    plotly.io.show(fig)




.. raw:: html
    :file: /home/rhossein/codes/linkedin_repos/greykite/greykite-docs/docs/gallery/tutorials/images/sphx_glr_0100_forecast_tutorial_001.html





A few exploratory plots can be plotted to reveal the time series's properties.
The `~greykite.framework.input.univariate_time_series.UnivariateTimeSeries` class
has a very powerful plotting tool
`~greykite.framework.input.univariate_time_series.UnivariateTimeSeries.plot_quantiles_and_overlays`.
A tutorial of using the function can be found at `Seasonality <../quickstart/0300_seasonality.html>`_.

Baseline model
--------------------
A simple forecast can be created on the data set,
see details in `Simple Forecast <../quickstart/0100_simple_forecast.html>`_.
Note that if you do not provide any extra parameters, all model parameters are by default.
The default parameters are chosen conservatively, so consider this a baseline
model to assess forecast difficulty and make further improvements if necessary.


.. code-block:: default
   :lineno-start: 153


    # Specifies dataset information
    metadata = MetadataParam(
        time_col="ts",  # name of the time column
        value_col="y",  # name of the value column
        freq="D"  # "H" for hourly, "D" for daily, "W" for weekly, etc.
    )

    forecaster = Forecaster()
    result = forecaster.run_forecast_config(
        df=df,
        config=ForecastConfig(
            model_template=ModelTemplateEnum.SILVERKITE.name,
            forecast_horizon=365,  # forecasts 365 steps ahead
            coverage=0.95,  # 95% prediction intervals
            metadata_param=metadata
        )
    )





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    Fitting 3 folds for each of 1 candidates, totalling 3 fits




For a detailed documentation about the output from
:py:meth:`~greykite.framework.templates.forecaster.Forecaster.run_forecast_config`,
see :doc:`/pages/stepbystep/0500_output`. Here we could plot the forecast.


.. code-block:: default
   :lineno-start: 176


    forecast = result.forecast
    fig = forecast.plot()
    plotly.io.show(fig)




.. raw:: html
    :file: /home/rhossein/codes/linkedin_repos/greykite/greykite-docs/docs/gallery/tutorials/images/sphx_glr_0100_forecast_tutorial_002.html





Model performance evaluation
----------------------------
We can see the forecast fits the existing data well; however, we do not
have a good ground truth to assess how well it predicts into the future.

Train-test-split
^^^^^^^^^^^^^^^^
The typical way to evaluate model performance is to reserve part of the training
data and use it to measure the model performance.
Because we always predict the future in a time series forecasting problem,
we reserve data from the end of training set to measure the performance
of our forecasts. This is called a time series train test split.

By default, the results returned by :py:meth:`~greykite.framework.templates.forecaster.Forecaster.run_forecast_config`
creates a time series train test split and stores the test result in ``result.backtest``.
The reserved testing data by default has the
same length as the forecast horizon. We can access the evaluation results:


.. code-block:: default
   :lineno-start: 199


    pd.DataFrame(result.backtest.test_evaluation, index=["Value"]).transpose()  # formats dictionary as a pd.DataFrame






.. only:: builder_html

    .. raw:: html

        <div>
        <style scoped>
            .dataframe tbody tr th:only-of-type {
                vertical-align: middle;
            }

            .dataframe tbody tr th {
                vertical-align: top;
            }

            .dataframe thead th {
                text-align: right;
            }
        </style>
        <table border="1" class="dataframe">
          <thead>
            <tr style="text-align: right;">
              <th></th>
              <th>Value</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th>CORR</th>
              <td>0.756897</td>
            </tr>
            <tr>
              <th>R2</th>
              <td>-0.695154</td>
            </tr>
            <tr>
              <th>MSE</th>
              <td>0.865076</td>
            </tr>
            <tr>
              <th>RMSE</th>
              <td>0.930095</td>
            </tr>
            <tr>
              <th>MAE</th>
              <td>0.856716</td>
            </tr>
            <tr>
              <th>MedAE</th>
              <td>0.840022</td>
            </tr>
            <tr>
              <th>MAPE</th>
              <td>11.3071</td>
            </tr>
            <tr>
              <th>MedAPE</th>
              <td>11.2497</td>
            </tr>
            <tr>
              <th>sMAPE</th>
              <td>5.318</td>
            </tr>
            <tr>
              <th>Q80</th>
              <td>0.187063</td>
            </tr>
            <tr>
              <th>Q95</th>
              <td>0.0664152</td>
            </tr>
            <tr>
              <th>Q99</th>
              <td>0.0342425</td>
            </tr>
            <tr>
              <th>OutsideTolerance1p</th>
              <td>0.986226</td>
            </tr>
            <tr>
              <th>OutsideTolerance2p</th>
              <td>0.972452</td>
            </tr>
            <tr>
              <th>OutsideTolerance3p</th>
              <td>0.961433</td>
            </tr>
            <tr>
              <th>OutsideTolerance4p</th>
              <td>0.933884</td>
            </tr>
            <tr>
              <th>OutsideTolerance5p</th>
              <td>0.892562</td>
            </tr>
            <tr>
              <th>Outside Tolerance (fraction)</th>
              <td>None</td>
            </tr>
            <tr>
              <th>R2_null_model_score</th>
              <td>None</td>
            </tr>
            <tr>
              <th>Prediction Band Width (%)</th>
              <td>28.276</td>
            </tr>
            <tr>
              <th>Prediction Band Coverage (fraction)</th>
              <td>0.785124</td>
            </tr>
            <tr>
              <th>Coverage: Lower Band</th>
              <td>0.754821</td>
            </tr>
            <tr>
              <th>Coverage: Upper Band</th>
              <td>0.030303</td>
            </tr>
            <tr>
              <th>Coverage Diff: Actual_Coverage - Intended_Coverage</th>
              <td>-0.164876</td>
            </tr>
          </tbody>
        </table>
        </div>
        <br />
        <br />

Evaluation metrics
^^^^^^^^^^^^^^^^^^
From here we can see a list of metrics that measure the model performance on the test data.
You may choose one or a few metrics to focus on. Typical metrics include:

  MSE:
      Mean squared error, the average squared error. Could be affected by extreme values.

  RMSE:
      Root mean squared error, the square root of MSE.

  MAE:
      Mean absolute error, the average of absolute error. Could be affected by extreme values.

  MedAE:
      Median absolute error, the median of absolute error. Less affected by extreme values.

  MAPE:
      Mean absolute percent error, measures the error percent with respective to the true values.
      This is useful when you would like to consider the relative error instead of the absolute error.
      For example, an error of 1 is considered as 10% for a true observation of 10, but as 1% for a true
      observation of 100. This is the default metric we like.

  MedAPE:
      Median absolute percent error, the median version of MAPE, less affected by extreme values.

Let's use MAPE as our metric in this example. Looking at these results,
you may have a basic sense of how the model is performing on the unseen test data.
On average, the baseline model's prediction is 11.3% away from the true values.

Time series cross-validation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Forecast quality depends a lot of the evaluation time window.
The evaluation window selected above might happen to be a relatively easy/hard period to predict.
Thus, it is more robust to evaluate over a longer time window when dataset size allows.
Let's consider a more general way of evaluating a forecast model: time series cross-validation.

Time series cross-validation is based on a time series rolling split.
Let's say we would like to perform an evaluation with a 3-fold cross-validation,
The whole training data is split in 3 different ways.
Since our forecast horizon is 365 days, we do:

    First fold:
      Train from 2007-12-10 to 2013-01-20, forecast from
      2013-01-21 to 2014-01-20, and compare the forecast with the actual.
    Second fold:
      Train from 2007-12-10 to 2014-01-20, forecast from
      2014-01-21 to 2015-01-20, and compare the forecast with the actual.
    Third fold:
      Train from 2007-12-10 to 2015-01-20, forecast from
      2015-01-21 to 2016-01-20, and compare the forecast with the actual.

The split could be more flexible, for example, the testing periods could have gaps.
For more details about evaluation period configuration, see
`Evaluation Period <../../pages/stepbystep/0400_configuration.html#evaluation-period>`_.
The forecast model's performance will be the average of the three evaluations
on the forecasts.

By default, the results returned by :py:meth:`~greykite.framework.templates.forecaster.Forecaster.run_forecast_config`
also runs time series cross-validation internally.
You are allowed to configure the cross-validation splits, as shown below.
Here note that the ``test_horizon`` are reserved from the back of
the data and not used for cross-validation.
This part of testing data can further evaluate the model performance
besides the cross-validation result, and is available for plotting.


.. code-block:: default
   :lineno-start: 268


    # Defines the cross-validation config
    evaluation_period = EvaluationPeriodParam(
        test_horizon=365,             # leaves 365 days as testing data
        cv_horizon=365,               # each cv test size is 365 days (same as forecast horizon)
        cv_max_splits=3,              # 3 folds cv
        cv_min_train_periods=365 * 4  # uses at least 4 years for training because we have 8 years data
    )

    # Runs the forecast
    result = forecaster.run_forecast_config(
        df=df,
        config=ForecastConfig(
            model_template=ModelTemplateEnum.SILVERKITE.name,
            forecast_horizon=365,  # forecasts 365 steps ahead
            coverage=0.95,  # 95% prediction intervals
            metadata_param=metadata,
            evaluation_period_param=evaluation_period
        )
    )

    # Summarizes the cv result
    cv_results = summarize_grid_search_results(
        grid_search=result.grid_search,
        decimals=1,
        # The below saves space in the printed output. Remove to show all available metrics and columns.
        cv_report_metrics=None,
        column_order=["rank", "mean_test", "split_test", "mean_train", "split_train", "mean_fit_time", "mean_score_time", "params"])
    # Transposes to save space in the printed output
    cv_results["params"] = cv_results["params"].astype(str)
    cv_results.set_index("params", drop=True, inplace=True)
    cv_results.transpose()





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    Fitting 3 folds for each of 1 candidates, totalling 3 fits


.. only:: builder_html

    .. raw:: html

        <div>
        <style scoped>
            .dataframe tbody tr th:only-of-type {
                vertical-align: middle;
            }

            .dataframe tbody tr th {
                vertical-align: top;
            }

            .dataframe thead th {
                text-align: right;
            }
        </style>
        <table border="1" class="dataframe">
          <thead>
            <tr style="text-align: right;">
              <th>params</th>
              <th>[]</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th>rank_test_MAPE</th>
              <td>1</td>
            </tr>
            <tr>
              <th>mean_test_MAPE</th>
              <td>7.3</td>
            </tr>
            <tr>
              <th>split_test_MAPE</th>
              <td>(5.1, 8.5, 8.4)</td>
            </tr>
            <tr>
              <th>mean_train_MAPE</th>
              <td>4.3</td>
            </tr>
            <tr>
              <th>split_train_MAPE</th>
              <td>(4.0, 4.3, 4.5)</td>
            </tr>
            <tr>
              <th>mean_fit_time</th>
              <td>20.8</td>
            </tr>
            <tr>
              <th>mean_score_time</th>
              <td>1.3</td>
            </tr>
          </tbody>
        </table>
        </div>
        <br />
        <br />

By default, all metrics in `~greykite.common.evaluation.ElementwiseEvaluationMetricEnum`
are computed on each CV train/test split.
The configuration of CV evaluation metrics can be found at
`Evaluation Metric <../../pages/stepbystep/0400_configuration.html#evaluation-metric>`_.
Here, we show the Mean Absolute Percentage Error (MAPE)
across splits (see `~greykite.framework.utils.result_summary.summarize_grid_search_results`
to control what to show and for details on the output columns).
From the result, we see that the cross-validation ``mean_test_MAPE`` is 7.3%, which
means the prediction is 7.3% away from the ground truth on average. We also see the
3 cv folds have ``split_test_MAPE`` 5.1%, 8.5% and 8.4%, respectively.

When we have different sets of model parameters, a good way to compare them is
to run a time series cross-validation on each set of parameters, and pick the
set of parameters that has the best cross-validated performance.

Start tuning
------------
Now that you know how to evaluate model performance,
let's see if we can improve the model by tuning its parameters.

Anomaly
^^^^^^^
An anomaly is a deviation in the metric that is not expected to occur again
in the future. Including anomaly points will lead the model to fit the
anomaly as an intrinsic property of the time series, resulting in inaccurate forecasts.
These anomalies could be identified through overlay plots, see
`Seasonality <../quickstart/0300_seasonality.html>`_.


.. code-block:: default
   :lineno-start: 329


    fig = ts.plot_quantiles_and_overlays(
        groupby_time_feature="month_dom",
        show_mean=True,
        show_quantiles=False,
        show_overlays=True,
        overlay_label_time_feature="year",
        overlay_style={"line": {"width": 1}, "opacity": 0.5},
        center_values=True,
        xlabel="day of year",
        ylabel=ts.original_value_col,
        title="yearly seasonality for each year (centered)",
    )
    plotly.io.show(fig)




.. raw:: html
    :file: /home/rhossein/codes/linkedin_repos/greykite/greykite-docs/docs/gallery/tutorials/images/sphx_glr_0100_forecast_tutorial_003.html





From the yearly overlay plot above, we could see two big anomalies:
one in March of 2012, and one in June of 2010. Other small anomalies
could be identified as well, however, they have less influence.
The ``SILVERKITE`` template currently supports masking anomaly points
by supplying the ``anomaly_info`` as a dictionary. You could
either assign adjusted values to them, or simply mask them as NA
(in which case these dates will not be used in fitting).
For a detailed introduction about the ``anomaly_info`` configuration,
see :doc:`/pages/stepbystep/0300_input`.
Here we define an ``anomaly_df`` dataframe to mask them as NA,
and wrap it into the ``anomaly_info`` dictionary.


.. code-block:: default
   :lineno-start: 356


    anomaly_df = pd.DataFrame({
        # start and end date are inclusive
        # each row is an anomaly interval
        cst.START_DATE_COL: ["2010-06-05", "2012-03-01"],  # inclusive
        cst.END_DATE_COL: ["2010-06-20", "2012-03-20"],  # inclusive
        cst.ADJUSTMENT_DELTA_COL: [np.nan, np.nan],  # mask as NA
    })
    # Creates anomaly_info dictionary.
    # This will be fed into the template.
    anomaly_info = {
        "value_col": "y",
        "anomaly_df": anomaly_df,
        "adjustment_delta_col": cst.ADJUSTMENT_DELTA_COL,
    }








Adding relevant features
^^^^^^^^^^^^^^^^^^^^^^^^

Growth and trend
""""""""""""""""
First we look at the growth and trend. Detailed growth configuration can be found
at :doc:`/pages/model_components/0200_growth`.
In these two features, we care less about the short-term fluctuations but rather long-term tendency.
From the original plot we see there is no obvious growth pattern, thus we
could use a linear growth to fit the model. On the other hand, there could be
potential trend changepoints, at which time the linear growth changes its rate.
Detailed changepoint configuration can be found at :doc:`/pages/model_components/0500_changepoints`.
These points can be detected with the ``ChangepointDetector`` class. For a quickstart example,
see `Changepoint detection <../quickstart/0200_changepoint_detection.html>`_.
Here we explore the automatic changepoint detection.
The parameters in this automatic changepoint detection is customized for this data set.
We keep the ``yearly_seasonality_order`` the same as the model's yearly seasonality order.
The ``regularization_strength`` controls how many changepoints are detected.
0.5 is a good choice, while you may try other numbers such as 0.4 or 0.6 to see the difference.
The ``resample_freq`` is set to 7 days, because we have a long training history, thus we should
keep this relatively long (the intuition is that shorter changes will be ignored).
We put 25 potential changepoints to be the candidates, because we do not expect too many changes.
However, this could be higher.
The ``yearly_seasonality_change_freq`` is set to 365 days, which means we refit the yearly seasonality
every year, because it can be see from the time series plot that the yearly seasonality varies every year.
The ``no_changepoint_distance_from_end`` is set to 365 days, which means we do not allow any changepoints
at the last 365 days of training data. This avoids fitting the final trend with too little data.
For long-term forecast, this is typically the same as the forecast horizon, while for short-term forecast,
this could be a multiple of the forecast horizon.


.. code-block:: default
   :lineno-start: 402


    model = ChangepointDetector()
    res = model.find_trend_changepoints(
        df=df,  # data df
        time_col="ts",  # time column name
        value_col="y",  # value column name
        yearly_seasonality_order=10,  # yearly seasonality order, fit along with trend
        regularization_strength=0.5,  # between 0.0 and 1.0, greater values imply fewer changepoints, and 1.0 implies no changepoints
        resample_freq="7D",  # data aggregation frequency, eliminate small fluctuation/seasonality
        potential_changepoint_n=25,  # the number of potential changepoints
        yearly_seasonality_change_freq="365D",  # varying yearly seasonality for every year
        no_changepoint_distance_from_end="365D")  # the proportion of data from end where changepoints are not allowed
    fig = model.plot(
        observation=True,
        trend_estimate=False,
        trend_change=True,
        yearly_seasonality_estimate=False,
        adaptive_lasso_estimate=True,
        plot=False)
    plotly.io.show(fig)




.. raw:: html
    :file: /home/rhossein/codes/linkedin_repos/greykite/greykite-docs/docs/gallery/tutorials/images/sphx_glr_0100_forecast_tutorial_004.html





From the plot we see the automatically detected trend changepoints.
The results shows that the time series is generally increasing until 2012,
then generally decreasing. One possible explanation is that 2011 is
the last year Peyton Manning was at the Indianapolis Colts before joining the
Denver Broncos. If we feed the trend changepoint detection parameter to the template,
these trend changepoint features will be automatically included in the model.


.. code-block:: default
   :lineno-start: 430


    # The following specifies the growth and trend changepoint configurations.
    growth = {
        "growth_term": "linear"
    }
    changepoints = {
        "changepoints_dict": dict(
            method="auto",
            yearly_seasonality_order=10,
            regularization_strength=0.5,
            resample_freq="7D",
            potential_changepoint_n=25,
            yearly_seasonality_change_freq="365D",
            no_changepoint_distance_from_end="365D"
        )
    }








Seasonality
"""""""""""
The next features we will look into are the seasonality features.
Detailed seasonality configurations can be found at
:doc:`/pages/model_components/0300_seasonality`.
A detailed seasonality detection quickstart example on the same data set is
available at `Seasonality Detection <../quickstart/0300_seasonality.html>`_.
The conclusions about seasonality terms are:

  - daily seasonality is not available (because frequency is daily);
  - weekly and yearly patterns are evident (weekly will also interact with football season);
  - monthly or quarterly seasonality is not evident.

Therefore, for pure seasonality terms, we include weekly and yearly
seasonality. The seasonality orders are something to be tuned; here
let's take weekly seasonality order to be 5 and yearly seasonality order to be 10.
For tuning info, see :doc:`/pages/model_components/0300_seasonality`.


.. code-block:: default
   :lineno-start: 465


    # Includes yearly seasonality with order 10 and weekly seasonality with order 5.
    # Set the other seasonality to False to disable them.
    yearly_seasonality_order = 10
    weekly_seasonality_order = 5
    seasonality = {
        "yearly_seasonality": yearly_seasonality_order,
        "quarterly_seasonality": False,
        "monthly_seasonality": False,
        "weekly_seasonality": weekly_seasonality_order,
        "daily_seasonality": False
    }








We will add the interaction between weekly seasonality and the football season
later in this tutorial.
The ``SILVERKITE`` template also supports seasonality changepoints. A seasonality
changepoint is a time point after which the periodic effect behaves
differently. For ``SILVERKITE``, this means the Fourier series coefficients are allowed
to change. We could decide to add this feature if cross-validation performance is poor
and seasonality changepoints are detected in exploratory analysis.
For details, see :doc:`/gallery/quickstart/0200_changepoint_detection`.

Holidays and events
"""""""""""""""""""
Then let's look at holidays and events. Detailed holiday and event configurations
can be found at :doc:`/pages/model_components/0400_events`.
Ask yourself which holidays are likely to affect the time series' values.
We expect that major United States holidays may affect wikipedia pageviews,
since most football fans are in the United States.
Events such as superbowl could potentially increase the pageviews.
Therefore, we add United States holidays and superbowls dates as custom events.
Other important events that affect the time series can also be found
through the yearly seasonality plots in `Seasonality <../quickstart/0300_seasonality.html>`_.


.. code-block:: default
   :lineno-start: 500


    # Includes major holidays and the superbowl date.
    events = {
        # These holidays as well as their pre/post dates are modeled as individual events.
        "holidays_to_model_separately": SilverkiteHoliday.ALL_HOLIDAYS_IN_COUNTRIES,  # all holidays in "holiday_lookup_countries"
        "holiday_lookup_countries": ["UnitedStates"],  # only look up holidays in the United States
        "holiday_pre_num_days": 2,  # also mark the 2 days before a holiday as holiday
        "holiday_post_num_days": 2,  # also mark the 2 days after a holiday as holiday
        "daily_event_df_dict": {
            "superbowl": pd.DataFrame({
                "date": ["2008-02-03", "2009-02-01", "2010-02-07", "2011-02-06",
                         "2012-02-05", "2013-02-03", "2014-02-02", "2015-02-01", "2016-02-07"],  # dates must cover training and forecast period.
                "event_name": ["event"] * 9  # labels
            })
        },
    }








Autoregression
""""""""""""""
The autoregressive features are very useful in short-term forecasting, but
could be risky to use in long-term forecasting. Detailed autoregression
configurations can be found at :doc:`/pages/model_components/0800_autoregression`.

Custom
""""""
Now we consider some custom features that could relate to the pageviews. The documentation for
extra regressors can be found at :Doc:`/pages/model_components/0700_regressors`. As mentioned
in `Seasonality <../quickstart/0300_seasonality.html>`_, we observe that the football
season heavily affects the pageviews, therefore we need to use regressors to identify the football season.
There are multiple ways to include this feature: adding indicator for the whole season;
adding number of days till season start (end) and number of days since season start (end).
The former puts a uniform effect over all in-season dates, while the latter quantify
the on-ramp and down-ramp. If you are not sure which effect to include, it's ok to include both
effects. ``SILVERKITE`` has the option to use Ridge regression as the fit algorithm to avoid
over-fitting too many features. Note that many datetime features could also be added to
the model as features. ``SILVERKITE`` calculates some of these features, which can be added to
``extra_pred_cols`` as an arbitrary patsy expression.
For a full list of such features, see `~greykite.common.features.timeseries_features.build_time_features_df`.

If a feature is not automatically created by ``SILVERKITE``, we need to create it
beforehand and append it to the data df.
Here we create the "is_football_season" feature.
Note that we also need to provide the customized column for the forecast horizon period as well.
The way we do it is to first create the df with timestamps covering the forecast horizon.
This can be done with the `~greykite.framework.input.univariate_time_series.UnivariateTimeSeries.make_future_dataframe`
function within the `~greykite.framework.input.univariate_time_series.UnivariateTimeSeries` class.
Then we create a new column of our customized regressor for this augmented df.


.. code-block:: default
   :lineno-start: 548


    # Makes augmented df with forecast horizon 365 days
    df_full = ts.make_future_dataframe(periods=365)
    # Builds "df_features" that contains datetime information of the "df"
    df_features = build_time_features_df(
        dt=df_full["ts"],
        conti_year_origin=convert_date_to_continuous_time(df_full["ts"][0])
    )

    # Roughly approximates the football season.
    # "woy" is short for "week of year", created above.
    # Football season is roughly the first 6 weeks and last 17 weeks in a year.
    is_football_season = (df_features["woy"] <= 6) | (df_features["woy"] >= 36)
    # Adds the new feature to the dataframe.
    df_full["is_football_season"] = is_football_season.astype(int).tolist()
    df_full.reset_index(drop=True, inplace=True)

    # Configures regressor column.
    regressors = {
        "regressor_cols": ["is_football_season"]
    }








Interactions
""""""""""""
Finally, let's consider what possible interactions are relevant to the forecast problem.
Generally speaking, if a feature behaves differently on different values of another feature,
these two features could have potential interaction effects.
As in `Seasonality <../quickstart/0300_seasonality.html>`_, the weekly seasonality
is different through football season and non-football season, therefore, the multiplicative
term ``is_football_season x weekly_seasonality`` is able to capture this pattern.


.. code-block:: default
   :lineno-start: 579


    fig = ts.plot_quantiles_and_overlays(
        groupby_time_feature="str_dow",
        show_mean=True,
        show_quantiles=False,
        show_overlays=True,
        center_values=True,
        overlay_label_time_feature="month",  # splits overlays by month
        overlay_style={"line": {"width": 1}, "opacity": 0.5},
        xlabel="day of week",
        ylabel=ts.original_value_col,
        title="weekly seasonality by month",
    )
    plotly.io.show(fig)




.. raw:: html
    :file: /home/rhossein/codes/linkedin_repos/greykite/greykite-docs/docs/gallery/tutorials/images/sphx_glr_0100_forecast_tutorial_005.html





Now let's create the interaction terms: interaction between ``is_football_season`` and ``weekly seasonality``.
The interaction terms between a feature and a seasonality feature
can be created with the `~greykite.algo.forecast.silverkite.forecast_simple_silverkite_helper.cols_interact` function.


.. code-block:: default
   :lineno-start: 598


    football_week = cols_interact(
        static_col="is_football_season",
        fs_name=SilverkiteSeasonalityEnum.WEEKLY_SEASONALITY.value.name,
        fs_order=weekly_seasonality_order,
        fs_seas_name=SilverkiteSeasonalityEnum.WEEKLY_SEASONALITY.value.seas_names
    )

    extra_pred_cols = football_week








Moreover, the multiplicative term ``month x weekly_seasonality`` and the ``dow_woy`` features also
account for the varying weekly seasonality through the year. One could added these features, too.
Here we just leave them out. You may use ``cols_interact`` again to create the ``month x weekly_seasonality``
similar to ``is_football_season x weekly_seasonality``. ``dow_woy`` is automatically calcuated by ``SILVERKITE``,
you may simply append the name to ``extra_pred_cols`` to include it in the model.

Putting things together
^^^^^^^^^^^^^^^^^^^^^^^
Now let's put everything together and produce a new forecast.
A detailed template documentation can be found at
:doc:`/pages/stepbystep/0400_configuration`.
We first configure the ``MetadataParam`` class.
The ``MetadataParam`` class includes basic proporties of the time series itself.


.. code-block:: default
   :lineno-start: 622


    metadata = MetadataParam(
        time_col="ts",              # column name of timestamps in the time series df
        value_col="y",              # column name of the time series values
        freq="D",                   # data frequency, here we have daily data
        anomaly_info=anomaly_info,  # this is the anomaly information we defined above,
        train_end_date=datetime.datetime(2016, 1, 20)
    )








Next we define the ``ModelComponentsParam`` class based on the discussion on relevant features.
The ``ModelComponentsParam`` include properties related to the model itself.


.. code-block:: default
   :lineno-start: 634


    model_components = ModelComponentsParam(
        seasonality=seasonality,
        growth=growth,
        events=events,
        changepoints=changepoints,
        autoregression=None,
        regressors=regressors,  # is_football_season defined above
        uncertainty={
            "uncertainty_dict": "auto",
        },
        custom={
            # What algorithm is used to learn the relationship between the time series and the features.
            # Regularized fitting algorithms are recommended to mitigate high correlations and over-fitting.
            # If you are not sure what algorithm to use, "ridge" is a good choice.
            "fit_algorithm_dict": {
                "fit_algorithm": "ridge",
            },
            "extra_pred_cols": extra_pred_cols  # the interaction between is_football_season and weekly seasonality defined above
        }
    )








Now let's run the model with the new configuration.
The evaluation config is kept the same as the previous case;
this is important for a fair comparison of parameter sets.


.. code-block:: default
   :lineno-start: 660


    # Runs the forecast
    result = forecaster.run_forecast_config(
        df=df_full,
        config=ForecastConfig(
            model_template=ModelTemplateEnum.SILVERKITE.name,
            forecast_horizon=365,  # forecasts 365 steps ahead
            coverage=0.95,  # 95% prediction intervals
            metadata_param=metadata,
            model_components_param=model_components,
            evaluation_period_param=evaluation_period
        )
    )

    # Summarizes the cv result
    cv_results = summarize_grid_search_results(
        grid_search=result.grid_search,
        decimals=1,
        # The below saves space in the printed output. Remove to show all available metrics and columns.
        cv_report_metrics=None,
        column_order=["rank", "mean_test", "split_test", "mean_train", "split_train", "mean_fit_time", "mean_score_time", "params"])
    # Transposes to save space in the printed output
    cv_results["params"] = cv_results["params"].astype(str)
    cv_results.set_index("params", drop=True, inplace=True)
    cv_results.transpose()





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    Fitting 3 folds for each of 1 candidates, totalling 3 fits


.. only:: builder_html

    .. raw:: html

        <div>
        <style scoped>
            .dataframe tbody tr th:only-of-type {
                vertical-align: middle;
            }

            .dataframe tbody tr th {
                vertical-align: top;
            }

            .dataframe thead th {
                text-align: right;
            }
        </style>
        <table border="1" class="dataframe">
          <thead>
            <tr style="text-align: right;">
              <th>params</th>
              <th>[]</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th>rank_test_MAPE</th>
              <td>1</td>
            </tr>
            <tr>
              <th>mean_test_MAPE</th>
              <td>5.5</td>
            </tr>
            <tr>
              <th>split_test_MAPE</th>
              <td>(3.9, 8.7, 3.8)</td>
            </tr>
            <tr>
              <th>mean_train_MAPE</th>
              <td>3.5</td>
            </tr>
            <tr>
              <th>split_train_MAPE</th>
              <td>(3.5, 3.6, 3.3)</td>
            </tr>
            <tr>
              <th>mean_fit_time</th>
              <td>25.1</td>
            </tr>
            <tr>
              <th>mean_score_time</th>
              <td>1.5</td>
            </tr>
          </tbody>
        </table>
        </div>
        <br />
        <br />

Now we see that after analyzing the problem and adding appropriate features,
the cross-validation test MAPE is 5.4%, which is improved compared with the baseline (7.3%).
The 3 cv folds also have their MAPE reduced to 3.9%, 8.7% and 3.8%, respectively.
The first and third fold improved significantly. With some investigation, we can see that
the second fold did not improve because there is a trend changepoint right at the the start
of its test period.

It would be hard to know this situation until we see it. In the cross-validation step, one
way to avoid this is to set a different evaluation period. However, leaving this period
also makes sense because it could happen again in the future.
In the forecast period, we could monitor the forecast and actual, and re-train the model
to adapt to the most recent pattern if we see a deviation. In the changepoints dictionary,
tune ``regularization_strength`` or ``no_changepoint_distance_from_end`` accordingly, or
add manually specified changepoints to the automatically detected ones. For details, see
:doc:`/pages/model_components/0500_changepoints`.

We could also plot the forecast.


.. code-block:: default
   :lineno-start: 704


    forecast = result.forecast
    fig = forecast.plot()
    plotly.io.show(fig)




.. raw:: html
    :file: /home/rhossein/codes/linkedin_repos/greykite/greykite-docs/docs/gallery/tutorials/images/sphx_glr_0100_forecast_tutorial_006.html





Check model summary
^^^^^^^^^^^^^^^^^^^
To further investigate the model mechanism, it's also helpful
to see the model summary.
The `~greykite.algo.common.model_summary.ModelSummary` module
provides model results such as estimations, significance, p-values,
confidence intervals, etc.
that can help the user understand how the model works and
what can be further improved.

The model summary is a class method of the estimator and can be used as follows.


.. code-block:: default
   :lineno-start: 721


    summary = result.model[-1].summary()  # -1 retrieves the estimator from the pipeline
    print(summary)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    ================================ Model Summary =================================

    Number of observations: 2964,   Number of features: 287
    Method: Ridge regression
    Number of nonzero features: 287
    Regularization parameter: 2.848

    Residuals:
             Min           1Q       Median           3Q          Max
          -2.092      -0.2289     -0.05127       0.1587        3.205

                 Pred_col   Estimate Std. Err Pr(>)_boot sig. code                   95%CI
                Intercept      7.803  0.05541     <2e-16       ***          (7.703, 7.909)
     events_Christmas Day    -0.3566   0.1276      0.006        **     (-0.5798, -0.09617)
      events_C...bserved)    -0.3852   0.3003      0.172                 (-0.839, 0.07946)
      events_C...erved)-1     -0.289   0.2936      0.360                 (-0.7673, 0.2281)
      events_C...erved)-2    -0.2097   0.2625      0.498                 (-0.6635, 0.2282)
      events_C...erved)+1   0.008593  0.06733      0.778                 (-0.1228, 0.1459)
      events_C...erved)+2    0.04168  0.05988      0.438                (-0.07438, 0.1652)
      events_C...as Day-1    -0.1885   0.1269      0.124                 (-0.4299, 0.0477)
      events_C...as Day-2   -0.07981   0.1984      0.704                 (-0.5069, 0.2454)
      events_C...as Day+1    -0.2303   0.1293      0.066         .      (-0.4616, 0.02968)
      events_C...as Day+2    0.07615  0.08837      0.408                  (-0.0746, 0.263)
      events_Columbus Day    -0.1138   0.1482      0.448                 (-0.3956, 0.1944)
      events_C...us Day-1    0.07423   0.0753      0.328                (-0.08363, 0.2124)
      events_C...us Day-2   -0.05108   0.0579      0.368                (-0.1621, 0.05822)
      events_C...us Day+1    0.01457    0.104      0.900                 (-0.1954, 0.2143)
      events_C...us Day+2   0.005195  0.09899      0.964                 (-0.1925, 0.1849)
      events_I...ence Day   -0.03354  0.07079      0.634                 (-0.1629, 0.1012)
      events_I...bserved)    -0.1073  0.05468      0.028         *           (-0.1953, 0.)
      events_I...erved)-1    -0.1054  0.06969      0.112                (-0.2336, 0.02175)
      events_I...erved)-2    -0.0639  0.05602      0.270                (-0.1656, 0.04674)
      events_I...erved)+1    0.01105  0.06436      0.856                 (-0.1021, 0.1361)
      events_I...erved)+2    0.08295   0.1157      0.540                (-0.09126, 0.3112)
      events_I...ce Day-1     -0.117  0.05444      0.028         *     (-0.2023, 0.003908)
      events_I...ce Day-2    -0.1045  0.05646      0.064         .     (-0.2183, 0.006299)
      events_I...ce Day+1   -0.03637  0.07187      0.620                  (-0.1555, 0.108)
      events_I...ce Day+2   -0.03666  0.07938      0.634                 (-0.1654, 0.1362)
         events_Labor Day    -0.9081   0.1465     <2e-16       ***       (-1.121, -0.5565)
       events_Labor Day-1   -0.08142   0.1205      0.468                 (-0.3159, 0.1447)
       events_Labor Day-2   -0.07605  0.06069      0.198                (-0.1926, 0.05074)
       events_Labor Day+1    -0.4698  0.09686     <2e-16       ***      (-0.6497, -0.2709)
       events_Labor Day+2    -0.1605  0.08321      0.046         *    (-0.3105, -0.001678)
      events_M... Jr. Day     0.2639   0.1919      0.170                 (-0.1121, 0.6481)
      events_M...r. Day-1     0.2341   0.2279      0.310                  (-0.1796, 0.704)
      events_M...r. Day-2   -0.06938  0.09999      0.464                 (-0.2463, 0.1427)
      events_M...r. Day+1   -0.09268   0.1511      0.532                 (-0.3889, 0.1999)
      events_M...r. Day+2    0.03705   0.1158      0.806                 (-0.1842, 0.2544)
      events_Memorial Day     -0.172  0.04817      0.002        **     (-0.2539, -0.07448)
      events_M...al Day-1    -0.1218  0.06899      0.068         .      (-0.2312, 0.03646)
      events_M...al Day-2   -0.06832  0.09053      0.438                 (-0.2104, 0.1421)
      events_M...al Day+1   -0.03727  0.05343      0.492                (-0.1361, 0.07449)
      events_M...al Day+2    0.08794  0.07888      0.254                (-0.07074, 0.2441)
     events_New Years Day    -0.1494  0.08484      0.074         .      (-0.2974, 0.02739)
      events_N...bserved)     0.0206   0.0409      0.540                (-0.06284, 0.1051)
      events_N...erved)-1    -0.0941  0.06109      0.082         .     (-0.2039, 0.005784)
      events_N...erved)-2   -0.04235   0.1354      0.698                 (-0.2933, 0.1965)
      events_N...erved)+1     0.1807   0.1178      0.082         .       (-0.0286, 0.3657)
      events_N...erved)+2    0.04302  0.04313      0.278                (-0.03583, 0.1303)
      events_N...rs Day-1   -0.02544  0.08409      0.736                 (-0.1879, 0.1443)
      events_N...rs Day-2     0.1148   0.1114      0.328                  (-0.1016, 0.314)
      events_N...rs Day+1     0.1684  0.07893      0.032         *       (0.02531, 0.3251)
      events_N...rs Day+2     0.1893   0.1281      0.142                 (-0.04292, 0.463)
      events_Thanksgiving   -0.07547  0.07127      0.290                 (-0.2041, 0.0652)
      events_T...giving-1    -0.2546  0.06687      0.002        **      (-0.3732, -0.1024)
      events_T...giving-2    -0.2523  0.07763      0.002        **     (-0.3926, -0.09142)
      events_T...giving+1   -0.04444   0.0828      0.594                 (-0.2015, 0.1134)
      events_T...giving+2    -0.1189  0.05926      0.038         *     (-0.2246, 0.001758)
      events_Veterans Day   -0.03341  0.05812      0.608                (-0.1419, 0.07594)
      events_V...bserved)    -0.1164  0.08249      0.086         .           (-0.2538, 0.)
      events_V...erved)-1    0.03432  0.02971      0.140              (-0.001452, 0.09585)
      events_V...erved)-2  -0.008749   0.0206      0.406               (-0.06177, 0.02336)
      events_V...erved)+1   -0.05363  0.03861      0.084         .           (-0.1238, 0.)
      events_V...erved)+2   -0.04841  0.03664      0.100                     (-0.1144, 0.)
      events_V...ns Day-1   -0.07678  0.06152      0.218                (-0.1896, 0.04387)
      events_V...ns Day-2    -0.0182  0.07336      0.790                 (-0.1543, 0.1416)
      events_V...ns Day+1   -0.02022  0.06396      0.726                 (-0.1485, 0.1012)
      events_V...ns Day+2   -0.04613   0.0426      0.268                (-0.1262, 0.04784)
      events_W...Birthday    -0.0329  0.08141      0.704                 (-0.1675, 0.1315)
      events_W...rthday-1    -0.2622  0.06801     <2e-16       ***       (-0.3831, -0.115)
      events_W...rthday-2    -0.1086  0.05133      0.038         *    (-0.1969, -0.001164)
      events_W...rthday+1   -0.05971  0.06095      0.328                (-0.1566, 0.07939)
      events_W...rthday+2    -0.1126  0.03431      0.002        **     (-0.1756, -0.04283)
         events_superbowl     0.4419   0.2582      0.096         .      (-0.05191, 0.9668)
            str_dow_2-Tue    0.02405  0.01534      0.128              (-0.003447, 0.05931)
            str_dow_3-Wed    0.01784  0.01205      0.134              (-0.003942, 0.04181)
            str_dow_4-Thu   0.006795  0.01355      0.590               (-0.01922, 0.03577)
            str_dow_5-Fri   -0.02559  0.01242      0.030         *   (-0.04805, -0.001831)
            str_dow_6-Sat    -0.0495  0.01127     <2e-16       ***    (-0.07058, -0.02766)
            str_dow_7-Sun  -0.008702  0.01565      0.588               (-0.04051, 0.02063)
      is_footb...w_weekly   -0.05625   0.0236      0.024         *    (-0.1045, -0.009711)
      is_footb...w_weekly     0.4787  0.02505     <2e-16       ***        (0.4314, 0.5291)
      is_footb...w_weekly   -0.02021   0.0114      0.068         .    (-0.04091, 0.001503)
      is_footb...w_weekly     0.1007  0.01239     <2e-16       ***        (0.07339, 0.122)
      is_footb...w_weekly   -0.02886  0.01121      0.014         *   (-0.04938, -0.007815)
      is_footb...w_weekly   0.008454  0.01391      0.534               (-0.01795, 0.03547)
      is_footb...w_weekly    0.02886  0.01121      0.014         *     (0.007815, 0.04938)
      is_footb...w_weekly   0.008454  0.01391      0.534               (-0.01795, 0.03547)
      is_footb...w_weekly    0.02021   0.0114      0.068         .    (-0.001503, 0.04091)
      is_footb...w_weekly     0.1007  0.01239     <2e-16       ***        (0.07339, 0.122)
                      ct1    -0.4201  0.06607     <2e-16       ***      (-0.5594, -0.2893)
           is_weekend:ct1   -0.06344   0.0359      0.078         .     (-0.1317, 0.006213)
        str_dow_2-Tue:ct1    -0.0147  0.06627      0.828                  (-0.152, 0.1047)
        str_dow_3-Wed:ct1   -0.08275  0.04424      0.054         .     (-0.1614, 0.003656)
        str_dow_4-Thu:ct1   -0.03337  0.03986      0.416                (-0.1146, 0.03157)
        str_dow_5-Fri:ct1   -0.01293  0.03753      0.692                (-0.08226, 0.0584)
        str_dow_6-Sat:ct1   -0.02598  0.04115      0.546                (-0.1112, 0.05402)
        str_dow_7-Sun:ct1   -0.03745  0.06225      0.540                (-0.1531, 0.09196)
       is_football_season     0.5158  0.08845     <2e-16       ***        (0.3511, 0.6904)
        cp0_2008_07_21_00    -0.2149  0.06145      0.002        **      (-0.319, -0.08504)
      is_weeke...07_21_00   -0.07226  0.03494      0.028         *    (-0.1366, -0.006034)
      str_dow_...07_21_00   -0.05792  0.03366      0.072         .      (-0.1084, 0.01511)
      str_dow_...07_21_00  -0.004965   0.0256      0.846               (-0.05651, 0.04557)
      str_dow_...07_21_00    -0.0411  0.02561      0.118                (-0.0886, 0.01106)
      str_dow_...07_21_00   -0.03848  0.02514      0.122               (-0.08457, 0.01454)
      str_dow_...07_21_00   -0.06369   0.0267      0.018         *    (-0.1122, -0.007754)
      str_dow_...07_21_00  -0.008568  0.03255      0.814               (-0.06665, 0.05376)
        cp1_2008_11_10_00      1.003  0.06053     <2e-16       ***         (0.8731, 1.099)
      is_weeke...11_10_00     0.2044  0.03399     <2e-16       ***         (0.126, 0.2665)
      str_dow_...11_10_00     0.1291  0.04552      0.006        **       (0.04808, 0.2237)
      str_dow_...11_10_00     0.1554  0.03285     <2e-16       ***       (0.08542, 0.2096)
      str_dow_...11_10_00     0.1136  0.03149     <2e-16       ***       (0.05793, 0.1821)
      str_dow_...11_10_00     0.1202  0.03636     <2e-16       ***       (0.04016, 0.1853)
      str_dow_...11_10_00     0.1074   0.0346      0.002        **       (0.03277, 0.1746)
      str_dow_...11_10_00    0.09702  0.04406      0.030         *      (0.009347, 0.1749)
        cp2_2009_03_09_00     0.3711  0.06626     <2e-16       ***        (0.2469, 0.4956)
      is_weeke...03_09_00     0.1121  0.03968      0.010         *       (0.03981, 0.1898)
      str_dow_...03_09_00     0.0434  0.04916      0.396                 (-0.0486, 0.1413)
      str_dow_...03_09_00     0.0452  0.03772      0.250                (-0.02702, 0.1158)
      str_dow_...03_09_00     0.0313  0.03719      0.416                 (-0.03873, 0.104)
      str_dow_...03_09_00    0.04474  0.04063      0.266                 (-0.03675, 0.122)
      str_dow_...03_09_00    0.07753  0.04194      0.076         .     (0.0006661, 0.1641)
      str_dow_...03_09_00     0.0346  0.05262      0.490                (-0.07586, 0.1384)
        cp3_2009_10_19_00    -0.4704  0.07806     <2e-16       ***      (-0.6102, -0.3001)
      is_weeke...10_19_00    -0.1084   0.0444      0.022         *     (-0.2052, -0.02789)
      str_dow_...10_19_00    -0.0759  0.05357      0.156                (-0.1839, 0.01733)
      str_dow_...10_19_00    -0.0874  0.04452      0.052         .    (-0.1767, -0.001941)
      str_dow_...10_19_00   -0.04999   0.0383      0.190                (-0.1247, 0.02468)
      str_dow_...10_19_00   -0.05887   0.0453      0.182                (-0.1526, 0.02718)
      str_dow_...10_19_00   -0.04535  0.04263      0.268                 (-0.126, 0.04536)
      str_dow_...10_19_00   -0.06306   0.0473      0.156                (-0.1546, 0.02546)
        cp4_2010_02_15_00     -0.477  0.08124     <2e-16       ***      (-0.6298, -0.3136)
      is_weeke...02_15_00      -0.14  0.05248      0.010         *      (-0.2464, -0.0486)
      str_dow_...02_15_00   -0.05004  0.05473      0.384                (-0.1599, 0.06216)
      str_dow_...02_15_00   -0.08166  0.04601      0.078         .     (-0.1727, 0.007498)
      str_dow_...02_15_00   -0.04409  0.03929      0.258                 (-0.124, 0.03344)
      str_dow_...02_15_00   -0.08251  0.04989      0.096         .      (-0.1908, 0.01253)
      str_dow_...02_15_00   -0.07317  0.04446      0.086         .      (-0.163, 0.007691)
      str_dow_...02_15_00   -0.06685   0.0557      0.244                (-0.1779, 0.03659)
        cp5_2010_06_07_00     0.1524  0.06417      0.018         *       (0.01499, 0.2656)
      is_weeke...06_07_00    0.04952  0.04313      0.250                (-0.03866, 0.1318)
      str_dow_...06_07_00   0.005808  0.04286      0.904               (-0.07695, 0.09608)
      str_dow_...06_07_00    0.05367  0.03429      0.108                 (-0.01536, 0.116)
      str_dow_...06_07_00    0.04172  0.03455      0.234                (-0.02791, 0.1072)
      str_dow_...06_07_00  -0.001987  0.04307      0.958               (-0.08822, 0.07951)
      str_dow_...06_07_00     0.0292  0.03995      0.470                (-0.04749, 0.1019)
      str_dow_...06_07_00    0.02032  0.04714      0.644                 (-0.0659, 0.1193)
        cp6_2011_01_24_00     0.2651  0.08315      0.004        **         (0.122, 0.4442)
      is_weeke...01_24_00    0.06135  0.05733      0.276                (-0.05855, 0.1754)
      str_dow_...01_24_00    0.02369  0.06516      0.690                  (-0.1091, 0.148)
      str_dow_...01_24_00     0.0421  0.04604      0.370                (-0.04294, 0.1396)
      str_dow_...01_24_00    0.01953  0.03888      0.614                (-0.05606, 0.0971)
      str_dow_...01_24_00    0.03062   0.0552      0.570                (-0.08018, 0.1414)
      str_dow_...01_24_00    0.02935  0.05247      0.580                 (-0.06415, 0.135)
      str_dow_...01_24_00      0.032  0.07436      0.670                  (-0.1276, 0.164)
        cp7_2011_05_16_00     0.3743  0.07629     <2e-16       ***        (0.2185, 0.5185)
      is_weeke...05_16_00    0.06395   0.0517      0.218                (-0.04038, 0.1609)
      str_dow_...05_16_00    0.07994  0.04316      0.060         .     (-0.007283, 0.1612)
      str_dow_...05_16_00     0.0699  0.04363      0.110                (-0.02299, 0.1558)
      str_dow_...05_16_00    0.03932  0.04318      0.338                (-0.04542, 0.1193)
      str_dow_...05_16_00    0.05649  0.05484      0.322                (-0.04965, 0.1606)
      str_dow_...05_16_00    0.01349  0.05594      0.804                (-0.09634, 0.1181)
      str_dow_...05_16_00    0.05045  0.05049      0.336                (-0.05563, 0.1359)
        cp8_2012_01_02_00    -0.2182  0.09669      0.022         *     (-0.4522, -0.07285)
      is_weeke...01_02_00   0.009077  0.04852      0.856               (-0.09939, 0.09003)
      str_dow_...01_02_00   -0.05135  0.06344      0.398                (-0.1788, 0.06947)
      str_dow_...01_02_00   -0.07913  0.05276      0.138                (-0.2005, 0.01249)
      str_dow_...01_02_00   -0.08078  0.04689      0.078         .    (-0.1771, 0.0009338)
      str_dow_...01_02_00     0.0531  0.07158      0.450                (-0.08662, 0.1869)
      str_dow_...01_02_00  -0.009237  0.06045      0.880                 (-0.143, 0.08286)
      str_dow_...01_02_00    0.01831  0.06302      0.760                 (-0.1029, 0.1469)
        cp9_2012_04_23_00    -0.9381  0.09047     <2e-16       ***       (-1.097, -0.7455)
      is_weeke...04_23_00    -0.1823  0.05456      0.002        **     (-0.2941, -0.08054)
      str_dow_...04_23_00    -0.1463  0.05519      0.008        **     (-0.2522, -0.04007)
      str_dow_...04_23_00    -0.1643  0.05718      0.004        **     (-0.2817, -0.06493)
      str_dow_...04_23_00    -0.1162  0.05012      0.018         *     (-0.2177, -0.02413)
      str_dow_...04_23_00    -0.1539  0.05356     <2e-16       ***      (-0.251, -0.04483)
      str_dow_...04_23_00    -0.1028  0.05381      0.062         .     (-0.2127, -0.00365)
      str_dow_...04_23_00   -0.07953   0.0562      0.156                (-0.1818, 0.02887)
       cp10_2012_08_13_00    0.06176   0.0845      0.494                  (-0.1033, 0.224)
      is_weeke...08_13_00   -0.07427    0.043      0.084         .      (-0.1517, 0.02587)
      str_dow_...08_13_00    0.01243  0.06045      0.812                 (-0.1187, 0.1232)
      str_dow_...08_13_00     0.0877  0.04122      0.020         *       (0.01185, 0.1683)
      str_dow_...08_13_00    0.06894  0.05071      0.176                (-0.02528, 0.1705)
      str_dow_...08_13_00   -0.04406  0.05073      0.388                (-0.1451, 0.05463)
      str_dow_...08_13_00     0.0215  0.03891      0.584               (-0.05841, 0.09594)
      str_dow_...08_13_00   -0.09577  0.04917      0.050         .    (-0.1888, 0.0009876)
       cp11_2013_04_01_00     0.6097  0.06185     <2e-16       ***        (0.4841, 0.7236)
      is_weeke...04_01_00     0.1213  0.04226     <2e-16       ***       (0.03648, 0.2051)
      str_dow_...04_01_00      0.113  0.05358      0.028         *       (0.01559, 0.2179)
      str_dow_...04_01_00    0.07494  0.04858      0.128                (-0.02202, 0.1713)
      str_dow_...04_01_00    0.07154  0.04432      0.098         .     (-0.007499, 0.1537)
      str_dow_...04_01_00    0.09219  0.05188      0.072         .     (-0.006562, 0.1896)
      str_dow_...04_01_00    0.05036  0.05172      0.350                (-0.04976, 0.1471)
      str_dow_...04_01_00    0.07096  0.06753      0.298                (-0.05513, 0.2022)
       cp12_2014_03_10_00    -0.4588  0.05903     <2e-16       ***      (-0.5725, -0.3465)
      is_weeke...03_10_00   -0.07332  0.03816      0.044         *   (-0.1383, -0.0007601)
      str_dow_...03_10_00   -0.01682   0.0804      0.830                  (-0.1712, 0.148)
      str_dow_...03_10_00   -0.09497  0.05391      0.076         .       (-0.1994, 0.0182)
      str_dow_...03_10_00   -0.05342  0.05104      0.306                 (-0.1535, 0.0391)
      str_dow_...03_10_00   -0.03822  0.05382      0.492                 (-0.148, 0.05785)
      str_dow_...03_10_00   -0.07655  0.05796      0.188                (-0.1895, 0.02821)
      str_dow_...03_10_00   0.003228  0.07396      0.952                 (-0.1354, 0.1566)
      ct1:sin1_tow_weekly   -0.04642   0.0494      0.358                  (-0.1448, 0.041)
      ct1:cos1_tow_weekly    -0.1795  0.08667      0.036         *     (-0.3451, -0.01293)
      ct1:sin2_tow_weekly    0.06279  0.05699      0.282                (-0.05543, 0.1728)
      ct1:cos2_tow_weekly    -0.1322  0.07597      0.076         .     (-0.2879, 0.005016)
      cp0_2008...w_weekly    0.01753  0.04767      0.696                (-0.07375, 0.1132)
      cp0_2008...w_weekly     0.0454  0.06025      0.470                (-0.07942, 0.1618)
      cp0_2008...w_weekly   -0.07155  0.05062      0.154                 (-0.1573, 0.0356)
      cp0_2008...w_weekly    0.02691   0.0569      0.650                (-0.08029, 0.1359)
      cp1_2008...w_weekly    0.06903   0.0471      0.132                (-0.02961, 0.1629)
      cp1_2008...w_weekly     0.1525   0.0749      0.038         *       (0.01134, 0.2961)
      cp1_2008...w_weekly    0.01559   0.0519      0.752                (-0.08638, 0.1145)
      cp1_2008...w_weekly     0.1392  0.06522      0.034         *          (0.019, 0.258)
      cp2_2009...w_weekly   -0.03046  0.05296      0.594                (-0.1296, 0.07481)
      cp2_2009...w_weekly    0.04712  0.06951      0.476                (-0.08817, 0.1777)
      cp2_2009...w_weekly    0.03312  0.06006      0.610                (-0.08042, 0.1455)
      cp2_2009...w_weekly    0.01379  0.06176      0.810                 (-0.1085, 0.1292)
      cp3_2009...w_weekly   -0.04718  0.06239      0.458                (-0.1712, 0.07349)
      cp3_2009...w_weekly   -0.04884  0.08718      0.594                 (-0.2072, 0.1112)
      cp3_2009...w_weekly  -0.001207  0.06833      0.980                 (-0.1375, 0.1258)
      cp3_2009...w_weekly  -0.007164  0.07936      0.926                  (-0.1495, 0.153)
      cp4_2010...w_weekly    0.02153  0.07031      0.762                  (-0.108, 0.1692)
      cp4_2010...w_weekly  -0.003041  0.08078      0.950                 (-0.1701, 0.1603)
      cp4_2010...w_weekly  -0.009966  0.07726      0.906                 (-0.1606, 0.1459)
      cp4_2010...w_weekly   0.007884  0.07901      0.914                 (-0.1409, 0.1695)
      cp5_2010...w_weekly    0.03148  0.05538      0.586                (-0.06985, 0.1449)
      cp5_2010...w_weekly   -0.03428  0.07061      0.664                (-0.1644, 0.09872)
      cp5_2010...w_weekly   -0.05894  0.06396      0.338                (-0.1951, 0.05487)
      cp5_2010...w_weekly   -0.05203  0.06613      0.422                (-0.1817, 0.06804)
      cp6_2011...w_weekly   0.001124   0.0729      0.984                 (-0.1444, 0.1614)
      cp6_2011...w_weekly    0.06146  0.08382      0.472                 (-0.1084, 0.2101)
      cp6_2011...w_weekly  -0.004963   0.0913      0.948                 (-0.1637, 0.1844)
      cp6_2011...w_weekly    0.04231  0.07169      0.550                 (-0.1054, 0.1721)
      cp7_2011...w_weekly     0.0706   0.0688      0.288                (-0.07222, 0.1965)
      cp7_2011...w_weekly    0.04115  0.07414      0.562                (-0.08917, 0.1938)
      cp7_2011...w_weekly     0.0177  0.07073      0.828                 (-0.1149, 0.1655)
      cp7_2011...w_weekly    0.02031  0.07369      0.776                   (-0.1322, 0.16)
      cp8_2012...w_weekly    -0.1807  0.07734      0.022         *     (-0.3243, -0.01381)
      cp8_2012...w_weekly   -0.04509   0.1084      0.712                 (-0.2527, 0.1538)
      cp8_2012...w_weekly    0.06708  0.08278      0.414                 (-0.1054, 0.2265)
      cp8_2012...w_weekly   0.000601  0.09285      0.996                 (-0.1767, 0.1976)
      cp9_2012...w_weekly   -0.09577  0.07879      0.226                 (-0.2527, 0.0548)
      cp9_2012...w_weekly   -0.01311  0.08331      0.872                 (-0.1703, 0.1507)
      cp9_2012...w_weekly   -0.06793  0.08109      0.410                (-0.2171, 0.08889)
      cp9_2012...w_weekly   -0.05262  0.08011      0.538                 (-0.1985, 0.1042)
      cp10_201...w_weekly     0.1982  0.06952      0.006        **       (0.05179, 0.3214)
      cp10_201...w_weekly   -0.08764  0.09343      0.338                  (-0.2759, 0.104)
      cp10_201...w_weekly   -0.01159  0.07815      0.912                  (-0.162, 0.1302)
      cp10_201...w_weekly    -0.0533  0.08465      0.534                 (-0.2238, 0.1068)
      cp11_201...w_weekly    0.04788  0.05835      0.418                (-0.06089, 0.1642)
      cp11_201...w_weekly    0.07602  0.06818      0.246                (-0.06325, 0.2156)
      cp11_201...w_weekly    0.04648  0.07014      0.498                (-0.09535, 0.1852)
      cp11_201...w_weekly    0.08498  0.06959      0.216                 (-0.03968, 0.227)
      cp12_201...w_weekly   -0.04022  0.05327      0.438                (-0.1467, 0.07009)
      cp12_201...w_weekly   -0.06984  0.08047      0.400                 (-0.2285, 0.0858)
      cp12_201...w_weekly  0.0003325   0.0587      0.998                   (-0.12, 0.1121)
      cp12_201...w_weekly   -0.08167  0.07928      0.304                (-0.2442, 0.05791)
          sin1_tow_weekly     0.1053  0.03669      0.004        **       (0.04112, 0.1795)
          cos1_tow_weekly    0.06865  0.05095      0.172                (-0.03487, 0.1632)
          sin2_tow_weekly    -0.0226  0.02138      0.308               (-0.06102, 0.02031)
          cos2_tow_weekly    0.04849  0.02412      0.048         *     (0.003066, 0.09655)
          sin3_tow_weekly   -0.00687  0.01276      0.586                 (-0.02891, 0.022)
          cos3_tow_weekly   0.005713  0.01966      0.794               (-0.03208, 0.04429)
          sin4_tow_weekly    0.00687  0.01276      0.586                 (-0.022, 0.02891)
          cos4_tow_weekly   0.005713  0.01966      0.794               (-0.03208, 0.04429)
          sin5_tow_weekly     0.0226  0.02138      0.308               (-0.02031, 0.06102)
          cos5_tow_weekly    0.04849  0.02412      0.048         *     (0.003066, 0.09655)
          sin1_ct1_yearly   -0.04426  0.02098      0.042         *   (-0.08567, -0.003609)
          cos1_ct1_yearly     0.4169  0.05208     <2e-16       ***        (0.3163, 0.5168)
          sin2_ct1_yearly     0.1042  0.01467     <2e-16       ***       (0.07585, 0.1333)
          cos2_ct1_yearly    -0.1489  0.01432     <2e-16       ***      (-0.1779, -0.1199)
          sin3_ct1_yearly     0.1752  0.01599     <2e-16       ***        (0.1434, 0.2095)
          cos3_ct1_yearly   -0.01013  0.01298      0.412               (-0.03728, 0.01348)
          sin4_ct1_yearly   -0.04372  0.01505      0.002        **    (-0.07087, -0.01355)
          cos4_ct1_yearly    -0.0897   0.0128     <2e-16       ***      (-0.114, -0.06431)
          sin5_ct1_yearly   -0.06317  0.01189     <2e-16       ***    (-0.08674, -0.04317)
          cos5_ct1_yearly   -0.01998  0.01026      0.048         *  (-0.04012, -0.0006269)
          sin6_ct1_yearly   -0.06777   0.0154     <2e-16       ***    (-0.09973, -0.03867)
          cos6_ct1_yearly  -0.009463  0.01189      0.398               (-0.03336, 0.01314)
          sin7_ct1_yearly   -0.04924  0.01102     <2e-16       ***    (-0.07044, -0.02863)
          cos7_ct1_yearly    0.02889  0.01171      0.018         *      (0.00531, 0.05122)
          sin8_ct1_yearly    0.01905  0.01287      0.146              (-0.007489, 0.04521)
          cos8_ct1_yearly    0.06879  0.01285     <2e-16       ***      (0.04565, 0.09465)
          sin9_ct1_yearly  -0.004435  0.01223      0.708               (-0.02802, 0.01937)
          cos9_ct1_yearly   -0.03218  0.01105      0.002        **   (-0.05241, -0.009229)
         sin10_ct1_yearly   -0.06601  0.01097     <2e-16       ***    (-0.08892, -0.04556)
         cos10_ct1_yearly    -0.0234  0.01092      0.038         *   (-0.04462, -0.002115)
    Signif. Code: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Multiple R-squared: 0.7553,   Adjusted R-squared: 0.744
    F-statistic: 64.947 on 130 and 2832 DF,   p-value: 1.110e-16
    Model AIC: 18720.0,   model BIC: 19511.0

    WARNING: the condition number is large, 1.42e+05. This might indicate that there are strong multicollinearity or other numerical problems.
    WARNING: the F-ratio and its p-value on regularized methods might be misleading, they are provided only for reference purposes.





The model summary shows the model information, the coefficients and their significance,
and a few summary statistics. For example,
we can see the changepoints and how much the growth rate
changes at each changepoint.
We can see that some of the holidays have significant
effect in the model, such as Christmas, Labor day, Thanksgiving, etc.
We can see the significance of the interaction between football season and weekly seasonality
etc.

For a more detailed guide on model summary, see
:doc:`/gallery/quickstart/0400_model_summary`.

Summary in model tuning
-----------------------
After the example, you may have some sense about how to select parameters and tune the model.
Here we list a few steps and tricks that might help select the best models.
What you may do:

  #. Detect anomaly points with the overlay plots
     (`~greykite.framework.input.univariate_time_series.UnivariateTimeSeries.plot_quantiles_and_overlays`).
     Mask these points with NA. Do not specify the adjustment unless you are confident about how to correct the anomalies.

  #. Choose an appropriate way to model the growth (linear, quadratic, square root, etc.)
     If none of the typical growth shape fits the time series, you might consider linear
     growth with trend changepoints. Try different changepoint detection configurations.
     You may also plot the detected changepoints and see if it makes sense to you.
     The template also supports custom changepoints. If the automatic changepoint detection result
     does not make sense to you, you might supply your own changepoints.

  #. Choose the appropriate seasonality orders. The higher the order, the more details the model can learn.
     However, too large orders could overfit the training data. These can also be detected from the
     overlay plots (`~greykite.framework.input.univariate_time_series.UnivariateTimeSeries.plot_quantiles_and_overlays`).
     There isn't a unified way to choose seasonality, so explore different seasonality orders and compare the results.

  #. Consider what events and holidays to model. Are there any custom events we need to add?
     If you add a custom event, remember also adding the dates for the event in the forecast period.

  #. Add external regressors that could be related to the time series. Note that you will need to provide the
     values of the regressors in the forecast period as well. You may use another time series as a regressor,
     as long as you have a ground truth/good forecast for it that covers your forecast period.

  #. Adding interaction terms. Let's mention again here that there could be interaction between two features
     if the behaviors of one feature are different when the other feature have different values.
     Try to detect this through the overlay plot
     (`~greykite.framework.input.univariate_time_series.UnivariateTimeSeries.plot_quantiles_and_overlays`), too.
     By default, we have a few pre-defined interaction terms, see
     `feature_set_enabled <../../pages/model_components/0600_custom.html#interactions>`_.

  #. Choose an appropriate fit algorithm. This is the algorithm that models the relationship between the features
     and the time series. See a full list of available algorithms at
     `fit_algorithm <../../pages/model_components/0600_custom.html#fit-algorithm>`_.
     If you are unsure about their difference, try some of them and compare the results. If you don't want to, choosing "ridge"
     is a safe option.

It is worth noting that the template supports automatic grid search with different sets of parameters.
For each parameter, if you provide the configuration in a list, it will automatically run each combination
and choose the one with the best cross-validation performance. This will save a lot of time.
For details, see `grid search <../quickstart/0500_grid_search.html>`_.

Follow your insights and intuitions, and play with the parameters, you will get good forecasts!


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 7 minutes  1.983 seconds)


.. _sphx_glr_download_gallery_tutorials_0100_forecast_tutorial.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: 0100_forecast_tutorial.py <0100_forecast_tutorial.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: 0100_forecast_tutorial.ipynb <0100_forecast_tutorial.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
