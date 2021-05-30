# Resample wise
# Note the different x-axis labels
df2011[['BETN029', 'BETR801']].resample('W').quantile(0.75).plot()