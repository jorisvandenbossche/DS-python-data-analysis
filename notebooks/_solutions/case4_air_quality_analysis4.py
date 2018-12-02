fig, ax = plt.subplots()
data.loc['2009':, 'FR04037'].resample('M').mean().plot(ax=ax, label='mean')
data.loc['2009':, 'FR04037'].resample('M').median().plot(ax=ax, label='median')
ax.legend(ncol=2)
ax.set_title("FR04037");