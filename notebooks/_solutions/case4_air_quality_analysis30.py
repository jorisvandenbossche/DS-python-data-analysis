# using a tidy dataset and plotnine
data_weekend_BETR801_tidy = data_weekend['BETR801'].reset_index()

(pn.ggplot(data_weekend_BETR801_tidy,
           pn.aes(x='hour', y='BETR801', color='weekend'))
    + pn.geom_line())