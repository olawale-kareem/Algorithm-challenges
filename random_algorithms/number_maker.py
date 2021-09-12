def number_maker(num):
    num_f = str(num)
    output = ""
    count = len(num_f)
    
    for num in range(len(num_f)+1):
        if count != 0:
            f_out = num_f[num] + ("0" * (count - 1))
            count -= 1
            output += f" {f_out}"
        else:
            f_out = num_f[num - 1]
            output += f" {f_out}"

    return output


print(number_maker(3450786))