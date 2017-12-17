def transform_utm_to_wgs(row):
    """
    Converts the x and y coordinates of this row into a Series of the
    longitude and latitude.
    
    """
    return pd.Series(pyproj.transform(utm12n, wgs84, row['xutm'], row['yutm']))