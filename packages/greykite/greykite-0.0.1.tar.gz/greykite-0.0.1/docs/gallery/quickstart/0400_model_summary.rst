.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_gallery_quickstart_0400_model_summary.py>`     to download the full example code
    .. rst-class:: sphx-glr-example-title

    .. _sphx_glr_gallery_quickstart_0400_model_summary.py:


Model Summary
=============
For every forecast model trained with the ``SILVERKITE`` algorithm,
you can print the model summary with only a few lines of code.
The model summary gives you insight into model performance,
parameter significance and etc.

In this example, we will discuss how to utilize the
`~greykite.algo.common.model_summary.ModelSummary`
module to output model summary.

First we'll load a dataset representing ``log(daily page views)``
on the Wikipedia page for Peyton Manning.
It contains values from 2007-12-10 to 2016-01-20. More dataset info
`here <https://facebook.github.io/prophet/docs/quick_start.html>`_.


.. code-block:: default
   :lineno-start: 19


    import warnings

    warnings.filterwarnings("ignore")

    from greykite.common.data_loader import DataLoader
    from greykite.framework.templates.autogen.forecast_config import ForecastConfig
    from greykite.framework.templates.autogen.forecast_config import MetadataParam
    from greykite.framework.templates.autogen.forecast_config import ModelComponentsParam
    from greykite.framework.templates.model_templates import ModelTemplateEnum
    from greykite.framework.templates.forecaster import Forecaster

    # Loads dataset into pandas DataFrame
    dl = DataLoader()
    df = dl.load_peyton_manning()








Then we create a forecast model with ``SILVERKITE`` template.
For a simple example of creating a forecast model, see
`Simple Forecast <./0100_simple_forecast.html>`_.
For a detailed tuning tutorial, see
`Forecast Model Tuning <../tutorials/0100_forecast_tutorial.html>`_.


.. code-block:: default
   :lineno-start: 41


    # Specifies dataset information
    metadata = MetadataParam(
        time_col="ts",  # name of the time column
        value_col="y",  # name of the value column
        freq="D"  # "H" for hourly, "D" for daily, "W" for weekly, etc.
    )

    # Specifies model parameters
    model_components = ModelComponentsParam(
        changepoints={
            "changepoints_dict": {
                "method": "auto",
                "potential_changepoint_n": 25,
                "regularization_strength": 0.5,
                "resample_freq": "7D",
                "no_changepoint_distance_from_end": "365D"}
        },
        uncertainty={
            "uncertainty_dict": "auto",
        },
        custom={
            "fit_algorithm_dict": {
                "fit_algorithm": "linear",
            },
        }
    )

    # Runs the forecast
    forecaster = Forecaster()
    result = forecaster.run_forecast_config(
        df=df,
        config=ForecastConfig(
            model_template=ModelTemplateEnum.SILVERKITE.name,
            forecast_horizon=365,  # forecasts 365 steps ahead
            coverage=0.95,  # 95% prediction intervals
            metadata_param=metadata,
            model_components_param=model_components
        )
    )





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    Fitting 3 folds for each of 1 candidates, totalling 3 fits




Creating model summary
^^^^^^^^^^^^^^^^^^^^^^
Now that we have the output from :py:meth:`~greykite.framework.templates.forecaster.Forecaster.run_forecast_config`,
we are able to access the model summary.


.. code-block:: default
   :lineno-start: 87


    # Initializes the model summary class.
    # ``max_colwidth`` is the maximum length of predictor names that can be displayed.
    summary = result.model[-1].summary(max_colwidth=30)








The above command creates a model summary class and derives extra information
that summarizes the model. Generally the summarized information includes
the following sections:

  #. **Model parameter section:** includes basic model parameter information such
     as number of observations, number of features, model name and etc.
  #. **Model residual section:** includes the five number summary of training residuals.
  #. **Model coefficients section (for regression model):** the estimated coefficients
     and their p-values/confidence intervals. For linear regression, these are the
     conventional results; for ridge regression, these are calculated from bootstrap [1]_;
     for lasso regression, these are calculated by multi-sample-splitting [2]_.
  #. **Model coefficients section (for tree model):** the feature significance.
  #. **Model significance section (for regression model only):** the overall significance
     of the regression model, including the coefficient of determination, the
     F-ratio and its p-value, and model AIC/BIC. The results are based on classical
     statistical inference and may not be reliable for regularized methods (ridge, lasso, etc.).
  #. **Warning section:** any warnings for the model summary such as high multicollinearity
     are displayed in this section.

To see the summary, you can either type ``summary`` or ``print(summary)``.


