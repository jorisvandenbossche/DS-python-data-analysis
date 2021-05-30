fig, ax = plt.subplots()
data['2012'].mean().plot(kind='bar', ax=ax, rot=0, color='C0')
ax.set_ylabel("NO$_2$ concentration (µg/m³)")
ax.axhline(y=40., color='darkorange')
ax.text(0.01, 0.48, 'Yearly limit is 40 µg/m³',
        horizontalalignment='left', fontsize=13, 
        transform=ax.transAxes, color='darkorange');