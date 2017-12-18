survey_data_plots = pd.merge(survey_data_decoupled, plot_data_selection, 
                             how="left", on="plot")