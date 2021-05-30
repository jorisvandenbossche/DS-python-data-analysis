mask = survey_data_unique['species'].isna() & survey_data_unique['sex'].notna()
not_identified = survey_data_unique[mask]