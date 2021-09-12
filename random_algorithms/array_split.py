def array_split(arr):   
    output = []
    for i in range(0,len(arr),2):
        output.append(arr[i:i+2])  
    return output

print(array_split([1,2,3,4,5,6,7,8,9,10]))