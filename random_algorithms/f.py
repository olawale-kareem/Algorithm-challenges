def calc(n,k):
    if 'times' in str(k):
        output = n * k
    if 'plus' in str(k):
        output = n + k
    if 'minus' in str(k):
        output = n - k
    else: 
        output = n // k
    return output


def zero(s=None):
    if s == None:
        return 0
    else:
        return calc(0,s)
def one(s=None):
    if s == None:
        return 1
    else:
        return calc(1,s)
             
def two(s=None):   
    if s == None:
        return 2
    else:
        return calc(2,s)
    
def three(s=None):
    if s == None:
        return 3
    else:
        return calc(3,s)
        
def four(s=None):
    if s == None:
        return 4
    else:
        return calc(4,s)

def five(s=None):
    if s == None:
        return 5
    else:
        return calc(5,s)
        
def six(s=None):
    if s == None:
        return 6
    else:
        return calc(6,s)
        
def seven(s=None):
    if s == None:
        return 7
    else:
        return calc(7,s)
        
def eight(s=None):
    if s == None:
        return 8
    else:
        return calc(8,s)
        
def nine(s=None):
    if s == None:
        return 9
    else:
        return calc(9,s)    

def plus(s): 
    return s
def minus(s):
    return s
def times(s):
    return s
def divided_by(s):
    return s