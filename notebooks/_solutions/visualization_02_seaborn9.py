sns.catplot(data=compare_dead_30,
            x="dead_prop",
            y="road_user_type",
            kind="bar",
            hue="datetime"
           )