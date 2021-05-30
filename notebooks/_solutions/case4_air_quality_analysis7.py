# with tidy dataframe
data_tidy_subset = data_tidy[(data_tidy['datetime'] >= "2011-01") & (data_tidy['datetime'] < "2011-09")]

fig, ax = plt.subplots()
sns.violinplot(data=data_tidy_subset, x="station", y="no2", palette="GnBu_d", ax=ax)
ax.set_ylabel("NO$_2$ concentration (µg/m³)")