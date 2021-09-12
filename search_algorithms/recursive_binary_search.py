def recursive_binary_search(arr,target):
    # check the length of the list first
    # This condition also accounts for when a number is not in the list,
    # Then len of arr evetually turns to zero as the search progresses
    if len(arr) == 0:
        return False
    else:
        # get the midpoint
        mid_point = len(arr)// 2
        if arr[mid_point] == target:
            print("target found")
            return True
        else:
            if arr[mid_point] < target:
                return recursive_binary_search(arr[mid_point+1 : ], target)
            else:
                return recursive_binary_search(arr[ : mid_point ], target)

numbers = [1,2,3,4,5,6,7,8,9]
print(recursive_binary_search(numbers,9))  