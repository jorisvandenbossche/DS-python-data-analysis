def transform_utm_to_wgs(row):
    """Converts the x and y coordinates

    Parameters
    ----------
    row : pd.Series
        Single DataFrame row

    Returns
    -------
    pd.Series with longitude and latitude
    """
    transformer = Transformer.from_crs("EPSG:32612", "epsg:4326")

    return pd.Series(transformer.transform(row['xutm'], row['yutm']))