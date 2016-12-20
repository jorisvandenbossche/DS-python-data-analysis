# Cleaning the column names as well to end up with a better legend
data_weekend_BETR801 = data_weekend_BETR801.rename(columns={True: 'weekend', False: 'weekday'})
data_weekend_BETR801.columns.name = None
data_weekend_BETR801.plot()