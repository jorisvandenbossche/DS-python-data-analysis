sns.catplot(data=victims_hour_of_day, 
            x="Hour of the day", 
            y="Number of victims", 
            kind="bar", 
            aspect=4,
            height=3,
)