# add a column to the dataframe that indicates the month (integer value of 1 to 12):
data['month'] = data.index.month

# now, we can calculate the mean of each month over the different years:
data.groupby('month').mean()

# plot the typical monthly profile of the different stations:
data.groupby('month').mean().plot()