def process_bike_count_data(df):
    """
    Process the provided dataframe: parse datetimes and rename columns.
    
    """
    df.index = pd.to_datetime(df['datum'] + ' ' + df['tijd'], format="%d/%m/%Y %H:%M")
    df = df.drop(['datum', 'tijd'], axis=1)
    df = df.rename(columns={'ri Centrum': 'direction_centre', 'ri Mariakerke':'direction_mariakerke'})
    return df