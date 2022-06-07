subset = data.loc['2009-01'].copy()
subset["dayofweek"] = subset.index.dayofweek
subset = subset[subset['dayofweek'].isin([0, 6])]