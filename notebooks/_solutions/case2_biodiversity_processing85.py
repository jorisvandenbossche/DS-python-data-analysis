#%%timeit
unique_species = survey_data_species[["genus", "species"]].drop_duplicates().dropna()