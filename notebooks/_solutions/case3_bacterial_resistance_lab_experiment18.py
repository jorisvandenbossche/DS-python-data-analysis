# precalculate the median value
end_of_experiment["Phage_median"] = end_of_experiment.groupby(["Phage_t", "Bacterial_genotype"])['optical_density'].transform('median')

pn.options.figure_size = (8, 10)
(pn.ggplot(end_of_experiment, pn.aes(x='Bacterial_genotype', 
                                     y='optical_density'))
    + pn.geom_jitter(mapping=pn.aes(color='factor(PhageR_72h)'), 
                     width=0.2, height=0., size=2, fill='white')
    + pn.facet_wrap("Phage_t", nrow=4, 
                    labeller=pn.as_labeller({'C_noPhage' : '(a) no phage', 'L' : '(b) phage $\lambda$', 
                                             'T4' : '(c) phage T4', 'T7': '(d) phage T7'}))
    + pn.theme_bw()
    + pn.xlab("Bacterial genotype")
    + pn.ylab("Bacterial density (OD)")
    + pn.theme(strip_text=pn.element_text(size=11))
    + pn.geom_crossbar(inherit_aes=False, alpha=0.5,
                       mapping=pn.aes(x='Bacterial_genotype', y='Phage_median',
                                      ymin='Phage_median', ymax='Phage_median'))
    + pn.scale_color_manual(values=["black", "red"], guide=False)
)