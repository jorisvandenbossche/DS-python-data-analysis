# A more in-detail plotting version of the graph.
fig, ax = plt.subplots()
newyear.plot(ax=ax, color=['LightGreen', 'LightBlue'], legend=False, rot=0)
newyear.rolling(10, center=True).mean().plot(linewidth=2, ax=ax, color=['DarkGreen', 'DarkBlue'], rot=0)

# Intensive customization of the labels with matplotlib to point specifically at 18h, 0h and 6h (Purely as illustration!)
import matplotlib.dates as mdates
ax.set_xticklabels(ax.get_xticklabels(), ha='center', minor=False)
ax.xaxis.set_major_locator(mdates.HourLocator(byhour=[18, 0, 6]))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m\n%H:%M'))
ax.set_xlabel('')
ax.set_ylabel('Cyclists count')