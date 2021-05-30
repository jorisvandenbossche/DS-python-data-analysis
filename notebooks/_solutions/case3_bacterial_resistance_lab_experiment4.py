sns.catplot(data=tidy_experiment, x="experiment_time_h", y="optical_density", 
            col="Phage_t", col_wrap=2, kind="violin")