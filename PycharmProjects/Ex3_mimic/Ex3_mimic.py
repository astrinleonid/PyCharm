#!/usr/bin/python -tt
##   adapted to Python3 for ITC - 17/10/18
##       - also added pep8 and naming convention compliance
##
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

No need to submit tests, but make sure you try your code on numerous files and that it works.
"""

import random
import sys

NUMBER_OF_ARGS = 2
FILE_NAME = 1

THINGS_TO_REMOVE = """
                    ('`-*#.,:;?!)"[]{}/\|$%#@^&~_1234567890
                    """

def clean_words(text_to_clean):
    """
    Takes a string.
    Makes all words lowercase and cleans them from punctuation signs and returns a list of words
    """
    text_dashes_replaced = text_to_clean.replace("--"," ")
    # text_dashes_replaced = text_to_clean
    text = text_dashes_replaced.split()
    clean_text = []
    for  word in text:
        word_cleaned = word.lower().strip(THINGS_TO_REMOVE)
        if len(word_cleaned) > 0:
            clean_text.append(word_cleaned)
    return clean_text

def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    dict = {}
    file = open(filename,"r")
    text = file.read()
    file.close()

    all_words = clean_words(text)
    dict.update({"": [all_words[0]]})

    for i, word in enumerate(all_words):
        if i ==  len(all_words) - 1:
            break
        if not word in dict.keys():
            dict.update({word:[]})
        dict[word].append(all_words[i+1])

    return dict

def cut_the_text(text):
    """
    Cuts the text into strings no more than 70 char long
    """
    MAX_LEN = 70
    strings =[]
    while len(text) > MAX_LEN:
        space_index = text.rfind(" ",0,70)
        strings.append(text[:space_index])
        text = text[space_index:]
    return strings



def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    mimic_text = ""
    for i in range(200):
        mimic_text += " "
        if word == "i":
            mimic_text += "I"
        else:
            mimic_text += word
        next_word = random.choice(mimic_dict[word])
        word = next_word

    mimic_text_strings = cut_the_text(mimic_text)
    for line in mimic_text_strings:
        print(line)

def test():
    filename = '/Users/leonidastrin/myrepo/ex2-alice.txt'
    print_mimic(mimic_dict(filename), "i")

def main():
    """ Provided main(), calls mimic_dict() and mimic() """
    if len(sys.argv) != NUMBER_OF_ARGS:
        print("usage: ./mimic.py file-to-read")
        sys.exit(1)

    my_dict = mimic_dict(sys.argv[FILE_NAME])
    print_mimic(my_dict, "")


if __name__ == "__main__":
    main()
    # test()
