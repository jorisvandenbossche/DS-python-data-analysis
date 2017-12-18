data_weekend = data.groupby(['weekend', data.index.hour]).mean()
data_weekend_BETR801 = data_weekend['BETR801'].unstack(level=0)
data_weekend_BETR801.plot()