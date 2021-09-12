def duplicate_encode(word):

    new_word = word.lower()
    new_word_list = list(new_word)
    output_word =""
    
    for letter in new_word_list:
        text_count = new_word_list.count(letter)
        if text_count > 1:
            output_word += ")"
        else:
            output_word += "("

    return output_word

print(duplicate_encode("Success")) # "Success"  =>  ")())())"
