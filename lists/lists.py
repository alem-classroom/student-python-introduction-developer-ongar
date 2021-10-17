def size_of_list(list):
    return(len(list))

def add_elem_to_list(list, elem):
    list.append(elem)
    return list

def delete_elem_from_list(list, index = -1):
    if len(list) < index:
        return []
    return list.pop(index)

def count_elements_in_list(list, x):
    occurences = list.count(x)
    return occurences

def sort_list(list):
    sorted = list.sort()
    return sorted

def reverse(list):
    reversed = list.reverse()
    return reversed
