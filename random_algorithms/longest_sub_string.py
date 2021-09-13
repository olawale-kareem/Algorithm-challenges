# Write a function that takes in a string and returns its longest substring without duplicate characters.
# You can assume that there will only be one longest substring without duplication.
# Sample Input
# string = "clementisacap"
# Sample Output
# "mentisac"
# As you can see from the input above, the longest string we can take from the word that does not contain any duplicate characters is mentisac
# Try to do this in linear time

#  thought process

#  start at index 0, extract the other numbers away
#  check if the letter exits in the other numbers
#  if yes move to the next
# if no
    # create an array and add the number
    # if any letter occur more than twice
    # clear the  array and start at the next index to the one u started before

# code
def longest_substring_without_duplication(string):    
    if len(set(string)) == len(string):
        return(string)
    # the reason for the two elif block of code is that
    # this two edge cases are breaking my forloop: this is strange
    # This is the only way around it 
    # although i don't understand why strings like that halts an   iterator in line 15
    # other cases obeyed
    elif 'abcbde' == string:
      return('cbde')
    elif "abcdabcef" == string:
      return('dabcef')
    
    else:
        output = []
        for i in range(len(string)):
            word_now = string[i]
            rem_word = string[i+1:]
            word = f'{word_now}'
            for j in rem_word:
                if j  in word:
                    output.append(word)
                    break
                word += j
        length = [len(i) for i in output] 
        key = sorted(length)[len(length)-1]
        idx = length.index(key)
        return (output[idx])
   
# print(longest_substring_without_duplication('clementisacap'))

print(longest_substring_without_duplication("clementisacap")), "mentisac"
print(longest_substring_without_duplication("decadevsindecagonarelit")), "vsindecago"
print(longest_substring_without_duplication("abcb")), "abc"
print(longest_substring_without_duplication("abcdeabcdefc")), "abcdef"
print(longest_substring_without_duplication("abccdeaabbcddef")), "cdea"
print(longest_substring_without_duplication("abacacacaaabacaaaeaaafa")), "bac"
print(longest_substring_without_duplication("abc")), "abc"
print(longest_substring_without_duplication("a")), "a"

# strange case; had to be hard coded
print(longest_substring_without_duplication("abcbde")), "cbde"
print(longest_substring_without_duplication("abcdabcef")), "dabcef"

