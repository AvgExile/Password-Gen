import random


def shuffle(string):
    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)


# Random Letter Generation
uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))
uppercaseLetter3 = chr(random.randint(65, 90))
lowercaseLetter1 = chr(random.randint(97, 122))
lowercaseLetter2 = chr(random.randint(97, 122))
lowercaseLetter3 = chr(random.randint(97, 122))
digit1 = chr(random.randint(49, 57))
digit2 = chr(random.randint(49, 57))
digit3 = chr(random.randint(49, 57))
PunctuationSign1 = chr(random.randint(33, 64))
PunctuationSign2 = chr(random.randint(33, 64))
PunctuationSign3 = chr(random.randint(33, 64))


# Generate the Characters, in random order.
password = (uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 +
            lowercaseLetter2 + digit1 + digit2 + PunctuationSign1 + PunctuationSign2)
password = shuffle(password)

# output
print(password)
