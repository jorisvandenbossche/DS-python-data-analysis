survey_data_decoupled.loc[pd.to_datetime(survey_data_decoupled[["year", "month", "day"]], 
                                         errors='coerce').isnull(), "day"] = 30