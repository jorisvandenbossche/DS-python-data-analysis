(pn.ggplot(density_mean, pn.aes(x='Bacterial_genotype',
                                y='optical_density',
                                fill='Phage_t'))
    + pn.geom_bar(stat='identity', position='dodge')
    + pn.facet_wrap('experiment_time_h', dir='v', scales='free')
    + pn.scale_fill_brewer(type='qual', palette=8)
)