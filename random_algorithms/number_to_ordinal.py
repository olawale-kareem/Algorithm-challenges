def number_to_ordinal(number):

    number_form = str(number)
    number_form_list = list(number_form)
    max_index = len(number_form_list) - 1 
    last_number = number_form_list[max_index]
    p_last_number = number_form_list[max_index - 1]
  
    # suffixes

    suffix_1 = "st"
    suffix_2 = "nd"
    suffix_3 = "rd"
    suffix_4 = "th"

    if number == 0 :
        output_ordinal = number_form
        return output_ordinal
    if number == 1 :
        output_ordinal = number_form + suffix_1
        return output_ordinal
    else:
        # elif last_number == "1" and len(number_form) == 3:
        #     output_ordinal = number_form + suffix_1 
        if last_number == "1"  and len(number_form) > 2:
            output_ordinal = number_form + suffix_1
            return output_ordinal
        elif last_number == "2":
            output_ordinal = number_form + suffix_2
            return output_ordinal
        elif last_number == "3":
            output_ordinal = number_form + suffix_3
            return output_ordinal
        else:
            output_ordinal = number_form + suffix_4
            return output_ordinal

  
print(number_to_ordinal(0))
print(number_to_ordinal(1))
print(number_to_ordinal(2))
print(number_to_ordinal(3))
print(number_to_ordinal(4))
print(number_to_ordinal(5))
print(number_to_ordinal(6))
print(number_to_ordinal(7))
print(number_to_ordinal(8))
print(number_to_ordinal(9))
print(number_to_ordinal(10))
print(number_to_ordinal(11))
print(number_to_ordinal(22))
print(number_to_ordinal(121))
print(number_to_ordinal(123))
print(number_to_ordinal(142))


