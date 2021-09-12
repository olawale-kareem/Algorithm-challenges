def laptoprentals(times):    
    if len(times) == 1 and times[0] == []:
        return 0
    elif len(times) == 1 and times[0][0] == 0:
        return 1
    elif len(times) == 1 and times[0][0] != 0:
        return times[0][0]
    else:
        extra_laptop = 0
        start_times = [ i[0] for i in times]
        for i in start_times:
            if start_times.count(i) > 1:
                extra_laptop += start_times.count(i)
                break
        
        if extra_laptop != 0:
            total__laptop = 1 + extra_laptop
            return total__laptop
        else:
            return 1
    

print(laptoprentals([[0,2],[1,4],[4,6],[0,4],[7,8],[9,11],[3,10]])) # 3
print(laptoprentals([[0,4],[2,3],[2,3],[2,3]])) # 4
print(laptoprentals([[1,5],[5,6],[6,7],[7,9]])) # 1
print(laptoprentals([[0,4]])) #
print(laptoprentals([[]]))  # 0