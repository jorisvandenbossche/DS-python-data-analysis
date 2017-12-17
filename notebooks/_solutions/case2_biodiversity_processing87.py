#%%timeit
unique_species = \
    survey_data_species.groupby(["genus", "species"]).first().reset_index()[["genus", "species"]]