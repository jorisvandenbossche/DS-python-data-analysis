sns.catplot(data=density_mean, kind="bar",
            x='Bacterial_genotype',
            y='optical_density',
            hue='Phage_t',
            row="experiment_time_h",
            sharey=False,
            aspect=3, height=3,
            palette="colorblind")