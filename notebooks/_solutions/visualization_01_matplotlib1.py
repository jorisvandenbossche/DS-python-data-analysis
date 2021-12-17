fig, ax  = plt.subplots(figsize=(12, 4))

ax.plot(data, color='darkgrey')
ax.set_xlabel('days since start');
ax.set_ylabel('measured value');