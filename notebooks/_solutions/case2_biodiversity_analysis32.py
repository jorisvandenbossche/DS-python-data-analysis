(pn.ggplot(subselection_sex, pn.aes(x="verbatimLocality", fill="sex"))
     + pn.geom_bar(position='dodge')
     + pn.scale_x_discrete(breaks=np.arange(1, 25, 1), limits=np.arange(1, 25, 1))
)