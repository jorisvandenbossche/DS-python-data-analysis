(p9.ggplot(titanic.dropna(subset=['Age']), p9.aes(x='Sex', y='Age'))
     + p9.geom_violin()
     + p9.geom_jitter(alpha=0.2)
)