.. code-block:: default
   :lineno-start: 113


    # Prints the summary
    print(summary)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    ================================ Model Summary =================================

    Number of observations: 2964,   Number of features: 295
    Method: Ordinary least squares
    Number of nonzero features: 295

    Residuals:
             Min           1Q       Median           3Q          Max
          -1.911      -0.2596     -0.04944       0.1781        3.418

                          Pred_col   Estimate Std. Err    t value  Pr(>|t|) sig. code                  95%CI
                         Intercept      7.067  0.07816      90.41    <2e-16       ***          (6.913, 7.22)
           events_Chinese New Year  -0.002513   0.1707   -0.01472     0.988                (-0.3372, 0.3321)
         events_Chinese New Year-1   -0.06487   0.1707    -0.3801     0.704                (-0.3995, 0.2698)
         events_Chinese New Year-2    0.03329   0.1707     0.1951     0.845                (-0.3014, 0.3679)
         events_Chinese New Year+1   -0.08899   0.1706    -0.5215     0.602                (-0.4236, 0.2456)
         events_Chinese New Year+2     0.3175   0.1706      1.861     0.063         .     (-0.01708, 0.6521)
              events_Christmas Day    -0.5985   0.1808      -3.31  9.46e-04       ***     (-0.9531, -0.2439)
            events_Christmas Day-1    -0.3339   0.1788     -1.867     0.062         .     (-0.6845, 0.01674)
            events_Christmas Day-2    -0.1267   0.1759    -0.7202     0.471                (-0.4716, 0.2182)
            events_Christmas Day+1    -0.4725   0.1819     -2.597     0.009        **     (-0.8292, -0.1158)
            events_Christmas Day+2    0.08283   0.1813     0.4568     0.648                (-0.2727, 0.4383)
     events_Easter...hern Ireland]     -0.256   0.1737     -1.473     0.141                (-0.5966, 0.0847)
     events_Easter...rn Ireland]-1    -0.1193  0.08686     -1.374     0.170               (-0.2896, 0.05101)
     events_Easter...rn Ireland]-2   -0.06177  0.08814    -0.7007     0.484                (-0.2346, 0.1111)
     events_Easter...rn Ireland]+1    -0.1009   0.1737    -0.5807     0.561                (-0.4415, 0.2397)
     events_Easter...rn Ireland]+2  -0.001061    0.172  -0.006168     0.995                (-0.3383, 0.3362)
                events_Good Friday    -0.1968   0.1745     -1.128     0.259                 (-0.539, 0.1454)
              events_Good Friday-1    -0.1382   0.1722    -0.8026     0.422                (-0.4759, 0.1995)
              events_Good Friday-2    -0.0244   0.1725    -0.1415     0.888                (-0.3626, 0.3138)
              events_Good Friday+1   -0.06177  0.08814    -0.7007     0.484                (-0.2346, 0.1111)
              events_Good Friday+2    -0.1193  0.08686     -1.374     0.170               (-0.2896, 0.05101)
           events_Independence Day     0.0393   0.1296     0.3033     0.762                (-0.2148, 0.2934)
         events_Independence Day-1   -0.01773   0.1295    -0.1369     0.891                (-0.2717, 0.2362)
         events_Independence Day-2   -0.07645   0.1292    -0.5919     0.554                (-0.3297, 0.1768)
         events_Independence Day+1     -0.038   0.1295    -0.2935     0.769                (-0.2919, 0.2159)
         events_Independence Day+2   -0.03187   0.1291    -0.2469     0.805                 (-0.285, 0.2213)
                  events_Labor Day    -0.4191   0.1272     -3.295  9.95e-04       ***     (-0.6685, -0.1697)
                events_Labor Day-1     -0.181   0.1272     -1.423     0.155               (-0.4304, 0.06839)
                events_Labor Day-2   -0.07273    0.127    -0.5726     0.567                (-0.3218, 0.1763)
                events_Labor Day+1    -0.2792   0.1271     -2.196     0.028         *    (-0.5284, -0.02994)
                events_Labor Day+2    -0.2351   0.1267     -1.856     0.064         .      (-0.4835, 0.0133)
               events_Memorial Day    -0.4697   0.1796     -2.615     0.009        **      (-0.822, -0.1175)
             events_Memorial Day-1     -0.299   0.1797     -1.664     0.096         .     (-0.6514, 0.05341)
             events_Memorial Day-2    -0.1466   0.1793    -0.8176     0.414                 (-0.4982, 0.205)
             events_Memorial Day+1    -0.1655   0.1798    -0.9206     0.357                 (-0.5181, 0.187)
             events_Memorial Day+2     0.1411   0.1797     0.7857     0.432                (-0.2111, 0.4934)
              events_New Years Day    -0.2642   0.1815     -1.456     0.146               (-0.6201, 0.09166)
            events_New Years Day-1   -0.03417   0.1838    -0.1859     0.853                (-0.3946, 0.3263)
            events_New Years Day-2     0.1582   0.1832     0.8638     0.388                 (-0.201, 0.5175)
            events_New Years Day+1     0.1232   0.1799      0.685     0.493                (-0.2295, 0.4759)
            events_New Years Day+2     0.2676   0.1765      1.516     0.130               (-0.07848, 0.6137)
                      events_Other     0.0338  0.03137      1.077     0.281              (-0.02771, 0.09531)
                    events_Other-1     0.0111  0.03107     0.3574     0.721              (-0.04981, 0.07202)
                    events_Other-2    0.03176  0.03068      1.035     0.301              (-0.02839, 0.09191)
                    events_Other+1    0.02679  0.03144     0.8518     0.394              (-0.03487, 0.08844)
                    events_Other+2    0.01347   0.0311     0.4333     0.665               (-0.0475, 0.07445)
               events_Thanksgiving    -0.3788   0.1792     -2.114     0.035         *    (-0.7301, -0.02746)
             events_Thanksgiving-1    -0.5778   0.1789      -3.23     0.001        **      (-0.9285, -0.227)
             events_Thanksgiving-2    -0.4193   0.1784      -2.35     0.019         *    (-0.7691, -0.06944)
             events_Thanksgiving+1    -0.2698   0.1792     -1.506     0.132               (-0.6211, 0.08156)
             events_Thanksgiving+2    -0.3672   0.1788     -2.054     0.040         *    (-0.7178, -0.01658)
               events_Veterans Day    0.09711   0.1845     0.5264     0.599                (-0.2646, 0.4589)
             events_Veterans Day-1   0.005506   0.1843    0.02988     0.976                (-0.3558, 0.3668)
             events_Veterans Day-2   -0.01296   0.1837   -0.07054     0.944                (-0.3731, 0.3472)
             events_Veterans Day+1    0.08413   0.1842     0.4568     0.648                 (-0.277, 0.4453)
             events_Veterans Day+2   0.009467   0.1832    0.05169     0.959                (-0.3497, 0.3686)
                     str_dow_2-Tue      1.003  0.04409      22.74    <2e-16       ***        (0.9161, 1.089)
                     str_dow_3-Wed     0.9034  0.04263      21.19    <2e-16       ***        (0.8198, 0.987)
                     str_dow_4-Thu     0.8671  0.04139      20.95    <2e-16       ***       (0.7859, 0.9483)
                     str_dow_5-Fri      0.828  0.04165      19.88    <2e-16       ***       (0.7463, 0.9097)
                     str_dow_6-Sat     0.8208  0.04413       18.6    <2e-16       ***       (0.7342, 0.9073)
                     str_dow_7-Sun      1.097   0.0476      23.04    <2e-16       ***          (1.003, 1.19)
                               ct1     0.1566   0.3892     0.4023     0.688                (-0.6065, 0.9196)
                    is_weekend:ct1   -0.01622   0.2944    -0.0551     0.956                (-0.5935, 0.5611)
                 str_dow_2-Tue:ct1     0.3667   0.7287     0.5032     0.615                  (-1.062, 1.795)
                 str_dow_3-Wed:ct1    -0.1647   0.6144    -0.2681     0.789                   (-1.369, 1.04)
                 str_dow_4-Thu:ct1     0.9581    0.581      1.649     0.099         .       (-0.1811, 2.097)
                 str_dow_5-Fri:ct1     0.1686    0.591     0.2853     0.775                 (-0.9903, 1.327)
                 str_dow_6-Sat:ct1     0.4989   0.6581     0.7581     0.448                 (-0.7915, 1.789)
                 str_dow_7-Sun:ct1    -0.5151   0.7317     -0.704     0.481                  (-1.95, 0.9196)
                 cp0_2008_03_31_00    -0.3359   0.6343    -0.5295     0.596                  (-1.58, 0.9079)
      is_weekend:cp0_2008_03_31_00     0.1604   0.4746     0.3379     0.735                 (-0.7702, 1.091)
     str_dow_2-Tue...2008_03_31_00    -0.2944    1.187    -0.2481     0.804                  (-2.622, 2.033)
     str_dow_3-Wed...2008_03_31_00    0.06264      1.0    0.06264     0.950                  (-1.898, 2.024)
     str_dow_4-Thu...2008_03_31_00     -1.008   0.9421      -1.07     0.285                 (-2.855, 0.8396)
     str_dow_5-Fri...2008_03_31_00    -0.2437   0.9556     -0.255     0.799                   (-2.117, 1.63)
     str_dow_6-Sat...2008_03_31_00    -0.4173    1.061    -0.3932     0.694                  (-2.499, 1.664)
     str_dow_7-Sun...2008_03_31_00     0.5777    1.179     0.4899     0.624                   (-1.735, 2.89)
                 cp1_2008_07_21_00     -1.587    0.568     -2.793     0.005        **      (-2.701, -0.4728)
      is_weekend:cp1_2008_07_21_00    -0.5207   0.4148     -1.255     0.209                 (-1.334, 0.2927)
     str_dow_2-Tue...2008_07_21_00    -0.2748    1.054    -0.2608     0.794                  (-2.341, 1.792)
     str_dow_3-Wed...2008_07_21_00    -0.2432   0.8867    -0.2743     0.784                  (-1.982, 1.495)
     str_dow_4-Thu...2008_07_21_00    -0.7263   0.8317    -0.8733     0.383                 (-2.357, 0.9044)
     str_dow_5-Fri...2008_07_21_00   -0.09643   0.8391    -0.1149     0.909                  (-1.742, 1.549)
     str_dow_6-Sat...2008_07_21_00    -0.8503   0.9288    -0.9155     0.360                 (-2.671, 0.9709)
     str_dow_7-Sun...2008_07_21_00     0.3297    1.031     0.3196     0.749                  (-1.693, 2.352)
                 cp2_2008_11_10_00      2.573   0.5389      4.774  1.90e-06       ***         (1.516, 3.629)
      is_weekend:cp2_2008_11_10_00     0.5256   0.3954      1.329     0.184                 (-0.2496, 1.301)
     str_dow_2-Tue...2008_11_10_00     0.2169     1.01     0.2148     0.830                  (-1.763, 2.197)
     str_dow_3-Wed...2008_11_10_00     0.5601   0.8479     0.6605     0.509                  (-1.103, 2.223)
     str_dow_4-Thu...2008_11_10_00      1.308   0.7943      1.646     0.100         .         (-0.25, 2.865)
     str_dow_5-Fri...2008_11_10_00     0.3597   0.7997     0.4498     0.653                  (-1.208, 1.928)
     str_dow_6-Sat...2008_11_10_00       1.18   0.8855      1.332     0.183                 (-0.5568, 2.916)
     str_dow_7-Sun...2008_11_10_00    -0.6539   0.9847    -0.6641     0.507                  (-2.585, 1.277)
                 cp3_2009_03_09_00     0.6519   0.5423      1.202     0.229                 (-0.4114, 1.715)
      is_weekend:cp3_2009_03_09_00    0.08017   0.3941     0.2034     0.839                 (-0.6927, 0.853)
     str_dow_2-Tue...2009_03_09_00     0.2698    1.005     0.2685     0.788                     (-1.7, 2.24)
     str_dow_3-Wed...2009_03_09_00     0.1218   0.8426     0.1445     0.885                   (-1.53, 1.774)
     str_dow_4-Thu...2009_03_09_00    -0.2915   0.7893    -0.3693     0.712                  (-1.839, 1.256)
     str_dow_5-Fri...2009_03_09_00    0.01462   0.7962    0.01837     0.985                  (-1.547, 1.576)
     str_dow_6-Sat...2009_03_09_00    -0.1394   0.8824     -0.158     0.874                   (-1.87, 1.591)
     str_dow_7-Sun...2009_03_09_00     0.2196   0.9814     0.2237     0.823                  (-1.705, 2.144)
                 cp4_2009_06_29_00     -1.338   0.5573       -2.4     0.016         *       (-2.43, -0.2449)
      is_weekend:cp4_2009_06_29_00    -0.1873   0.4069    -0.4603     0.645                (-0.9852, 0.6106)
     str_dow_2-Tue...2009_06_29_00    -0.4879    1.037    -0.4704     0.638                  (-2.522, 1.546)
     str_dow_3-Wed...2009_06_29_00    -0.4097   0.8689    -0.4716     0.637                  (-2.114, 1.294)
     str_dow_4-Thu...2009_06_29_00    -0.7721   0.8148    -0.9475     0.343                  (-2.37, 0.8256)
     str_dow_5-Fri...2009_06_29_00    -0.3734   0.8231    -0.4536     0.650                  (-1.987, 1.241)
     str_dow_6-Sat...2009_06_29_00    -0.4628   0.9122    -0.5073     0.612                  (-2.251, 1.326)
     str_dow_7-Sun...2009_06_29_00     0.2755    1.014     0.2716     0.786                  (-1.713, 2.264)
                 cp5_2009_10_19_00     0.6892   0.5376      1.282     0.200                 (-0.3649, 1.743)
      is_weekend:cp5_2009_10_19_00     0.2402   0.3938     0.6099     0.542                 (-0.5319, 1.012)
     str_dow_2-Tue...2009_10_19_00     0.2131    1.005     0.2119     0.832                  (-1.758, 2.184)
     str_dow_3-Wed...2009_10_19_00      0.318   0.8419     0.3777     0.706                  (-1.333, 1.969)
     str_dow_4-Thu...2009_10_19_00     0.7512   0.7887     0.9524     0.341                 (-0.7954, 2.298)
     str_dow_5-Fri...2009_10_19_00     0.4888   0.7974      0.613     0.540                  (-1.075, 2.052)
     str_dow_6-Sat...2009_10_19_00     0.3932   0.8831     0.4453     0.656                  (-1.338, 2.125)
     str_dow_7-Sun...2009_10_19_00    -0.1531   0.9815     -0.156     0.876                  (-2.078, 1.771)
                 cp6_2010_02_15_00     -2.515   0.5437     -4.625  3.92e-06       ***       (-3.581, -1.449)
      is_weekend:cp6_2010_02_15_00    -0.7505   0.3942     -1.904     0.057         .      (-1.523, 0.02236)
     str_dow_2-Tue...2010_02_15_00       0.31    1.005     0.3085     0.758                    (-1.66, 2.28)
     str_dow_3-Wed...2010_02_15_00    -0.7729   0.8404    -0.9197     0.358                 (-2.421, 0.8749)
     str_dow_4-Thu...2010_02_15_00     0.2337   0.7869      0.297     0.766                  (-1.309, 1.777)
     str_dow_5-Fri...2010_02_15_00    -0.5174   0.7975    -0.6488     0.517                  (-2.081, 1.046)
     str_dow_6-Sat...2010_02_15_00    -0.2437   0.8842    -0.2756     0.783                   (-1.978, 1.49)
     str_dow_7-Sun...2010_02_15_00    -0.5068   0.9826    -0.5158     0.606                   (-2.434, 1.42)
                 cp7_2010_06_07_00      3.488   0.5579      6.253  4.66e-10       ***         (2.394, 4.582)
      is_weekend:cp7_2010_06_07_00     0.9022   0.4055      2.225     0.026         *        (0.1071, 1.697)
     str_dow_2-Tue...2010_06_07_00    -0.2454    1.033    -0.2375     0.812                  (-2.272, 1.781)
     str_dow_3-Wed...2010_06_07_00     0.7733   0.8655     0.8935     0.372                  (-0.9238, 2.47)
     str_dow_4-Thu...2010_06_07_00    -0.9702   0.8096     -1.198     0.231                 (-2.558, 0.6174)
     str_dow_5-Fri...2010_06_07_00     0.2812    0.819     0.3434     0.731                  (-1.325, 1.887)
     str_dow_6-Sat...2010_06_07_00    -0.1674   0.9087    -0.1843     0.854                  (-1.949, 1.614)
     str_dow_7-Sun...2010_06_07_00       1.07     1.01      1.059     0.289                   (-0.91, 3.049)
                 cp8_2010_09_27_00     -2.989   0.5291     -5.648  1.79e-08       ***       (-4.026, -1.951)
      is_weekend:cp8_2010_09_27_00    -0.7411   0.3754     -1.974     0.048         *    (-1.477, -0.004907)
     str_dow_2-Tue...2010_09_27_00    -0.5368   0.9551     -0.562     0.574                   (-2.41, 1.336)
     str_dow_3-Wed...2010_09_27_00    -0.1625   0.8017    -0.2027     0.839                  (-1.734, 1.409)
     str_dow_4-Thu...2010_09_27_00     0.6075   0.7494     0.8107     0.418                  (-0.862, 2.077)
     str_dow_5-Fri...2010_09_27_00    -0.1857   0.7563    -0.2455     0.806                  (-1.669, 1.297)
     str_dow_6-Sat...2010_09_27_00     0.3321   0.8382     0.3962     0.692                  (-1.311, 1.976)
     str_dow_7-Sun...2010_09_27_00     -1.073    0.931     -1.153     0.249                 (-2.899, 0.7523)
                 cp9_2011_01_24_00      1.765   0.3794      4.653  3.43e-06       ***         (1.021, 2.509)
      is_weekend:cp9_2011_01_24_00      0.508   0.2601      1.953     0.051         .      (-0.00197, 1.018)
     str_dow_2-Tue...2011_01_24_00     0.6831   0.6601      1.035     0.301                 (-0.6112, 1.977)
     str_dow_3-Wed...2011_01_24_00    -0.1427   0.5539    -0.2576     0.797                 (-1.229, 0.9435)
     str_dow_4-Thu...2011_01_24_00    0.06832    0.518     0.1319     0.895                 (-0.9474, 1.084)
     str_dow_5-Fri...2011_01_24_00     0.1457    0.523     0.2787     0.781                 (-0.8797, 1.171)
     str_dow_6-Sat...2011_01_24_00  -0.003916   0.5797  -0.006756     0.995                  (-1.141, 1.133)
     str_dow_7-Sun...2011_01_24_00     0.5119   0.6438     0.7952     0.427                 (-0.7504, 1.774)
                cp10_2011_09_05_00    0.06695   0.3807     0.1758     0.860                (-0.6796, 0.8134)
     is_weekend:cp10_2011_09_05_00    -0.4058    0.259     -1.567     0.117                (-0.9137, 0.1021)
     str_dow_2-Tue...2011_09_05_00    -0.4998   0.6567     -0.761     0.447                  (-1.787, 0.788)
     str_dow_3-Wed...2011_09_05_00     0.5105   0.5505     0.9273     0.354                  (-0.5689, 1.59)
     str_dow_4-Thu...2011_09_05_00    -0.3479   0.5133    -0.6778     0.498                 (-1.354, 0.6586)
     str_dow_5-Fri...2011_09_05_00     -0.264   0.5189    -0.5088     0.611                 (-1.282, 0.7535)
     str_dow_6-Sat...2011_09_05_00    -0.2696   0.5765    -0.4676     0.640                   (-1.4, 0.8608)
     str_dow_7-Sun...2011_09_05_00    -0.1362   0.6407    -0.2126     0.832                   (-1.393, 1.12)
                cp11_2012_01_02_00     0.2574   0.4944     0.5207     0.603                  (-0.712, 1.227)
     is_weekend:cp11_2012_01_02_00     0.5849   0.3457      1.692     0.091         .      (-0.09292, 1.263)
     str_dow_2-Tue...2012_01_02_00     0.5218    0.878     0.5943     0.552                    (-1.2, 2.243)
     str_dow_3-Wed...2012_01_02_00    -0.4144   0.7342    -0.5644     0.573                  (-1.854, 1.025)
     str_dow_4-Thu...2012_01_02_00     0.4073   0.6852     0.5945     0.552                 (-0.9362, 1.751)
     str_dow_5-Fri...2012_01_02_00     0.8381    0.694      1.208     0.227                 (-0.5228, 2.199)
     str_dow_6-Sat...2012_01_02_00     0.4047   0.7708     0.5251     0.600                  (-1.107, 1.916)
     str_dow_7-Sun...2012_01_02_00     0.1802   0.8568     0.2103     0.833                     (-1.5, 1.86)
                cp12_2012_04_23_00     -1.735   0.3025     -5.736  1.07e-08       ***       (-2.328, -1.142)
     is_weekend:cp12_2012_04_23_00    -0.5217   0.2197     -2.375     0.018         *    (-0.9524, -0.09092)
     str_dow_2-Tue...2012_04_23_00    -0.3187   0.5599    -0.5692     0.569                 (-1.417, 0.7792)
     str_dow_3-Wed...2012_04_23_00    -0.2259   0.4685    -0.4821     0.630                 (-1.145, 0.6928)
     str_dow_4-Thu...2012_04_23_00    -0.3114   0.4383    -0.7105     0.477                  (-1.171, 0.548)
     str_dow_5-Fri...2012_04_23_00    -0.7798   0.4432     -1.759     0.079         .      (-1.649, 0.08923)
     str_dow_6-Sat...2012_04_23_00    -0.3741   0.4909    -0.7621     0.446                 (-1.337, 0.5885)
     str_dow_7-Sun...2012_04_23_00    -0.1475   0.5459    -0.2702     0.787                  (-1.218, 0.923)
                cp13_2013_04_01_00      1.433   0.1341      10.69    <2e-16       ***          (1.17, 1.696)
     is_weekend:cp13_2013_04_01_00     0.1539   0.1028      1.497     0.134               (-0.04762, 0.3554)
     str_dow_2-Tue...2013_04_01_00    0.01899   0.2634    0.07207     0.943                (-0.4975, 0.5355)
     str_dow_3-Wed...2013_04_01_00     0.3881   0.2206      1.759     0.079         .     (-0.04449, 0.8206)
     str_dow_4-Thu...2013_04_01_00     0.1302   0.2067     0.6302     0.529                 (-0.275, 0.5355)
     str_dow_5-Fri...2013_04_01_00     0.2075   0.2084     0.9955     0.320                (-0.2011, 0.6161)
     str_dow_6-Sat...2013_04_01_00     0.2493   0.2306      1.081     0.280                (-0.2028, 0.7014)
     str_dow_7-Sun...2013_04_01_00    -0.0954   0.2567    -0.3716     0.710                 (-0.5988, 0.408)
                cp14_2013_11_11_00    -0.9378  0.09501      -9.87    <2e-16       ***      (-1.124, -0.7515)
     is_weekend:cp14_2013_11_11_00    -0.1002  0.07316      -1.37     0.171               (-0.2437, 0.04324)
     str_dow_2-Tue...2013_11_11_00    0.06435   0.1872     0.3438     0.731                (-0.3027, 0.4314)
     str_dow_3-Wed...2013_11_11_00    -0.2741   0.1567     -1.749     0.080         .     (-0.5814, 0.03319)
     str_dow_4-Thu...2013_11_11_00   -0.07223    0.147    -0.4914     0.623                 (-0.3605, 0.216)
     str_dow_5-Fri...2013_11_11_00    -0.0736   0.1483    -0.4964     0.620                (-0.3643, 0.2171)
     str_dow_6-Sat...2013_11_11_00    -0.2099   0.1641     -1.279     0.201                (-0.5317, 0.1119)
     str_dow_7-Sun...2013_11_11_00     0.1097   0.1827     0.6004     0.548                (-0.2485, 0.4679)
               ct1:sin1_tow_weekly      0.385   0.3817      1.009     0.313                 (-0.3635, 1.133)
               ct1:cos1_tow_weekly     -2.338   0.5154     -4.536  5.99e-06       ***       (-3.349, -1.327)
               ct1:sin2_tow_weekly     0.5304   0.4246      1.249     0.212                 (-0.3021, 1.363)
               ct1:cos2_tow_weekly    -0.7214   0.4715      -1.53     0.126                 (-1.646, 0.2031)
     cp0_2008_03_3...n1_tow_weekly    -0.5454   0.6184     -0.882     0.378                 (-1.758, 0.6671)
     cp0_2008_03_3...s1_tow_weekly       2.37   0.8403      2.821     0.005        **        (0.7224, 4.018)
     cp0_2008_03_3...n2_tow_weekly    -0.4612    0.686    -0.6723     0.501                 (-1.806, 0.8839)
     cp0_2008_03_3...s2_tow_weekly     0.4633   0.7687     0.6026     0.547                  (-1.044, 1.971)
     cp1_2008_07_2...n1_tow_weekly     -0.154   0.5437    -0.2833     0.777                  (-1.22, 0.9121)
     cp1_2008_07_2...s1_tow_weekly      1.294    0.746      1.734     0.083         .       (-0.1692, 2.756)
     cp1_2008_07_2...n2_tow_weekly    -0.3602   0.6022    -0.5981     0.550                 (-1.541, 0.8207)
     cp1_2008_07_2...s2_tow_weekly     0.7349   0.6833      1.075     0.282                  (-0.605, 2.075)
     cp2_2008_11_1...n1_tow_weekly     0.4882   0.5185     0.9414     0.347                 (-0.5286, 1.505)
     cp2_2008_11_1...s1_tow_weekly     -2.559   0.7129      -3.59  3.37e-04       ***       (-3.957, -1.161)
     cp2_2008_11_1...n2_tow_weekly     0.3767   0.5745     0.6557     0.512                 (-0.7498, 1.503)
     cp2_2008_11_1...s2_tow_weekly    -0.8277   0.6535     -1.267     0.205                 (-2.109, 0.4537)
     cp3_2009_03_0...n1_tow_weekly     0.1611   0.5154     0.3126     0.755                 (-0.8495, 1.172)
     cp3_2009_03_0...s1_tow_weekly      1.016   0.7098      1.431     0.153                 (-0.3762, 2.407)
     cp3_2009_03_0...n2_tow_weekly      0.175   0.5705     0.3068     0.759                 (-0.9437, 1.294)
     cp3_2009_03_0...s2_tow_weekly     0.1913   0.6506     0.2941     0.769                  (-1.084, 1.467)
     cp4_2009_06_2...n1_tow_weekly    -0.7181    0.532      -1.35     0.177                  (-1.761, 0.325)
     cp4_2009_06_2...s1_tow_weekly      1.987   0.7334      2.709     0.007        **        (0.5485, 3.424)
     cp4_2009_06_2...n2_tow_weekly    -0.4556   0.5887    -0.7738     0.439                  (-1.61, 0.6988)
     cp4_2009_06_2...s2_tow_weekly      1.012   0.6716      1.507     0.132                 (-0.3049, 2.329)
     cp5_2009_10_1...n1_tow_weekly     0.3268   0.5154      0.634     0.526                 (-0.6838, 1.337)
     cp5_2009_10_1...s1_tow_weekly      -2.56   0.7099     -3.606  3.16e-04       ***       (-3.952, -1.168)
     cp5_2009_10_1...n2_tow_weekly     0.1845   0.5704     0.3234     0.746                  (-0.934, 1.303)
     cp5_2009_10_1...s2_tow_weekly     -1.203   0.6504      -1.85     0.064         .      (-2.478, 0.07233)
     cp6_2010_02_1...n1_tow_weekly     0.4486   0.5157       0.87     0.384                  (-0.5625, 1.46)
     cp6_2010_02_1...s1_tow_weekly    -0.6583   0.7101     -0.927     0.354                 (-2.051, 0.7341)
     cp6_2010_02_1...n2_tow_weekly     0.4386   0.5707     0.7685     0.442                 (-0.6804, 1.558)
     cp6_2010_02_1...s2_tow_weekly    -0.2346   0.6503    -0.3607     0.718                    (-1.51, 1.04)
     cp7_2010_06_0...n1_tow_weekly     -0.654   0.5314     -1.231     0.219                  (-1.696, 0.388)
     cp7_2010_06_0...s1_tow_weekly      3.747   0.7308      5.127  3.15e-07       ***          (2.314, 5.18)
     cp7_2010_06_0...n2_tow_weekly    -0.7118   0.5878     -1.211     0.226                 (-1.864, 0.4407)
     cp7_2010_06_0...s2_tow_weekly      1.588   0.6698      2.371     0.018         *        (0.2748, 2.902)
     cp8_2010_09_2...n1_tow_weekly     0.2813   0.4914     0.5724     0.567                 (-0.6823, 1.245)
     cp8_2010_09_2...s1_tow_weekly     -3.392   0.6753     -5.023  5.42e-07       ***       (-4.716, -2.068)
     cp8_2010_09_2...n2_tow_weekly     0.1174   0.5437     0.2159     0.829                 (-0.9488, 1.184)
     cp8_2010_09_2...s2_tow_weekly     -1.502   0.6199     -2.422     0.015         *      (-2.717, -0.2861)
     cp9_2011_01_2...n1_tow_weekly   -0.03507   0.3397    -0.1032     0.918                (-0.7012, 0.6311)
     cp9_2011_01_2...s1_tow_weekly      1.088    0.467      2.329     0.020         *         (0.172, 2.003)
     cp9_2011_01_2...n2_tow_weekly     0.2876   0.3756     0.7658     0.444                 (-0.4488, 1.024)
     cp9_2011_01_2...s2_tow_weekly     0.5025   0.4286      1.172     0.241                 (-0.3379, 1.343)
     cp10_2011_09_...n1_tow_weekly     0.4399   0.3388      1.298     0.194                 (-0.2245, 1.104)
     cp10_2011_09_...s1_tow_weekly      1.175   0.4659      2.523     0.012         *        (0.2618, 2.089)
     cp10_2011_09_...n2_tow_weekly    -0.6273   0.3744     -1.675     0.094         .       (-1.361, 0.1069)
     cp10_2011_09_...s2_tow_weekly     0.6169   0.4274      1.444     0.149                 (-0.2211, 1.455)
     cp11_2012_01_...n1_tow_weekly    -0.7184   0.4531     -1.585     0.113                 (-1.607, 0.1701)
     cp11_2012_01_...s1_tow_weekly     -2.363   0.6226     -3.794  1.51e-04       ***       (-3.583, -1.142)
     cp11_2012_01_...n2_tow_weekly      1.025   0.4994      2.053     0.040         *       (0.04598, 2.005)
     cp11_2012_01_...s2_tow_weekly     -1.051   0.5693     -1.847     0.065         .      (-2.168, 0.06492)
     cp12_2012_04_...n1_tow_weekly      0.214   0.2883     0.7423     0.458                (-0.3513, 0.7793)
     cp12_2012_04_...s1_tow_weekly      1.249   0.3966      3.148     0.002        **        (0.4708, 2.026)
     cp12_2012_04_...n2_tow_weekly    -0.5974   0.3177      -1.88     0.060         .       (-1.22, 0.02556)
     cp12_2012_04_...s2_tow_weekly     0.3864   0.3622      1.067     0.286                 (-0.3238, 1.097)
     cp13_2013_04_...n1_tow_weekly     0.1912   0.1346      1.421     0.155               (-0.07267, 0.4551)
     cp13_2013_04_...s1_tow_weekly    0.04089   0.1856     0.2203     0.826                 (-0.323, 0.4048)
     cp13_2013_04_...n2_tow_weekly     0.1117   0.1494     0.7473     0.455                (-0.1813, 0.4047)
     cp13_2013_04_...s2_tow_weekly     0.1879   0.1703      1.103     0.270                 (-0.146, 0.5219)
     cp14_2013_11_...n1_tow_weekly   -0.09745   0.0958     -1.017     0.309                (-0.2853, 0.0904)
     cp14_2013_11_...s1_tow_weekly    -0.1344   0.1321     -1.017     0.309                (-0.3935, 0.1247)
     cp14_2013_11_...n2_tow_weekly   -0.01741   0.1069    -0.1628     0.871                (-0.2271, 0.1923)
     cp14_2013_11_...s2_tow_weekly    -0.1756   0.1217     -1.442     0.149               (-0.4142, 0.06314)
                   sin1_tow_weekly    0.02394  0.09165     0.2612     0.794                (-0.1558, 0.2037)
                   cos1_tow_weekly     0.9462  0.09745      9.709    <2e-16       ***        (0.7551, 1.137)
                   sin2_tow_weekly    -0.1581  0.09161     -1.726     0.085         .     (-0.3377, 0.02153)
                   cos2_tow_weekly     0.5847  0.09709      6.023  1.94e-09       ***       (0.3944, 0.7751)
                   sin3_tow_weekly   -0.06729   0.0512     -1.314     0.189                (-0.1677, 0.0331)
                   cos3_tow_weekly     0.3549  0.09744      3.642  2.75e-04       ***        (0.1638, 0.546)
                   sin4_tow_weekly    0.06729   0.0512      1.314     0.189                (-0.0331, 0.1677)
                sin4_toq_quarterly  -0.001162  0.01278   -0.09087     0.928               (-0.02623, 0.0239)
                cos4_toq_quarterly    -0.0395  0.01317     -2.999     0.003        **   (-0.06533, -0.01367)
                sin5_toq_quarterly   -0.03851  0.01307     -2.946     0.003        **   (-0.06413, -0.01288)
                cos5_toq_quarterly    0.01821  0.01299      1.401     0.161             (-0.007267, 0.04368)
                   sin1_ct1_yearly     -0.102  0.01781     -5.727  1.13e-08       ***    (-0.1369, -0.06706)
                   cos1_ct1_yearly     0.7463  0.01784      41.84    <2e-16       ***       (0.7113, 0.7813)
                   sin2_ct1_yearly    0.06028  0.01403      4.297  1.79e-05       ***     (0.03277, 0.08778)
                   cos2_ct1_yearly   -0.09214  0.01373     -6.712  2.31e-11       ***    (-0.1191, -0.06523)
                   sin3_ct1_yearly     0.2559  0.01398      18.31    <2e-16       ***       (0.2285, 0.2833)
                   cos3_ct1_yearly    -0.0482  0.01324     -3.641  2.76e-04       ***   (-0.07416, -0.02225)
                   sin4_ct1_yearly   0.001313  0.01375    0.09547     0.924              (-0.02565, 0.02828)
                   cos4_ct1_yearly    -0.1092  0.01255     -8.706    <2e-16       ***    (-0.1338, -0.08464)
                   sin5_ct1_yearly    -0.1003  0.01381     -7.259  5.06e-13       ***    (-0.1273, -0.07317)
                   cos5_ct1_yearly   -0.01609  0.01257      -1.28     0.201             (-0.04075, 0.008563)
                   sin6_ct1_yearly    -0.1229  0.01373     -8.955    <2e-16       ***      (-0.1498, -0.096)
                   cos6_ct1_yearly   -0.02659  0.01305     -2.038     0.042         *  (-0.05218, -0.001007)
                   sin7_ct1_yearly   -0.05338  0.01342     -3.976  7.18e-05       ***    (-0.0797, -0.02706)
                   cos7_ct1_yearly    0.04467  0.01292      3.458  5.53e-04       ***        (0.01934, 0.07)
                   sin8_ct1_yearly    0.03468  0.01306      2.655     0.008        **    (0.009068, 0.06029)
                   cos8_ct1_yearly     0.1085  0.01367      7.938  2.96e-15       ***       (0.0817, 0.1353)
                   sin9_ct1_yearly   0.004104  0.01309     0.3134     0.754              (-0.02157, 0.02978)
                   cos9_ct1_yearly    -0.0303  0.01382     -2.193     0.028         *   (-0.0574, -0.003206)
                  sin10_ct1_yearly   -0.07522  0.01313     -5.729  1.12e-08       ***     (-0.101, -0.04948)
                  cos10_ct1_yearly   -0.06762  0.01315     -5.144  2.87e-07       ***    (-0.0934, -0.04185)
                  sin11_ct1_yearly   -0.01983  0.01295     -1.531     0.126             (-0.04522, 0.005569)
                  cos11_ct1_yearly   -0.01528  0.01333     -1.146     0.252              (-0.04142, 0.01087)
                  sin12_ct1_yearly   -0.01809  0.01329     -1.362     0.173             (-0.04415, 0.007957)
                  cos12_ct1_yearly    0.01126  0.01332      0.845     0.398              (-0.01487, 0.03738)
                  sin13_ct1_yearly  -0.008644  0.01274    -0.6785     0.498              (-0.03363, 0.01634)
                  cos13_ct1_yearly    0.04896  0.01356       3.61  3.11e-04       ***     (0.02237, 0.07555)
                  sin14_ct1_yearly    0.03825  0.01302      2.938     0.003        **     (0.01272, 0.06378)
                  cos14_ct1_yearly   -0.01737  0.01346      -1.29     0.197             (-0.04377, 0.009034)
                  sin15_ct1_yearly    0.02524  0.01326      1.903     0.057         .  (-0.0007695, 0.05125)
                  cos15_ct1_yearly   -0.03081  0.01321     -2.333     0.020         *  (-0.05671, -0.004918)
    Signif. Code: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Multiple R-squared: 0.7214,   Adjusted R-squared: 0.7007
    F-statistic: 34.842 on 204 and 2758 DF,   p-value: 1.110e-16
    Model AIC: 19345.0,   model BIC: 20580.0

    WARNING: the condition number is large, 6.67e+19. This might indicate that there are strong multicollinearity or other numerical problems.





