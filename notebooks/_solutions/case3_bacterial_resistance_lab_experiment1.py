tidy_experiment = main_experiment.melt(id_vars=['Bacterial_genotype', 'Phage_t', 'experiment_ID'],
                                       value_vars=['OD_0h', 'OD_20h', 'OD_72h'],
                                       var_name='experiment_time_h',
                                       value_name='optical_density', )
tidy_experiment