sns.catplot(data=observations, x="verbatimLocality", 
            hue="sex", kind="count", height=3, aspect=3)