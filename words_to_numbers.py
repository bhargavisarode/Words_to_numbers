'''You have a string which contains a number represented as English text. Your task is to translate these numbers into their integer representation. The numbers can range from -999,999,999 to 999,999,999. The following is an exhaustive list of English words that your program must account for:

negative,
zero, one, two, three, four, five, six, seven, eight, nine,
ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen,
twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety,
hundred,
thousand,
million

Είσοδος:
Your program should read lines from standard input. Each line contains an English of a number.
Negative numbers will be preceded by the word, "negative".
The word "hundred" is not used when "thousand" could be. E.g. 1500 is written "one thousand five hundred", not "fifteen hundred".
Έξοδος:
Print the decimal representation of the number.
'''


lines = ['five\n', 'fifty one\n', 'one hundred ninety\n', 'one hubred one\n', 'one million two\n', 'negative six hundred twenty four\n', 'two hundred\n', 'one hundred two\n', 'one hundred twenty\n', 'one\n', 'negative ten\n', 'ninety one\n', 'negative twenty one\n', 'one hundred\n', 'seven\n', 'twenty\n', 'twenty five\n', 'negative thirty\n', 'three million\n', 'three hundred twenty\n', 'three hundred forty five\n', 'negative eight hundred\n', 'eight thousand\n', 'negative eight thousand\n', 'negative nine thousand three hundred ninety two\n' ]

# initialize words and numbers dict
word_numbers_dict = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000
}

# prepare data function
def prepare_data(line):
        ''' Prepares the data. '''
        # remove \n at the end
        line = line.rstrip()
        # string into seperate word strings
        line_words = line.split(' ')
        #remove negative word
        if line_words[0] == 'negative':
            print_number.append('-')
            line_words.pop(0)
        return line_words

# find the one word numbers
def one_word_nums(line_words):
        ''' Finds the numbers of the one-word numbers.'''
        if len(line_words) == 1:
            # 1 to 19, 20, 30, 40, ...
            if line_words[0] in word_numbers_dict:
                print_number.append(str(word_numbers_dict[line_words[0]]))

# find the two word numbers
def two_word_nums(line_words):
    ''' Finds the numbers of the two-word numbers. '''
    if len(line_words) == 2:
        # 100, 200, 300...
        if line_words[1] == 'hundred':
            print_number.append(str(word_numbers_dict[line_words[0]]) + '00')
        # 1000, 2000, 3000...
        elif line_words[1] == 'thousand':
            print_number.append(str(word_numbers_dict[line_words[0]]) + '000')
        # 1000000, 2000000, 3000000...
        elif line_words[1] == 'million':
            print_number.append(str(word_numbers_dict[line_words[0]]) + '000000')
        # rest of two word numbers, 21, 56, 89...
        else:
            print_number.append((str(word_numbers_dict[line_words[0]])[0] + str(word_numbers_dict[line_words[1]])))

# find the three word numbers
def three_word_numbers(line_words):
    ''' Finds the numbers of the three-word numbers.'''
    if len(line_words) == 3:
        print_number.append(str(word_numbers_dict[line_words[0]]))
        if line_words[-1] in [k for (k,v) in word_numbers_dict.items() if v > 0 and v <= 9]:
            # 102, 209, 705...
            if line_words[1] == 'hundred':
                print_number.append('0' + (str(word_numbers_dict[line_words[-1]])))
            # 2005, 6009...
            elif line_words[1] == 'thousand':
                print_number.append('00' + (str(word_numbers_dict[line_words[-1]])))
            # 100004, 500009...
            elif line_words[1] == 'million':
                print_number.append('0000' + (str(word_numbers_dict[line_words[-1]])))
        # 140, 620, 870...
        elif line_words[-1] in [k for (k,v) in word_numbers_dict.items() if (v > 9 and v <= 20)
        or (v == 30 or v == 40 or v == 50 or v == 60 or v == 70 or v == 80 or v == 90)]:
            print_number.append(str(word_numbers_dict[line_words[-1]]))

# find the four word numbers
def four_word_nums(line_words):
    ''' Finds the four-word numbers (the rest of three digit numbers, like 146, 624, 999...). '''
    if len(line_words) == 4:
        #146, 624, 999...
        if line_words[1] == 'hundred':
            print_number.append(str(word_numbers_dict[line_words[0]])[0] + str(word_numbers_dict[line_words[2]])[0] + str(word_numbers_dict[line_words[3]])) 
        if line_words[1] == 'thousand':
            print_number.append(str(word_numbers_dict[line_words[0]])[0]+'0'+ str(word_numbers_dict[line_words[2]])[0] + str(word_numbers_dict[line_words[3]]))
for line in lines:
    # list containing the string for each digit of the final number that will be printed
    print_number = []

    # turns the string into a list of string, each containing one word for a number
    line_words = prepare_data(line)

    # deals with one-word numbers
    one_word_nums(line_words)

    # deals with two-word numbers
    two_word_nums(line_words)

    # deals with three-word numbers
    three_word_numbers(line_words)
    
    # deals with four-word numbers (the rest of three digit numbers)
    four_word_nums(line_words)   

    #print the final number
    print(''.join(print_number))


"""    
    # four word numbers: 638, 978, 618...
    if len(line_words) == 4:
"""

    

