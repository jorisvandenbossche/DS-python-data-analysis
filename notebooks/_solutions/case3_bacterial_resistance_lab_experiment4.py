tidy_experiment = main_experiment.melt(id_vars=['AB_r', 'Bacterial_genotype', 'Phage_t', 
                                                'Survival_72h', 'PhageR_72h'], 
                                       value_vars=['OD_0h', 'OD_20h', 'OD_72h'], 
                                       var_name='experiment_time_h', 
                                       value_name='optical_density', )
tidy_experiment.head()