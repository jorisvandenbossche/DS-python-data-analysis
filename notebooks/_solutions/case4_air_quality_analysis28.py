data_weekend = data.groupby(['weekend', 'hour']).mean()
data_weekend.head()