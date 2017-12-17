pd.pivot_table(tidy_experiment, values='optical_density', 
               index='Bacterial_genotype', 
               columns='experiment_time_h',
               aggfunc='mean')