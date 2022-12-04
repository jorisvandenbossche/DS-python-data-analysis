g = sns.jointplot(
    data=daily_with_temp, x="air_temperature", y="n_victims", kind="reg"
)