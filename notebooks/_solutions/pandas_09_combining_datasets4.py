joined = pd.merge(df, df_muni[["CD_REFNIS", "TX_PROV_DESCR_EN"]], on="CD_REFNIS", how="left")
joined