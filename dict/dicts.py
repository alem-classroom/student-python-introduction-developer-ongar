def clear_dict(dict):
    return  dict.clear()

def get_dict_items(dict):
    return dict.items()

def get_dict_keys(dict):
    return dict.keys()

def get_dict_value_by_key(dict, key):
    if(dict.get(key)):
        return dict[key]

def delete_dict_element_by_key(dict, key):
    dict.pop(key)
    return dict
