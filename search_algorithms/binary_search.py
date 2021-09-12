def binary_search(arr, target):
    first_point = 0
    last_point = len(arr) - 1
    while first_point <= last_point:
        mid_point = (first_point + last_point) // 2
        # use mid_point to make decision
        if arr[mid_point] == target:
            return f"The index of the target number {target} is {mid_point}"
        elif arr[mid_point] < target:
            first_point = mid_point + 1
        else: 
            last_point = mid_point - 1
    return None

numbers = [1,2,3,4,5,6,7,8,9]
print(binary_search(numbers,7))  