df_survival = df.groupby(["Pclass", "Sex"])["Survived"].mean().reset_index()
df_survival