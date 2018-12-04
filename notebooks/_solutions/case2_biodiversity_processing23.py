survey_data_species = pd.merge(survey_data_plots, species_data, how="left",  # LEFT OR INNER?
                                left_on="species", right_on="species_id")