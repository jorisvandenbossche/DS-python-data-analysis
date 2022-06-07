joined = pd.merge(df, df_legal_forms, on="CD_LGL_PSN_VAT", how="left")
joined