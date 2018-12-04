(p9.ggplot(density_mean, p9.aes(x='Bacterial_genotype',
                                y='optical_density',
                                fill='Phage_t'))
    + p9.geom_bar(stat='identity', position='dodge')
    + p9.facet_wrap('experiment_time_h', scales='free', nrow=3)
    + p9.scale_fill_brewer(type='qual', palette=8)
)