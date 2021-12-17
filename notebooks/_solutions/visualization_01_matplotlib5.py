fig, (ax0, ax1) = plt.subplots(1, 2, constrained_layout=True)

flowdata.min().plot.bar(ylabel="min discharge", ax=ax0)
flowdata.max().plot.bar(ylabel="max discharge", ax=ax1)

fig.suptitle(f"Minimal and maximal discharge from {flowdata.index[0]:%Y-%m-%d} till {flowdata.index[-1]:%Y-%m-%d}");