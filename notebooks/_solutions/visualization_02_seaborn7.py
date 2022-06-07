sns.catplot(data=victims_gender_hour_of_day.fillna("unknown"),
            x="datetime", 
            y="n_victims", 
            row="gender",
            palette="rocket",
            kind="bar", 
            aspect=4,
            height=3)