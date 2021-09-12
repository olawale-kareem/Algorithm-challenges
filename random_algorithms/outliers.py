def find_outlier(integers):

    odd_arrays = []
    even_arrays = []

    for i in integers:
        if i % 2 == 0:
            even_arrays.append(i)
        else:
            odd_arrays.append(i)

    if len(even_arrays) > len(odd_arrays):
        return odd_arrays[0]
    else:
        return even_arrays[0]

print(find_outlier([2, 4, 6, 8, 10, 3]))