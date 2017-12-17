(pn.ggplot(titanic.dropna(subset=['Age']), pn.aes(x='Age'))
     + pn.geom_histogram(bins=30)
     + pn.facet_wrap('Sex', nrow=2)
)