subset = data['2011':'2012']['L06_347']
fig, ax = plt.subplots()
subset.resample('M').mean().plot(ax=ax)
subset.resample('M').median().plot(ax=ax)
ax.legend(["mean", "median"])