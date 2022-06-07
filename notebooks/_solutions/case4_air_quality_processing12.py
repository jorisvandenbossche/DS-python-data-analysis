dfs = []

for filename in data_files:
    station = filename.name[:7]
    df = read_airbase_file(filename, station)
    dfs.append(df)