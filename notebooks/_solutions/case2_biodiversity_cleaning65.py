survey_data_plots["verbatimLocality"] = survey_data_plots["plot"].apply(value_to_measurement, 
                                                                        args=(["plot"]))
survey_data_plots = survey_data_plots.drop("plot", axis=1)