sns.catplot(data=survey_data, x="verbatimLocality", 
            hue="sex", kind="count", height=3, aspect=3)