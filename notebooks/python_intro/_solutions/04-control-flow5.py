for file_name in file_names:
    if file_name.startswith("sigma"):
        print(f"Processing file {file_name} with sigma pipeline.")
    elif file_name.startswith("ava"):
        print(f"Processing file {file_name} with avalanche pipeline.")       
    else: 
        print(f"Unrecognized file {file_name}")