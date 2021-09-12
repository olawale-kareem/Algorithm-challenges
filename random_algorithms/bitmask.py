def high_order_bitmask(word_size):
    binary_now = bin(word_size)
    

    if len(binary_now) <= 4:
        number_equivalent = int(binary_now, 2)
        print (number_equivalent)
    else:
        new_binary_now = binary_now.replace('b','0')
        binary_output_1 = new_binary_now[:4]
        binary_output_2 = new_binary_now[4:]
        now_binary = binary_output_2.replace('0','1')
        total_binary = binary_output_1+ now_binary

        print(binary_output_1)
        # print(total_binary)

        # print( bin(12))

        # for num in range(len(binary_output_1)):
        #     if num > binary_output_1.index('1') or binary_output_1[num] == '0':
        #         mk = binary_output_1.replace(binary_output_1[num], '1')

        # print(mk)


        print(binary_output_2)
        bit_list = list(binary_output_2)
        print(bit_list)
        for nums in bit_list:
            if nums == '0':
                bit_list.remove(nums)
                bit_list.append('1')
            elif nums == '1' :
                bit_list.remove(nums)
                bit_list.append('0')
        
        print(bit_list)


        # total = operation_factor + binary_output_2
        # print(total)

        print(new_binary_now,binary_output_1,binary_output_2 )



        binary_output_1 = new_binary_now[:4]
        operation_factor = '0' * len(binary_now)

        operation_factor = '0' * len(binary_now)
        number_equivalent = int(operation_factor,2)
        result = binary_now and bin(number_equivalent)
        print(new_binary_now, operation_factor, number_equivalent, result, int(result, 2))
        

    print(binary_now)
    print(int(binary_now,2))
    print(int(binary_now.replace('b',"0"),2))



high_order_bitmask(2) #2
high_order_bitmask(4)
high_order_bitmask(8)