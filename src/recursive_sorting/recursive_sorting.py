# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO

    merged_arr = []
    left_side = 0
    right_side = 0

    while left_side < len(arrA) and right_side < len(arrB):
        if arrA[left_side] < arrB[right_side]:
            merged_arr.append(arrA[left_side])
            # left_side++
            left_side += 1
        
        else:
            merged_arr.append(arrB[right_side])
            right_side += 1

    merged_arr.extend(arrA[left_side:])
    merged_arr.extend(arrB[right_side:])
    

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):  # beginning of sort
    # TO-DO

    if len(arr) <= 1:
        return arr
    
    else:

        middle_array = len(arr) // 2

        arrA = merge_sort(arr[:middle_array])
        arrB = merge_sort(arr[middle_array:])

    return merge(arrA, arrB)

# arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(arr)
# print(merge_sort(arr))

"""
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
"""