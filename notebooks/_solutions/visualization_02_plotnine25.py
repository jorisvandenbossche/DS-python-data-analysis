(pn.ggplot(titanic.dropna(subset=['Age']), pn.aes(x='Sex', y='Age'))
     + pn.geom_violin()
     + pn.geom_jitter(alpha=0.2)
)