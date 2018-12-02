# add a weekday column
data_daily['weekday'] = data_daily.index.weekday
data_daily.head()