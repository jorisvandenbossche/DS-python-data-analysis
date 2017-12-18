(pn.ggplot(tidy_experiment, pn.aes(x='optical_density'))
    + pn.geom_histogram(bins=30, color='white', fill='lightgrey')
    + pn.theme_bw()
)