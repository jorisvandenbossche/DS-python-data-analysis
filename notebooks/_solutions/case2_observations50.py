sns.relplot(data=year_evolution, x='eventDate', y="counts", 
            col="taxa", col_wrap=2, kind="line", height=2, aspect=5, 
            facet_kws={"sharey": False})