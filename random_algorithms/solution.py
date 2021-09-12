def solution(string,markers):
    
    # thought process
    # remove all element after the first marker into an array, this step gives two array
    # remove all element that has /n prefix alone
    # finally join the other arrays together.

    test_array = string
    second_array = []
    
    marker_1_index = test_array.index(markers[0]) 
    new_array = test_array.split(test_array[marker_1_index]) 
    
    first_array =  new_array[0].strip()
   
    
    second_array = markers[0] + new_array[1]

    marker_2_index = second_array.index(markers[1])
    new_array_2 = second_array.split(second_array[marker_2_index]) 
    new_array_2[1] = markers[1] + new_array_2[1]

    new_line_char = '\n'
    new_line_words = []

    for word in new_array_2:
        if new_line_char in word:
            new_line_words.append(word)

    
    new_line_words_now = ''.join(new_line_words)
    new_line_words_now_extras = new_line_words_now[new_line_words_now.index('\n'):]

    final_word = first_array + new_line_words_now_extras
    return final_word.strip()
    
    
print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])) # "apples, pears\ngrapes\nbananas"
solution("a #b\nc\nd $e f g", ["#", "$"]) # "a\nc\nd"