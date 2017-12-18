(pn.ggplot(heatmap_prep_plotnine, pn.aes(x="month", y="year", fill="count"))
    + pn.geom_tile()
    + pn.scale_fill_cmap("Reds")
    + pn.scale_y_reverse()
    + pn.theme( 
     axis_ticks=pn.element_blank(),
     panel_background=pn.element_rect(fill='white'))
)  