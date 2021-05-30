sns.catplot(data=falcor, kind="point",
            x='Bacterial_genotype', 
            y='log10 Mc', 
            row="Phage",
            join=False, ci=None,
            aspect=3, height=3,
            color="black")