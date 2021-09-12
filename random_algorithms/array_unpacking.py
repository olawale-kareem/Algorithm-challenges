def array_packing(integers):

    output_array = []

    for number in integers:
        binary_number = bin(number)
        formatted_binary_number = binary_number.replace("b", "0")
        # int_binary_num = int(formatted_binary_number)
        output_array.append(formatted_binary_number)

    # return output_array
    output = [output_array[2],output_array[1],output_array[0] ]

    sum = ""

    for bin_num in output:
        sum += bin_num

    int_sum = int(sum, 2)
    return (21784/ int_sum)

 

print(array_packing([24,85,0]))

print(array_packing([24,85,0]))