(p9.ggplot(tidy_experiment, p9.aes(x='experiment_time_h', 
                                   y='optical_density'))
    + p9.geom_violin()
)