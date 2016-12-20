fig, ax = plt.subplots()
data.loc['2009':, 'FR04037'].resample('M').mean().plot(ax=ax)
data.loc['2009':, 'FR04037'].resample('M').median().plot(ax=ax)
ax.legend(ncol=2);