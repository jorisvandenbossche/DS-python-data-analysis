df_monthly = df.resample('ME').sum()
df_monthly.plot()