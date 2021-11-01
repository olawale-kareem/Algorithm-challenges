
def split(lst):
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    return left, right

def merge(left, right) :
    l = []; i = 0;  j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    while i < len(left): 
        l.append(left[i])
        i+=1   
    while j < len(right): 
        l.append(right[j])
        j+=1   

    return l
  
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  
    left_half, right_half = split(arr)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)
    
def verify_sorted(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True
    return arr[0] < arr[1] and verify_sorted(arr[1:])

a_list = [54, 62, 93, 17, 77, 31, 44, 55, 20]


print(merge_sort(a_list))
a = merge_sort(a_list)
print(verify_sorted(a))


