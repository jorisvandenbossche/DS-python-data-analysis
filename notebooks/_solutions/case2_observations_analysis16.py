# Multiple lines
obs_with_weight = survey_data.dropna(subset=["wgt"])
median_weight = obs_with_weight.groupby(['name'])["wgt"].median()
median_weight.sort_values(ascending=False)