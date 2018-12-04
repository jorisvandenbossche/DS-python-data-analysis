# precalculate the median value
end_of_experiment["Phage_median"] = end_of_experiment.groupby(["Phage_t", "Bacterial_genotype"])['optical_density'].transform('median')

p9.options.figure_size = (8, 10)
(p9.ggplot(end_of_experiment, p9.aes(x='Bacterial_genotype', 
                                     y='optical_density'))
    + p9.geom_jitter(mapping=p9.aes(color='factor(PhageR_72h)'), 
                     width=0.2, height=0., size=2, fill='white')
    + p9.facet_wrap("Phage_t", nrow=4, 
                    labeller=p9.as_labeller({'C_noPhage' : '(a) no phage', 'L' : '(b) phage $\lambda$', 
                                             'T4' : '(c) phage T4', 'T7': '(d) phage T7'}))
    + p9.theme_bw()
    + p9.xlab("Bacterial genotype")
    + p9.ylab("Bacterial density (OD)")
    + p9.theme(strip_text=p9.element_text(size=11))
    + p9.geom_crossbar(inherit_aes=False, alpha=0.5,
                       mapping=p9.aes(x='Bacterial_genotype', y='Phage_median',
                                      ymin='Phage_median', ymax='Phage_median'))
    + p9.scale_color_manual(values=["black", "red"], guide=False)
)