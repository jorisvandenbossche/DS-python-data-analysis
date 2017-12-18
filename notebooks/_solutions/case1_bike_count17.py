def process_bike_count_data(df):
    """
    Process the provided dataframe: parse datetimes and rename columns.
    
    """
    df.index = pd.to_datetime(df['dag'] + ' ' + df['tijdstip'], format="%d.%m.%y %H:%M:%S")
    df = df.drop(['dag', 'tijdstip'], axis=1)
    df = df.rename(columns={'noord': 'north', 'zuid':'south', 'actief': 'active'})
    return df