    def is_prime(num):
    
    # declare a small list of known prime number
    # check if num in the small list , return True if yes
    # use this small list to compare other input 

    list_of_known_prime = [2,3]

    if num == 1 or num <= 0:
        return False
    elif num in list_of_known_prime:
        return True
    else:
        # check for divisiblity by previous number
        for known_prime in list_of_known_prime:
            if num % known_prime  == 0:
                return False

        
    return True


print(is_prime(5))
print(is_prime(11))
print(is_prime(73))
print(is_prime(120))