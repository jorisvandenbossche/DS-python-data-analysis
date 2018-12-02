(pn.ggplot(tidy_experiment, pn.aes(x='experiment_time_h', 
                                   y='optical_density'))
    + pn.geom_violin()
    + pn.facet_wrap('Phage_t')
)