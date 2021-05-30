sns.catplot(data=n_plot_sex, x="verbatimLocality", y="count",
            hue="sex", kind="bar", height=3, aspect=3)