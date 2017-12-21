# with seaborn
fig, ax = plt.subplots()
sns.violinplot(data=data['2011-01': '2011-08'], palette="GnBu_d", ax=ax)
ax.set_ylabel("NO$_2$ concentration (µg/m³)")