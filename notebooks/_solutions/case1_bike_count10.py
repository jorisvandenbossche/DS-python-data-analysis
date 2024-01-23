def process_bike_count_data(df):
    """Process the provided dataframe: parse datetimes and rename columns.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame as read from the raw `fietstellingen`,
        containing the 'Datum', 'Uur5Minuten', 
        'Ordening', 'Totaal', 'Tegenrichting', 'Hoofdrichting' columns.

    Returns
    -------
    df2 : pandas.DataFrame
        DataFrame with the datetime info as index and the
        `direction_centre` and `direction_mariakerke` columns
        with the counts.
    """
    timestamps = pd.to_datetime(df["Ordening"], format="%Y-%m-%dT%H:%M:%S%z", utc=True)    
    df2 = df.drop(columns=['Datum', 'Uur5Minuten', 'Ordening', 'Code'])
    df2["timestamp"] = timestamps
    df2 = df2.set_index("timestamp")
    df2 = df2.rename(columns={'Tegenrichting': 'direction_centre',
                              'Hoofdrichting': 'direction_mariakerke',
                              'Totaal': 'total',
                              'Locatie': 'location'
                             })
    return df2