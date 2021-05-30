duplicate_observations = survey_data_processed[survey_data_processed.duplicated(keep=False)]
duplicate_observations.sort_values(["eventDate", "verbatimLocality"]).head(9)