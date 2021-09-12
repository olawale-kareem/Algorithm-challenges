# an algorithm to return the index of a number and verify it


# long version
def liner_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i    
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


# call
numbers = [1,2,3,4,5,6,7,8,9]
result = liner_search(numbers, 6)
verify(result)


# short version

def linear_search(arr, target_num):
    try:  
        index_target = arr.index(target_num)    
    except ValueError:
        print("Target not found in list")
    else:
        print("Target found at index: ", index_target)

# i used try catch because once an index is not there it will tru an error
numbers = [1,2,3,4,5,6,7,8,9]
linear_search(numbers, 12)
