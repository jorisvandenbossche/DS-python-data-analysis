sns.set_style("ticks")
g = sns.FacetGrid(falcor, row="Phage", aspect=3, height=3)
g.map(errorbar, 
      "Bacterial_genotype", "log10 Mc", 
      "log10 LBc", "log10 UBc")