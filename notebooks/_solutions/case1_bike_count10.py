def process_bike_count_data(df):
    """Process the provided dataframe: parse datetimes and rename columns.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame as read from the raw `fietstellingen`,
        containing the `datum`, `tijd`, `ri Centrum`
        and `ri Mariakerke` columns.

    Returns
    -------
    df2 : pandas.DataFrame
        DataFrame with the datetime info as index and the
        `direction_centre` and `direction_mariakerke` columns
        with the counts.
    """
    df.index = pd.to_datetime(df['datum'] + ' ' + df['tijd'],
                              format="%d/%m/%Y %H:%M")
    df2 = df.drop(columns=['datum', 'tijd'])
    df2 = df2.rename(columns={'ri Centrum': 'direction_centre',
                              'ri Mariakerke':'direction_mariakerke'})
    return df2