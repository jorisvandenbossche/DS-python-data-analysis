survey_data_plots = pd.merge(survey_data_species, plot_data_selection,
                             how="left", on="plot")