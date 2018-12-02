mask = pd.to_datetime(survey_data_decoupled[["year", "month", "day"]], errors='coerce').isnull()
survey_data_decoupled.loc[mask, "day"] = 30