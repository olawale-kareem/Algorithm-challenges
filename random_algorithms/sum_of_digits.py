
def digital_root(n):
    # convert to a str and then list
    new_list = list(str(n))
    # initiate a sum and loop to add
    sum = 0
    for  i in new_list:
        sum += int(i)
    useable_sum = str(sum)
    # make decision based on the usable sum
    if len(useable_sum) == 1:
        return sum
    else:
       return digital_root(sum)
           
print(digital_root(132189))