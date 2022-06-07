# Groupby wise
# Note the different x-axis labels
df2011.groupby(df2011.index.isocalendar().week)[['BETN029', 'BETR801']].quantile(0.95).plot()