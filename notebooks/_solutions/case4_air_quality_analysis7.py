# with plotnine
data_tidy_subset = data_tidy[(data_tidy['datetime'] >= "2011-01") & (data_tidy['datetime'] < "2011-09")]

(pn.ggplot(data_tidy_subset, pn.aes(x='station', y='no2'))
    + pn.geom_violin()
    + pn.ylab("NO$_2$ concentration (µg/m³)"))