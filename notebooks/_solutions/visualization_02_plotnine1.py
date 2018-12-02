(p9.ggplot(titanic,
           p9.aes(x='factor(Pclass)', y='Fare', color='Sex'))
     + p9.geom_jitter()
) 