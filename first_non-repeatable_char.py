'''Write a programm that outputs the first non-repeatable character on a string. '''


count = {}
    for c in word:
        if c not in count:
            count[c] = 0
        count[c] += 1
    for c in word:
        if count[c] == 1:
            return c
            break