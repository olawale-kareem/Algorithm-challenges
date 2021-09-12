# the pangram algorithm
# a pangram is a sentence that contains all letters of the english alphabet

# solution 1
# if you can import a string
import string
def is_pangram(s):   
    # generates all the alphabets a-z in lowercase
    word_bank = string.ascii_lowercase
    sentence = s.lower()  
    # loop through to find which word of the alphabet is not in the sentence
    # if found break out of the loop and return false
    for letter in word_bank:
        if letter  not in sentence:
            return False        
    return True


# solution 2
# if you can't import a string

def is_pangram(s):   
    # generates all the alphabets a-z in lowercase
    word_bank = 'abcdefghijklmnopqrstuvwxyz'
    sentence = s.lower()  
    # loop through to find which word of the alphabet is not in the sentence
    # if found break out of the loop and return false
    for letter in word_bank:
        if letter  not in sentence:
            return False        
    return True

