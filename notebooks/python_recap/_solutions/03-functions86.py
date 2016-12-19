def check_for_jey(checkdict, key):
    """
    Function checks the presence of key in dictionary checkdict and returns an 
    exception if the key is already used in the dictionary
    
    """
    if key in checkdict.keys():
        raise Exception('Key already used in this dictionary')