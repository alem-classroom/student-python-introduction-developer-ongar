def insert_squares(arr, num):
    # add square of numbers from 1 to num to the list named arr and return list
    i = 1
    while i <= num:
        arr.append(i*i)
        i += 1
    return arr
