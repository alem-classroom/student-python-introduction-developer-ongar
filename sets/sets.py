def size_of_set(set):
    # return size of set  
    return len(set)
def is_elem_in_set(set, elem):
    # return true if elem exists in set, false otherwise
    if elem in set:
        return True
    return False

def are_sets_equal(first_set, second_set):
    # return true if sets have the same elements inside, otherwise false
    if first_set == second_set:
        return True
    return False


def add_elem_to_set(set, elem):
    # add elem to the set if elem does not exist in set, and return the set
    # if elem exists in set, return set
    if elem not in set:
        set.add(elem)
        return set
    else:
        return set

def remove_elem_if_exists(set, elem):
    # remove elem from set if it exists, and return the set
    if elem in set:
        set.discard(elem)
        return set
    else:
        return set

def delete_first_element(set):
    # delete first elemenent of set
    set.pop()
    return set
    
