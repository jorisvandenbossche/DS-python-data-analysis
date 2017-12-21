# when still having multiple factors, it becomes useful to convert to tidy dataset and use plotnine
(pn.ggplot(data_weekend_tidy,
           pn.aes(x='hour', y='no2', color='weekend'))
    + pn.geom_line()
    + pn.facet_wrap('station'))