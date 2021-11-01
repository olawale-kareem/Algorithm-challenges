# Morse Code
# Overview
# Morse Code is delivered in a series signals which are referred to as dashes (-) or dots (.). To keep things simple for the purposes of this challenge we'll only decode letters with a maximum length of three signals.

# Morse Code Graph

# Here is the Morse Code dichotomic search table courtesy of Wikipedia

# Morse Code Examples
# -.- translates to K
# ... translates to S
# .- translates to A
# -- translates to M
# . translates to E

# Background
# You've started work as morse code translator. Unfortunately some of the signals aren't as distinguishable as others and there are times where a . seems indistinguishable from -. In these cases you write down a ? so that you can figure out what all the posibilities of that letter for that word are later.

# Task
# Write a function possibilities that will take a string signals and return an array of possible characters that the Morse code signals could represent.

# Specification
# possibilities(signals)
# Parameters
# signals: String - The Morse code signals that needs to be parsed. The may contain one or more unknown signals (?).

# Return Value
# Array (of Strings) - The list of possible letters for the given group of signals. Letters will always be ordered from how they appear on the chart, from left to right.

# Constraints
# There will be no more than 3 characters within signals.

# 0 - 3 unknown signals may be given.

# Examples
# signals	Return Value
# "."	["E"]
# "-"	["T"]
# "-."	["N"]
# "..."	["S"]
# "..-"	["U"]
# "?"	["E","T"]
# ".?"	["I","A"]
# "?-?"	["R","W","G","O"]



#

def possibilities(signals):
    dict_morse = {
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    1:'.----',
    2:'..---',
    3:'...--',
    4:'....-',
    5:'.....',
    6:'-....',
    7:'--...',
    8:'---..',
    9:'----.',
    0:'-----',
  }

    morse_keys = list(dict_morse.keys())
    morse_signals = list(dict_morse.values())
    sample_confusion =  '?'
  
    # general case
    if sample_confusion not in signals:
        pos_array = []
        signal_idx = morse_signals.index(signals)
        key = morse_keys[signal_idx]
        pos_array.append(key)
        return pos_array

    else:
        if signals == sample_confusion:
            signals_idx = [ ]
            for i in morse_signals:
                if i == '.' or i == '-':
                    signals_idx.append(morse_signals.index(i))
            required_keys = [ morse_keys[i] for i in signals_idx]
            return required_keys
        
        if len(signals) == 2 and sample_confusion in signals:
            
            # back
            if signals[-1] == '?':
                samples = [f'{signals[0]}' + '.', f'{signals[0]}' + '-']
                sample_idx = [ morse_signals.index(i) for i in samples]
                required_keys = [ morse_keys[i] for i in sample_idx]
                return required_keys
            
            # front
            samples = [f'{signals[1]}' + '.', f'{signals[1]}' + '-']
            sample_idx = [ morse_signals.index(i) for i in samples]
            required_keys = [ morse_keys[i] for i in sample_idx]
            return required_keys
        
        if len(signals) == 3 and sample_confusion in signals:
            sig_list = list(signals)
            for i in range(len(sig_list)):
                if sig_list[i] == '?':
                    sig_list[i] = ['.','-']
            
            for i in sig_list:
                if len(i) == 1:
                   sig_list[sig_list.index(i)] = [i,i]
            
            for i in sig_list:
                if sig_list.index(i) == 0:
                    for j in i:
                        pass
                break

            



            

           
  
                    

 
            




           
      

            
 


# print(possibilities('.'))
# print(possibilities('-'))
# print(possibilities('-.'))
# print(possibilities('...'))
# print(possibilities('..-'))

# print(possibilities('?'))
# print(possibilities('.?'))
print(possibilities('?-?'))
  



# "?"	["E","T"]
# ".?"	["I","A"]      .- or ..
# "?-?"	["R","W","G","O"]



#   ? : CONTAINS ONLY . OR -
#   .? : CONTAINS ONLY . added to ?
#    ?-?: contains  ? + - + ?
# "-"	["T"]
# "-."	["N"]
# "..."	["S"]
# "..-"	["U"]