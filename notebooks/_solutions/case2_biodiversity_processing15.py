def transform_utm_to_wgs(row):
    """
    Converts the x and y coordinates of this row into a Series of the
    longitude and latitude.
    
    """
    utm12n = pyproj.Proj("+init=EPSG:32612")
    wgs84 = pyproj.Proj("+init=EPSG:4326")
    
    return pd.Series(pyproj.transform(utm12n, wgs84, row['xutm'], row['yutm']))