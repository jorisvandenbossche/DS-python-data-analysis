#%%timeit
unique_species = survey_data_plots[["genus", "species"]].drop_duplicates().dropna()