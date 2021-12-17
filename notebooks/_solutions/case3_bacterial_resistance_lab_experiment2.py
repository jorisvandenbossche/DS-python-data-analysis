sns.set_style("white")
histplot = sns.displot(data=tidy_experiment, x="optical_density",
                       color='grey', edgecolor='white')

histplot.fig.suptitle("Optical density distribution")
histplot.axes[0][0].set_ylabel("Frequency");