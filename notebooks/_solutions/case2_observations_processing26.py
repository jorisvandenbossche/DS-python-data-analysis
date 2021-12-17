#%%timeit
unique_species = \
    survey_data_plots.groupby(["genus", "species"]).first().reset_index()[["genus", "species"]]