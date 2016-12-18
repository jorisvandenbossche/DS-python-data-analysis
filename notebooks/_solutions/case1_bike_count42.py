df_monthly = df.resample('M').sum()
df_monthly.plot()