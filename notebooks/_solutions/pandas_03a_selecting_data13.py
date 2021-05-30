# alternative using an "inline" lambda function
df['Surname'] = df['Name'].apply(lambda x: x.split(',')[0])