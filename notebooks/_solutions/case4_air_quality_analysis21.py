# Resample wise (not possible to use quantile directly on a resample, so you need a lambda function)
# Note the different x-axis labels
df2011[['BETN029', 'BETR801']].resample('W').agg(lambda x: x.quantile(0.75)).plot()