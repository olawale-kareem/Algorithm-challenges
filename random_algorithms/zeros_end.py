# move zeros to the end
def move_zeros(array):
    for number in array:
        if number == 0:
            array.remove(number)
            array.append(number)
    
    return array
   
print(move_zeros([1,0,1,2,0,1,3]))