name = [[1,2,3], [5,6,7], [8,9,10]]
# 1
# get each array
for i in name:
    print (i)

# 2
# get each sub element
first_ele = []
second_ele = []
third_ele = []

for i in name:
    for  j in range(len(i)):
        if j == 0:
            first_ele.append(i[j])
        if j == 1:
            second_ele.append(i[j])
        if j == 2:
            third_ele.append(i[j])

print( first_ele, second_ele, third_ele)


# you can use the above logic to get all you need from all the arrays

# 3
name_2 = [[[1,2,3],[4,5,6]], [7,8,9], [10,11,12]]
first_ele = []
second_ele = []
third_ele = []

for i in name_2:
    if name_2.index(i) == 0:
        for j in i:
            for k in range(len(j)):
                if k == 0:
                    first_ele.append(j[k])
                if k == 1:
                    second_ele.append(j[k])
                if k == 2:
                    third_ele.append(j[k])
    else:
        for j in range(len(i)):
            if j == 0:
                first_ele.append(i[j])
            if j == 1:
                second_ele.append(i[j])
            if j == 2:
                third_ele.append(i[j])    

print( first_ele, second_ele, third_ele)        


