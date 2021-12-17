alarm_level = 20
max_datetime, max_value = flowdata["LS06_347"].idxmax(), flowdata["LS06_347"].max()

fig, ax = plt.subplots(figsize=(18, 4))
flowdata["LS06_347"].plot(ax=ax)

ax.axhline(y=alarm_level, color='red', linestyle='-', alpha=0.8)
ax.annotate('Alarm level', xy=(flowdata.index[0], alarm_level), 
            xycoords="data", xytext=(10, 10), textcoords="offset points",
            color="red", fontsize=12)
ax.annotate(f"Flood event on {max_datetime:%Y-%m-%d}",
            xy=(max_datetime, max_value), xycoords='data',
            xytext=(-30, -30), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom',
            fontsize=12)