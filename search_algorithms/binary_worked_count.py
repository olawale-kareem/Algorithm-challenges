# worked_count
# binary search 

def binary_search(array, target_number):
    # sort the array
    array.sort()

    # get the starting point and the end_point
    start_point = 0
    end_point = len(array)  -1

    # this is a copy of the end_point just so the number is not in the list 
    end_point_final = end_point

    # make decision based on the start_point and end_point

    while start_point <= end_point:

        # get the midpoint of the array

        mid_point = (start_point + end_point) // 2

        # make decision based on the mid_point

        if array[mid_point] == target_number:

            # get the final array form when the target number was found
            final_count_start = array[start_point]
            final_count_end = array[end_point]
            # final array
            final_array = array[array.index(final_count_start): array.index(final_count_end) + 1]
            # the total number of iterations taken to get the number
            count = (end_point // len(final_array)) 
            # return count_end, count_start, final_array
            return {"index": mid_point, "count": count }

        elif array[mid_point] > target_number:
            end_point = mid_point - 1
        else:
            start_point = mid_point + 1

        
    formatted_index = -1
    count_not_found = end_point_final // 2
    return {"index": formatted_index, "count": count_not_found }



array_1 = [0,5,10,15,20,22,30,35,40]
target_1 = 15

array_2 = [0,5,10,15,20,22,30,35,40]
target_2 = 11

array_3 = [0,5,10,15,20,22,30,35,40]
target_3 = 40

array_4 = [0,5,10,15,20,22,30,35,40]
target_4 = 0

print(binary_search(array_1,target_1))
print(binary_search(array_2,target_2))
print(binary_search(array_3,target_3))
print(binary_search(array_4,target_4))