fig, ax = plt.subplots()
sns.violinplot(data=data['2011-01': '2011-08'], palette="GnBu_d", 
                   bw=.2, cut=1, linewidth=1, ax=ax) # some additional settings to improve the appearance
ax.set_ylabel("NO$_2$ concentration (µg/m³)")