mask = pd.to_datetime(survey_data_decoupled[["year", "month", "day"]], errors='coerce').isna()
trouble_makers = survey_data_decoupled[mask]