# Drop the origal date and hour columns
data_stacked = data_stacked.drop(['date', 'hour'], axis=1)
data_stacked.head()