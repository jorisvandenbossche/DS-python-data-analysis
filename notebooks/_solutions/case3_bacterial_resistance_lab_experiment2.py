(p9.ggplot(tidy_experiment, p9.aes(x='optical_density'))
    + p9.geom_histogram(bins=30, color='white', fill='lightgrey')
    + p9.theme_bw()
)