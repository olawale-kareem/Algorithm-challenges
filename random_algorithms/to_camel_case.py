def to_camel_case(text):
    #your code here
    text1 = text.lower()
    letters = ""

    for letter in text1:
        if letter == "-" or letter == "_":
            next_letter_index = text1.index(letter)+ 1
            text1.replace(text1[next_letter_index],text1[next_letter_index].upper())

        letters += letter
                       
    return letters 


name ="The_stealth_warrior"

print(to_camel_case(name))