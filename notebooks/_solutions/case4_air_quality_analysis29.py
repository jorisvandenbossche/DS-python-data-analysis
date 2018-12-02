subset = data['2009-01'].copy()
subset["weekday"] = subset.index.weekday
subset = subset[subset['weekday'].isin([0, 6])]