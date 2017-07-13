"""Generate insults. Also demo of how to read from a csv file."""

# raspberrypi.org/learning/shakespearean-insult-generator/worksheet/

import random
from guizero import App, Text, PushButton


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


def get_content():
    """Output the entire file."""
    with open('insults.csv', 'r') as f:
        contents = f.read()
        print(contents)


def insult_me():
    """Make an insult."""
    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)

    insult = 'Thou %s %s %s!' % (word_a, word_b, word_c)
    return insult


def new_insult():
    """Make a new insult."""
    new_insult = insult_me()
    message.set(new_insult)


app_title = 'Shakespearean Insult Generator'

# documentation at https://lawsie.github.io/guizero/text/
app = App(app_title, width=600, height=200)

message = Text(app, text=insult_me(), size=20)

button = PushButton(app, new_insult, text='Insult me again')

app.display()
