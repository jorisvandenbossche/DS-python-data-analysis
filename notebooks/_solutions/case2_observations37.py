# Multiple lines
obs_with_weight = survey_data.dropna(subset=["weight"])
median_weight = obs_with_weight.groupby(['name'])["weight"].median()
median_weight.sort_values(ascending=False)