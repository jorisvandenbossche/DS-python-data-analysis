dates = pd.date_range("2021-01-01", periods=100, freq="D")

fig, ax  = plt.subplots(figsize=(12, 4))

ax.plot(dates, data, color='darkgrey')
ax.axhspan(ymin=-5, ymax=5, color='green', alpha=0.2)

ax.set_xlabel('days since start');
ax.set_ylabel('measured value');