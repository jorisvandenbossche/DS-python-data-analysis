# Single line statement
survey_data.dropna(subset=["weight"]).groupby(['name'])["weight"].median().sort_values(ascending=False)