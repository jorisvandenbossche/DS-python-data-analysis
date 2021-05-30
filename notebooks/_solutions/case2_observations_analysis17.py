# Single line statement
(survey_data
     .dropna(subset=["wgt"])
     .groupby(['name'])["wgt"]
     .median()
     .sort_values(ascending=False)
)