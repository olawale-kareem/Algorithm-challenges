# def high_and_low(numbers):   
#     now = []
#     if '-' in numbers:
#         neg_num = numbers[numbers.index("-"):(numbers.index("-") + 2)]
#         neg_num_int = int(neg_num)
#         rem_num = numbers.replace(neg_num,'')
        
#         list_now = list(rem_num)
#         r_list = []
#         # eliminate space in-between the list
#         for num in list_now:
#             if num in '123456789':
#                 r_list.append(num)
        
#         # r_list = [for num in list_now]
        
#         r_list.append(neg_num_int)
#         array_now = [int(num) for num in r_list]
#         array_now.sort()
#         lowest_number = array_now[0]
#         highest_number = array_now[ len(array_now) - 1]
#         print (f'{highest_number} {lowest_number}')
        

    
    # for num in list_now:
    #     if num in [1,2,3,4,5,6,7,8,9]:
    #         now.append()
        
    # print(now)

    # print(neg_num,rem_num, list_now)
   
    # numbers_now = list(numbers)
    # print(numbers_now)
    # for nums in numbers_now:
    #     if nums == ' ':
    #      numbers_now.remove(nums)
    # numbers_now.sort()
    # lowest_number = numbers_now[0]
    # highest_number = numbers_now[ len(numbers_now) - 1]
    # print (f'{highest_number} {lowest_number}')



# high_and_low("1 -2 3 4 5") # "5 1"

# name = "1 9 3 4 -5"

# print(name[name.index("-"):(name.index("-") + 2)])
# for i in name:
#     print(i)

