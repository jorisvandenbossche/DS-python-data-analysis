# alternative solution with pandas' string methods
df['Surname'] = df['Name'].str.split(",").str.get(0)