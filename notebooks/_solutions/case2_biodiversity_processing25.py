mask = pd.to_datetime(survey_data_decoupled[["year", "month", "day"]], errors='coerce').isnull()
trouble_makers = survey_data_decoupled[mask]