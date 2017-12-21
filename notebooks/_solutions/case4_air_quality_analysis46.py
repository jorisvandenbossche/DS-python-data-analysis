(pn.ggplot(subset,
           pn.aes(x="BETN029", y="FR04037", color="weekday"))
    + pn.geom_point()
    + pn.stat_smooth(method='lm'))