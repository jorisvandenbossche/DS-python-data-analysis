# An alternative method using `groupby` and `unstack`
data_daily.groupby(['dayofweek', 'week'])['BETR801'].mean().unstack(level=0).boxplot();