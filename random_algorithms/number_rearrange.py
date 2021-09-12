def number_rearrange(arr):
    # this algorithm rearranges the odd numbers alone in a list
    # seperate the odd numbers out and replace with a "#"
    odd_numbers = []
    copy_arr = arr.copy()
    for number in arr:
        if number % 2 == 1:
            copy_arr[copy_arr.index(number)] = "#"
            odd_numbers.append(number)
   

    # sort the odd_numbers array
    odd_numbers.sort()
    # add to the sorted odd_num array to the other using index method 
    for num in odd_numbers:
       copy_arr[ copy_arr.index("#") ] = num

    return copy_arr
    
test_1 = [9,8,7,6,5,4,3,2,1,0]
test_2 = [7,1]
test_3 = [5,8,6,3,4]

print(number_rearrange(test_1))
print(number_rearrange(test_2))
print(number_rearrange(test_3))