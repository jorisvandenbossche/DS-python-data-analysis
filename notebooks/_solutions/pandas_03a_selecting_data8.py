df['Surname'] = df['Name'].str.split(",").str.get(0)
df['Surname']