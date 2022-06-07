df_tidy = pd.melt(df, id_vars=["Hoofdgemeente", "Energie", "SLP"], var_name="time", value_name="consumption")
df_tidy