The model summary provides useful insights:

  #. We can check the ``sig. code`` column to see which features are not significant.
     For example, the "Independence Day" events are not significant,
     therefore we could consider removing them from the model.
  #. We can check the effect of each feature by examing the confidence interval.
     For example, the Christmas day has a negative effect of -0.57, with a confidence interval
     of -0.93 to -0.22. The changepoint at 2010-02-15 changes the slope by -2.52, with a
     confidence interval of -3.60 to -1.44.

For linear regression, the results are the
same as the regular regression summary in R (the ``lm`` function).
The usual considerations apply when interpreting the results:

  #. High feature correlation can increase the coefficient variance.
     This is common in forecasting problems, so we recommend regularized models.
  #. There is no standard way to calculate confidence intervals and p-values for regularized
     linear models (ridge, lasso, elastic_net). We follow the approach in [1]_ for ridge
     inference and [2]_ for lasso inference.
     The ideas are to use bootstrap and sample-splitting, respectively.

          - For ridge regression, the confidence intervals and p-values are based on biased estimators.
            This is a remedy for multicollinearity to produce better forecast, but could lower the true
            effect of the features.
          - For lasso regression, the confidence intervals and p-values are based on a multi-sample-split
            procedure. While this approach of generating CIs is optimized for accuracy, they are calculated
            independently of the coefficient estimates and are not guaranteed to overlap with the estimates.
            It's worth noting that the probability of a coefficient being nonzero is also reported in the column ``Prob_nonzero``.
            This probability can be used to interpret the significance of the corresponding feature.

