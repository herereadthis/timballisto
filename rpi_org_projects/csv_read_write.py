# https://www.raspberrypi.org/learning/shakespearean-insult-generator/worksheet/

import random

"""
output the entire file
with open('insults.csv', 'r') as f:
    contents = f.read()
    print(contents)
"""

list_a = []
list_b = []
list_c = []

with open('insults.csv', 'r') as f:
    # loop through each line
    for line in f:
        # terms in .CSV file are split by commas
        words = line.split(',')
        list_a.append(words[0])
        list_b.append(words[1])
        # each row is 3 items; a newline occurs after 3rd term
        # have to remove that new line by stripping whitespace
        list_c.append(words[2].strip())


def insult_me():
    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)
    # insult = 'Thou' + word_a + word_b + word_b
    insult = 'Thou %s %s %s!' % (word_a, word_b, word_c)
    print(insult)

insult_me()
