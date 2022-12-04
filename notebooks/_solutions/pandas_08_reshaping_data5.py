df_overall = df_tidy.groupby(["time", "Energie"])[["consumption"]].sum() # or with .reset_index()
df_overall.head()