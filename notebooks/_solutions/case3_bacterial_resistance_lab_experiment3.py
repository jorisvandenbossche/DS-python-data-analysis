sns.catplot(data=tidy_experiment, x="experiment_time_h",
            y="optical_density", kind="violin")