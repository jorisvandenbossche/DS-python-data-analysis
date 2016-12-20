mask = survey_data_unique['species'].isnull() & survey_data_unique['sex'].notnull()
not_identified = survey_data_unique[mask]