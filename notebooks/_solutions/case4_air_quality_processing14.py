# We reset the index to have the date and hours available as columns
data_stacked = data_stacked.reset_index()
data_stacked = data_stacked.rename(columns={'level_1': 'hour'})
data_stacked.head()