Moreover, if you would like to explore the numbers behind the printed summary,
they are stored in the ``info_dict`` attribute, which is a python dictionary.


.. code-block:: default
   :lineno-start: 150


    # Prints the keys of the ``info_dict`` dictionary.
    print(summary.info_dict.keys())





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    dict_keys(['x', 'y', 'beta', 'ml_model', 'fit_algorithm', 'pred_cols', 'degenerate_index', 'n_sample', 'n_feature', 'nonzero_index', 'n_feature_nonzero', 'y_pred', 'y_mean', 'residual', 'residual_summary', 'model', 'x_nz', 'condition_number', 'xtwx_alphai_inv', 'reg_df', 'df_sse', 'df_ssr', 'df_sst', 'sse', 'mse', 'ssr', 'msr', 'sst', 'mst', 'beta_var_cov', 'coef_summary_df', 'significance_code_legend', 'f_value', 'f_p_value', 'r2', 'r2_adj', 'aic', 'bic', 'model_type'])





.. code-block:: default
   :lineno-start: 155


    # The above coefficient summary can be accessed as a pandas Dataframe.
    print(summary.info_dict["coef_summary_df"])





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

                                                  Pred_col  Estimate  Std. Err    t value  Pr(>|t|) sig. code                                          95%CI
    0                                            Intercept  7.066716  0.078162  90.411129  0.000000       ***         (6.913454196757804, 7.219978191921828)
    1    C(Q('events_Chinese New Year'), levels=['', 'e... -0.002513  0.170665  -0.014722  0.988255                (-0.3371574209627301, 0.3321323067978256)
    2    C(Q('events_Chinese New Year_minus_1'), levels... -0.064868  0.170653  -0.380115  0.703889              (-0.39948839550616466, 0.26975282588438454)
    3    C(Q('events_Chinese New Year_minus_2'), levels...  0.033292  0.170665   0.195074  0.845349               (-0.3013524330596132, 0.36793714729596655)
    4    C(Q('events_Chinese New Year_plus_1'), levels=... -0.088987  0.170647  -0.521472  0.602080              (-0.42359547098653927, 0.24562065581666648)
    ..                                                 ...       ...       ...        ...       ...       ...                                            ...
    290                                   cos13_ct1_yearly  0.048958  0.013560   3.610450  0.000311       ***    (0.022368884607778947, 0.07554634712984043)
    291                                   sin14_ct1_yearly  0.038250  0.013019   2.938047  0.003330        **    (0.012722400853566771, 0.06377809911060893)
    292                                   cos14_ct1_yearly -0.017366  0.013464  -1.289833  0.197217               (-0.0437654171340634, 0.00903393413745155)
    293                                   sin15_ct1_yearly  0.025241  0.013265   1.902816  0.057169         .  (-0.0007694799739524326, 0.05125069221599819)
    294                                   cos15_ct1_yearly -0.030814  0.013207  -2.333183  0.019710         *   (-0.0567104100639305, -0.004917697037745732)

    [295 rows x 7 columns]




Selected features in a category
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You may have noticed that there are too many features in the forecast model.
It's not easy to read all of them in the coefficient summary table.
The model summary class is able to filter the categories of these features.
This is done by the
`~greykite.algo.common.model_summary.ModelSummary.get_coef_summary`
function.

A few filters are available, including:

  - ``is_intercept``: intercept term.
  - ``is_time_feature``: features defined in `~greykite.common.features.timeseries_features.build_time_features_df`.
  - ``is_event``: holidays and events.
  - ``is_trend``: trend features.
  - ``is_seasonality``: seasonality features.
  - ``is_lag``: autoregressive features.
  - ``is_regressor``: extra regressors provided by user.
  - ``is_interaction``: interaction terms.

All filters set to ``True`` will be joined with the logical operator ``or``,
while all filters set to ``False`` will be joined with the logical operator ``and``.
Simply speaking, set what you want to see to ``True`` and what you don't want to see
to ``False``.

By default, ``is_interaction`` is set to ``True``, this means as long as one feature in
an interaction term belongs to a category set to ``True``, the interaction term is included
in the output. However, if one feature in an interaction term belongs to a category set to
``False``, the interaction is excluded from the output.
To hide interaction terms, set ``is_interaction`` to ``False``.


.. code-block:: default
   :lineno-start: 190


    # Displays intercept, trend features but not seasonality features.
    summary.get_coef_summary(
        is_intercept=True,
        is_trend=True,
        is_seasonality=False
    )





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

                Pred_col   Estimate Std. Err    t value  Pr(>|t|) sig. code                95%CI
               Intercept      7.067  0.07816      90.41    <2e-16       ***        (6.913, 7.22)
                     ct1     0.1566   0.3892     0.4023     0.688              (-0.6065, 0.9196)
          is_weekend:ct1   -0.01622   0.2944    -0.0551     0.956              (-0.5935, 0.5611)
       str_dow_2-Tue:ct1     0.3667   0.7287     0.5032     0.615                (-1.062, 1.795)
       str_dow_3-Wed:ct1    -0.1647   0.6144    -0.2681     0.789                 (-1.369, 1.04)
       str_dow_4-Thu:ct1     0.9581    0.581      1.649     0.099         .     (-0.1811, 2.097)
       str_dow_5-Fri:ct1     0.1686    0.591     0.2853     0.775               (-0.9903, 1.327)
       str_dow_6-Sat:ct1     0.4989   0.6581     0.7581     0.448               (-0.7915, 1.789)
       str_dow_7-Sun:ct1    -0.5151   0.7317     -0.704     0.481                (-1.95, 0.9196)
       cp0_2008_03_31_00    -0.3359   0.6343    -0.5295     0.596                (-1.58, 0.9079)
     is_weeke...03_31_00     0.1604   0.4746     0.3379     0.735               (-0.7702, 1.091)
     str_dow_...03_31_00    -0.2944    1.187    -0.2481     0.804                (-2.622, 2.033)
     str_dow_...03_31_00    0.06264      1.0    0.06264     0.950                (-1.898, 2.024)
     str_dow_...03_31_00     -1.008   0.9421      -1.07     0.285               (-2.855, 0.8396)
     str_dow_...03_31_00    -0.2437   0.9556     -0.255     0.799                 (-2.117, 1.63)
     str_dow_...03_31_00    -0.4173    1.061    -0.3932     0.694                (-2.499, 1.664)
     str_dow_...03_31_00     0.5777    1.179     0.4899     0.624                 (-1.735, 2.89)
       cp1_2008_07_21_00     -1.587    0.568     -2.793     0.005        **    (-2.701, -0.4728)
     is_weeke...07_21_00    -0.5207   0.4148     -1.255     0.209               (-1.334, 0.2927)
     str_dow_...07_21_00    -0.2748    1.054    -0.2608     0.794                (-2.341, 1.792)
     str_dow_...07_21_00    -0.2432   0.8867    -0.2743     0.784                (-1.982, 1.495)
     str_dow_...07_21_00    -0.7263   0.8317    -0.8733     0.383               (-2.357, 0.9044)
     str_dow_...07_21_00   -0.09643   0.8391    -0.1149     0.909                (-1.742, 1.549)
     str_dow_...07_21_00    -0.8503   0.9288    -0.9155     0.360               (-2.671, 0.9709)
     str_dow_...07_21_00     0.3297    1.031     0.3196     0.749                (-1.693, 2.352)
       cp2_2008_11_10_00      2.573   0.5389      4.774  1.90e-06       ***       (1.516, 3.629)
     is_weeke...11_10_00     0.5256   0.3954      1.329     0.184               (-0.2496, 1.301)
     str_dow_...11_10_00     0.2169     1.01     0.2148     0.830                (-1.763, 2.197)
     str_dow_...11_10_00     0.5601   0.8479     0.6605     0.509                (-1.103, 2.223)
     str_dow_...11_10_00      1.308   0.7943      1.646     0.100         .       (-0.25, 2.865)
     str_dow_...11_10_00     0.3597   0.7997     0.4498     0.653                (-1.208, 1.928)
     str_dow_...11_10_00       1.18   0.8855      1.332     0.183               (-0.5568, 2.916)
     str_dow_...11_10_00    -0.6539   0.9847    -0.6641     0.507                (-2.585, 1.277)
       cp3_2009_03_09_00     0.6519   0.5423      1.202     0.229               (-0.4114, 1.715)
     is_weeke...03_09_00    0.08017   0.3941     0.2034     0.839               (-0.6927, 0.853)
     str_dow_...03_09_00     0.2698    1.005     0.2685     0.788                   (-1.7, 2.24)
     str_dow_...03_09_00     0.1218   0.8426     0.1445     0.885                 (-1.53, 1.774)
     str_dow_...03_09_00    -0.2915   0.7893    -0.3693     0.712                (-1.839, 1.256)
     str_dow_...03_09_00    0.01462   0.7962    0.01837     0.985                (-1.547, 1.576)
     str_dow_...03_09_00    -0.1394   0.8824     -0.158     0.874                 (-1.87, 1.591)
     str_dow_...03_09_00     0.2196   0.9814     0.2237     0.823                (-1.705, 2.144)
       cp4_2009_06_29_00     -1.338   0.5573       -2.4     0.016         *     (-2.43, -0.2449)
     is_weeke...06_29_00    -0.1873   0.4069    -0.4603     0.645              (-0.9852, 0.6106)
     str_dow_...06_29_00    -0.4879    1.037    -0.4704     0.638                (-2.522, 1.546)
     str_dow_...06_29_00    -0.4097   0.8689    -0.4716     0.637                (-2.114, 1.294)
     str_dow_...06_29_00    -0.7721   0.8148    -0.9475     0.343                (-2.37, 0.8256)
     str_dow_...06_29_00    -0.3734   0.8231    -0.4536     0.650                (-1.987, 1.241)
     str_dow_...06_29_00    -0.4628   0.9122    -0.5073     0.612                (-2.251, 1.326)
     str_dow_...06_29_00     0.2755    1.014     0.2716     0.786                (-1.713, 2.264)
       cp5_2009_10_19_00     0.6892   0.5376      1.282     0.200               (-0.3649, 1.743)
     is_weeke...10_19_00     0.2402   0.3938     0.6099     0.542               (-0.5319, 1.012)
     str_dow_...10_19_00     0.2131    1.005     0.2119     0.832                (-1.758, 2.184)
     str_dow_...10_19_00      0.318   0.8419     0.3777     0.706                (-1.333, 1.969)
     str_dow_...10_19_00     0.7512   0.7887     0.9524     0.341               (-0.7954, 2.298)
     str_dow_...10_19_00     0.4888   0.7974      0.613     0.540                (-1.075, 2.052)
     str_dow_...10_19_00     0.3932   0.8831     0.4453     0.656                (-1.338, 2.125)
     str_dow_...10_19_00    -0.1531   0.9815     -0.156     0.876                (-2.078, 1.771)
       cp6_2010_02_15_00     -2.515   0.5437     -4.625  3.92e-06       ***     (-3.581, -1.449)
     is_weeke...02_15_00    -0.7505   0.3942     -1.904     0.057         .    (-1.523, 0.02236)
     str_dow_...02_15_00       0.31    1.005     0.3085     0.758                  (-1.66, 2.28)
     str_dow_...02_15_00    -0.7729   0.8404    -0.9197     0.358               (-2.421, 0.8749)
     str_dow_...02_15_00     0.2337   0.7869      0.297     0.766                (-1.309, 1.777)
     str_dow_...02_15_00    -0.5174   0.7975    -0.6488     0.517                (-2.081, 1.046)
     str_dow_...02_15_00    -0.2437   0.8842    -0.2756     0.783                 (-1.978, 1.49)
     str_dow_...02_15_00    -0.5068   0.9826    -0.5158     0.606                 (-2.434, 1.42)
       cp7_2010_06_07_00      3.488   0.5579      6.253  4.66e-10       ***       (2.394, 4.582)
     is_weeke...06_07_00     0.9022   0.4055      2.225     0.026         *      (0.1071, 1.697)
     str_dow_...06_07_00    -0.2454    1.033    -0.2375     0.812                (-2.272, 1.781)
     str_dow_...06_07_00     0.7733   0.8655     0.8935     0.372                (-0.9238, 2.47)
     str_dow_...06_07_00    -0.9702   0.8096     -1.198     0.231               (-2.558, 0.6174)
     str_dow_...06_07_00     0.2812    0.819     0.3434     0.731                (-1.325, 1.887)
     str_dow_...06_07_00    -0.1674   0.9087    -0.1843     0.854                (-1.949, 1.614)
     str_dow_...06_07_00       1.07     1.01      1.059     0.289                 (-0.91, 3.049)
       cp8_2010_09_27_00     -2.989   0.5291     -5.648  1.79e-08       ***     (-4.026, -1.951)
     is_weeke...09_27_00    -0.7411   0.3754     -1.974     0.048         *  (-1.477, -0.004907)
     str_dow_...09_27_00    -0.5368   0.9551     -0.562     0.574                 (-2.41, 1.336)
     str_dow_...09_27_00    -0.1625   0.8017    -0.2027     0.839                (-1.734, 1.409)
     str_dow_...09_27_00     0.6075   0.7494     0.8107     0.418                (-0.862, 2.077)
     str_dow_...09_27_00    -0.1857   0.7563    -0.2455     0.806                (-1.669, 1.297)
     str_dow_...09_27_00     0.3321   0.8382     0.3962     0.692                (-1.311, 1.976)
     str_dow_...09_27_00     -1.073    0.931     -1.153     0.249               (-2.899, 0.7523)
       cp9_2011_01_24_00      1.765   0.3794      4.653  3.43e-06       ***       (1.021, 2.509)
     is_weeke...01_24_00      0.508   0.2601      1.953     0.051         .    (-0.00197, 1.018)
     str_dow_...01_24_00     0.6831   0.6601      1.035     0.301               (-0.6112, 1.977)
     str_dow_...01_24_00    -0.1427   0.5539    -0.2576     0.797               (-1.229, 0.9435)
     str_dow_...01_24_00    0.06832    0.518     0.1319     0.895               (-0.9474, 1.084)
     str_dow_...01_24_00     0.1457    0.523     0.2787     0.781               (-0.8797, 1.171)
     str_dow_...01_24_00  -0.003916   0.5797  -0.006756     0.995                (-1.141, 1.133)
     str_dow_...01_24_00     0.5119   0.6438     0.7952     0.427               (-0.7504, 1.774)
      cp10_2011_09_05_00    0.06695   0.3807     0.1758     0.860              (-0.6796, 0.8134)
     is_weeke...09_05_00    -0.4058    0.259     -1.567     0.117              (-0.9137, 0.1021)
     str_dow_...09_05_00    -0.4998   0.6567     -0.761     0.447                (-1.787, 0.788)
     str_dow_...09_05_00     0.5105   0.5505     0.9273     0.354                (-0.5689, 1.59)
     str_dow_...09_05_00    -0.3479   0.5133    -0.6778     0.498               (-1.354, 0.6586)
     str_dow_...09_05_00     -0.264   0.5189    -0.5088     0.611               (-1.282, 0.7535)
     str_dow_...09_05_00    -0.2696   0.5765    -0.4676     0.640                 (-1.4, 0.8608)
     str_dow_...09_05_00    -0.1362   0.6407    -0.2126     0.832                 (-1.393, 1.12)
      cp11_2012_01_02_00     0.2574   0.4944     0.5207     0.603                (-0.712, 1.227)
     is_weeke...01_02_00     0.5849   0.3457      1.692     0.091         .    (-0.09292, 1.263)
     str_dow_...01_02_00     0.5218    0.878     0.5943     0.552                  (-1.2, 2.243)
     str_dow_...01_02_00    -0.4144   0.7342    -0.5644     0.573                (-1.854, 1.025)
     str_dow_...01_02_00     0.4073   0.6852     0.5945     0.552               (-0.9362, 1.751)
     str_dow_...01_02_00     0.8381    0.694      1.208     0.227               (-0.5228, 2.199)
     str_dow_...01_02_00     0.4047   0.7708     0.5251     0.600                (-1.107, 1.916)
     str_dow_...01_02_00     0.1802   0.8568     0.2103     0.833                   (-1.5, 1.86)
      cp12_2012_04_23_00     -1.735   0.3025     -5.736  1.07e-08       ***     (-2.328, -1.142)
     is_weeke...04_23_00    -0.5217   0.2197     -2.375     0.018         *  (-0.9524, -0.09092)
     str_dow_...04_23_00    -0.3187   0.5599    -0.5692     0.569               (-1.417, 0.7792)
     str_dow_...04_23_00    -0.2259   0.4685    -0.4821     0.630               (-1.145, 0.6928)
     str_dow_...04_23_00    -0.3114   0.4383    -0.7105     0.477                (-1.171, 0.548)
     str_dow_...04_23_00    -0.7798   0.4432     -1.759     0.079         .    (-1.649, 0.08923)
     str_dow_...04_23_00    -0.3741   0.4909    -0.7621     0.446               (-1.337, 0.5885)
     str_dow_...04_23_00    -0.1475   0.5459    -0.2702     0.787                (-1.218, 0.923)
      cp13_2013_04_01_00      1.433   0.1341      10.69    <2e-16       ***        (1.17, 1.696)
     is_weeke...04_01_00     0.1539   0.1028      1.497     0.134             (-0.04762, 0.3554)
     str_dow_...04_01_00    0.01899   0.2634    0.07207     0.943              (-0.4975, 0.5355)
     str_dow_...04_01_00     0.3881   0.2206      1.759     0.079         .   (-0.04449, 0.8206)
     str_dow_...04_01_00     0.1302   0.2067     0.6302     0.529               (-0.275, 0.5355)
     str_dow_...04_01_00     0.2075   0.2084     0.9955     0.320              (-0.2011, 0.6161)
     str_dow_...04_01_00     0.2493   0.2306      1.081     0.280              (-0.2028, 0.7014)
     str_dow_...04_01_00    -0.0954   0.2567    -0.3716     0.710               (-0.5988, 0.408)
      cp14_2013_11_11_00    -0.9378  0.09501      -9.87    <2e-16       ***    (-1.124, -0.7515)
     is_weeke...11_11_00    -0.1002  0.07316      -1.37     0.171             (-0.2437, 0.04324)
     str_dow_...11_11_00    0.06435   0.1872     0.3438     0.731              (-0.3027, 0.4314)
     str_dow_...11_11_00    -0.2741   0.1567     -1.749     0.080         .   (-0.5814, 0.03319)
     str_dow_...11_11_00   -0.07223    0.147    -0.4914     0.623               (-0.3605, 0.216)
     str_dow_...11_11_00    -0.0736   0.1483    -0.4964     0.620              (-0.3643, 0.2171)
     str_dow_...11_11_00    -0.2099   0.1641     -1.279     0.201              (-0.5317, 0.1119)
     str_dow_...11_11_00     0.1097   0.1827     0.6004     0.548              (-0.2485, 0.4679)




There might be too many featuers for the trend (including interaction terms).
Let's hide the interaction terms.


.. code-block:: default
   :lineno-start: 201


    # Displays intercept, trend features but not seasonality features.
    # Hides interaction terms.
    summary.get_coef_summary(
        is_intercept=True,
        is_trend=True,
        is_seasonality=False,
        is_interaction=False
    )





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

               Pred_col Estimate Std. Err  t value  Pr(>|t|) sig. code              95%CI
              Intercept    7.067  0.07816    90.41    <2e-16       ***      (6.913, 7.22)
                    ct1   0.1566   0.3892   0.4023     0.688            (-0.6065, 0.9196)
      cp0_2008_03_31_00  -0.3359   0.6343  -0.5295     0.596              (-1.58, 0.9079)
      cp1_2008_07_21_00   -1.587    0.568   -2.793     0.005        **  (-2.701, -0.4728)
      cp2_2008_11_10_00    2.573   0.5389    4.774  1.90e-06       ***     (1.516, 3.629)
      cp3_2009_03_09_00   0.6519   0.5423    1.202     0.229             (-0.4114, 1.715)
      cp4_2009_06_29_00   -1.338   0.5573     -2.4     0.016         *   (-2.43, -0.2449)
      cp5_2009_10_19_00   0.6892   0.5376    1.282     0.200             (-0.3649, 1.743)
      cp6_2010_02_15_00   -2.515   0.5437   -4.625  3.92e-06       ***   (-3.581, -1.449)
      cp7_2010_06_07_00    3.488   0.5579    6.253  4.66e-10       ***     (2.394, 4.582)
      cp8_2010_09_27_00   -2.989   0.5291   -5.648  1.79e-08       ***   (-4.026, -1.951)
      cp9_2011_01_24_00    1.765   0.3794    4.653  3.43e-06       ***     (1.021, 2.509)
     cp10_2011_09_05_00  0.06695   0.3807   0.1758     0.860            (-0.6796, 0.8134)
     cp11_2012_01_02_00   0.2574   0.4944   0.5207     0.603              (-0.712, 1.227)
     cp12_2012_04_23_00   -1.735   0.3025   -5.736  1.07e-08       ***   (-2.328, -1.142)
     cp13_2013_04_01_00    1.433   0.1341    10.69    <2e-16       ***      (1.17, 1.696)
     cp14_2013_11_11_00  -0.9378  0.09501    -9.87    <2e-16       ***  (-1.124, -0.7515)




Now we can see the pure trend features, including the continuous growth term and trend changepoints.
Each changepoint's name starts with "cp" followed by the time point it happens.
The estimated coefficients are the changes in slope at the corresponding changepoints.
We can also see the significance of the changepoints by examining their p-values.

We can also retrieve the filtered dataframe by setting ``return_df`` to ``True``.
This way you could further explore the coefficients.


.. code-block:: default
   :lineno-start: 219


    output = summary.get_coef_summary(
        is_intercept=True,
        is_trend=True,
        is_seasonality=False,
        is_interaction=False,
        return_df=True  # returns the filtered df
    )





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

               Pred_col Estimate Std. Err  t value  Pr(>|t|) sig. code              95%CI
              Intercept    7.067  0.07816    90.41    <2e-16       ***      (6.913, 7.22)
                    ct1   0.1566   0.3892   0.4023     0.688            (-0.6065, 0.9196)
      cp0_2008_03_31_00  -0.3359   0.6343  -0.5295     0.596              (-1.58, 0.9079)
      cp1_2008_07_21_00   -1.587    0.568   -2.793     0.005        **  (-2.701, -0.4728)
      cp2_2008_11_10_00    2.573   0.5389    4.774  1.90e-06       ***     (1.516, 3.629)
      cp3_2009_03_09_00   0.6519   0.5423    1.202     0.229             (-0.4114, 1.715)
      cp4_2009_06_29_00   -1.338   0.5573     -2.4     0.016         *   (-2.43, -0.2449)
      cp5_2009_10_19_00   0.6892   0.5376    1.282     0.200             (-0.3649, 1.743)
      cp6_2010_02_15_00   -2.515   0.5437   -4.625  3.92e-06       ***   (-3.581, -1.449)
      cp7_2010_06_07_00    3.488   0.5579    6.253  4.66e-10       ***     (2.394, 4.582)
      cp8_2010_09_27_00   -2.989   0.5291   -5.648  1.79e-08       ***   (-4.026, -1.951)
      cp9_2011_01_24_00    1.765   0.3794    4.653  3.43e-06       ***     (1.021, 2.509)
     cp10_2011_09_05_00  0.06695   0.3807   0.1758     0.860            (-0.6796, 0.8134)
     cp11_2012_01_02_00   0.2574   0.4944   0.5207     0.603              (-0.712, 1.227)
     cp12_2012_04_23_00   -1.735   0.3025   -5.736  1.07e-08       ***   (-2.328, -1.142)
     cp13_2013_04_01_00    1.433   0.1341    10.69    <2e-16       ***      (1.17, 1.696)
     cp14_2013_11_11_00  -0.9378  0.09501    -9.87    <2e-16       ***  (-1.124, -0.7515)




.. [1] Reference: "An Introduction to Bootstrap", Efron 1993.
.. [2] Reference: "High-Dimensional Inference: Confidence Intervals, p-Values and R-Software hdi", Dezeure, Buhlmann, Meier and Meinshausen.


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  36.528 seconds)


.. _sphx_glr_download_gallery_quickstart_0400_model_summary.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: 0400_model_summary.py <0400_model_summary.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: 0400_model_summary.ipynb <0400_model_summary.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
