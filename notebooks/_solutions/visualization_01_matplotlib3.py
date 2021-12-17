fig, ax  = plt.subplots(figsize=(12, 4))

ax.bar(dates[-10:], data[-10:], color='darkgrey')
ax.bar(dates[-6], data[-6], color='orange')