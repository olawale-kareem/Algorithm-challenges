
def duplicate_count(text):
    double_letters = []
    formatted_letter = text.lower()

    for letter in formatted_letter:
        letter_occurence = formatted_letter.count(letter)
        if letter_occurence > 1 and  letter not in double_letters:
            double_letters.append(letter)
    return len(double_letters)
print(duplicate_count("Indivisibilities"))
