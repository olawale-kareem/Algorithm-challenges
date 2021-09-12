
def pack_array(array):
    
    # initialise a count 
    count = 0
    # initialise an empty array
    output_array = []

    def even_loop(array):
        output_array = []
        for i in range(len(array)):
            if i == 0 or i % 2 == 0:
                average_num = array[i] + array[i + 1]
                output_array.append(average_num)
            
        return output_array

    def odd_loop(array):
        output_array_2 = []

        for i in range(len(array)):
            if i == 0 or i % 2 == 0:
                average_num = array[i] * array[i + 1]
                output_array_2.append(average_num)
        
        return output_array_2

    result = even_loop(array)

    while len(result) != 1 :
        result = odd_loop(result)
        count += 1
        if len(result) > 1 and count % 2 != 0 :
            result = even_loop(result)
        elif len(result) > 1 and count % 2 == 0:
            result = odd_loop(result)
        else:
            break
    
    # format the display
    return result[0]  

array = [1,2,3,4,5,6,7,8]
print(pack_array(array))