survey_data = pd.merge(observations_data, species_names, how="left",
                       left_on="species_ID", right_on="ID")
survey_data