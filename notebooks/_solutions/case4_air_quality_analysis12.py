# Resample wise
df2011 = data.loc['2011']
df2011[['BETN029', 'BETR801']].resample('W').quantile(0.95).plot()