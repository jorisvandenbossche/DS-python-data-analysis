# plotnine
(pn.ggplot(data_daily["2012"],
           pn.aes(x='factor(weekday)', y='BETR801'))
    + pn.geom_boxplot())