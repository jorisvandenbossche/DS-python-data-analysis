fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(15, 5))

sns.ecdfplot(data=weekly_victim_dead_lc, x="dead_prop", hue="light_conditions", ax=ax0)
sns.ecdfplot(data=weekly_victim_dead_rt, x="dead_prop", hue="road_type", ax=ax1)