fig, ax = plt.subplots()

data['1999':].resample('YE').mean().plot(ax=ax)
data['1999':].mean(axis=1).resample('YE').mean().plot(color='k', 
                                            linestyle='--', 
                                            linewidth=4, 
                                            ax=ax, 
                                            label='Overall mean')
ax.legend(loc='center', ncol=3, 
          bbox_to_anchor=(0.5, 1.06))
ax.set_ylabel("NO$_2$ concentration (µg/m³)");