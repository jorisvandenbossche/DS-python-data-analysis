(p9.ggplot(titanic.dropna(subset=['Age']), p9.aes(x='Age'))
     + p9.geom_histogram(bins=30)
     + p9.facet_wrap('Sex', nrow=2)
)