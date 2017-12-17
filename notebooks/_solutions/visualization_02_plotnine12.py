(pn.ggplot(titanic,
           pn.aes(x='factor(Pclass)', y='Fare', color='Sex'))
     + pn.geom_jitter()
) 