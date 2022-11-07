#!/usr/bin/python -tt
##   adapted in numerous ways by ITC to clarify instructions
##   adapted to Python3 for ITC - 17/10/18
##       - also added pep8 and naming convention compliance
##   instructions were changed to deal with proper handling of punctuation
##
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete.
    Depending on the flag provided by user on command line, it calls
    print_words() or print_top() functions which you will implement.

Tip: don't build the whole program at once. Get it to an intermediate
    milestone and print your data structure. When that's working, try for the next milestone.

1. For the --count flag, implement a print_words(filename) function that counts
    how often each word appears in the text and prints:
word1 count1
word2 count2
...

    - Print the above list in alphabetical order.
    - Store all the words as lowercase, so 'The' and 'the' count as the same word.
    - Hint: Use str.split() (no arguments) to split into words by whitespace.
    - Hint: Do not assume that the file exists, print an appropriate message

2. Improve print_words() to deal with punctuation so it's not included as part of the word.
    For example:
    Alice     Alice:     "Alice      Alice,    Alice"   are all the same word   >>>> alice
    BUT - In words like  Alice's   or   they're, the apostrophe is part of the word
        so don't split them into into    Alice + s    or   they  +  re

    Tip: don't look for an exact definition. There is no such word as "Alice:",
        so it make sense to turn it into "alice".
        But splitting Alice's by ' would create 2 words: "alice" and "s", and since "s" is
        not a word, and for simplicity reasons since we are not in NLP course, and not doing
        proper tokenizining, let's keep it simple, and leave "alice's" as one word.


3. For the --topcount flag, implement a print_top(filename) function similar
    to print_words() but which prints just the top 20 most common words (and their counts)
    sorted so the most common word is first, then the next most common, and so on.

    Tips:
    - Since print_words() and print_top() share similar functionality,
    please use functions and reuse code to prevent writing duplicated code.
    For example, in addition to  print_words(filename) and print_top(filename) functions,
    write additional functions that read a file, build a word/count dict and so on.

5. Make sure to write and submit tests for as much of your code and functions as possible.
    It's OK not to test 100% of your code
    (it's OK not to test input from command line and actually reading files),
    but try to reach a high percentage of testing of the rest of the code.

    Tip: you might need to restructure your functions further to reach a high level of test coverage
"""

import sys

# constants used for main()
REQUIRED_NUM_OF_ARGS = 3
ARG_OPTION = 1
ARG_FILE_NAME = 2

THINGS_TO_REMOVE = """
                    ('`-*#.,:;?!)"[]{}/\|$%#@^&~_1234567890
                    """

def read_file(filename):
    """
    Opens the file and returns its contents as a string. If it fails to open a file, returns empty string
    """
    # try:
    file = open(filename, "r")
    text = file.read()
    file.close()
    return text
    # except:
    #     print("File opening raised an exception")
    #     return ''

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

def count_words(text):
    """
    Takes the string and returns the dictionary containing words and their count
    """
    words = clean_words(text)
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count.update({word:1})
    return word_count

def print_words_count(words,number='all'):
    """
    printing function output in the format requested,
    word1 count1
    word2 count2
    ...
    up to number of lines
    """
    if number == 'all':
        number = len(words)
    i = 0
    for (word, count) in words:
        print(word," ",count)
        i += 1
        if i == number:
            break

def dictionary_sort(dict,sort=False):
    """
    Takes a dictionary and returns a list of tuples (key,value) sorted by value if sort == True
    """
    list = [(count, word) for word, count in dict.items()]
    if sort:
        list.sort(reverse=True)
    return [(word,count) for count,word in list]


def print_words(filename):
    """
    Reads a file and prints list of words that appear in the file,
    and frequences of their appearance, in alphabetical order
    """

    text = read_file(filename)
    if text == '':
        print("Failed to read the file or the file is empty")
        return False
    else:
        result_unsorted = count_words(text)
        result = dictionary_sort(result_unsorted)
    print_words_count(sorted(result))


def print_top(filename):
    """
    Reads a file and prints 20 most frequent words in the file, and frequences of their appearance
    """
    MAX_WORDS = 20
    text = read_file(filename)
    if text == '':
        print("Failed to read the file or the file is empty")
        return False
    else:
        result_dict = count_words(text)
        result = dictionary_sort(result_dict, sort=True)
    print_words_count(result,min(MAX_WORDS,len(result)))



def all_tests():
    TEST_TXT ='(Make the woRld, make) the world. The world, , world better place! the--the--place 04the make 3*& 56 the'
    TEST_DICT = {'make':3,'the':7,'world':4, 'better':1, 'place':2}
    result = dictionary_sort(TEST_DICT,sort=True)
    assert result == [('the',7),('world',4),('make',3),('place',2),('better',1)]
    assert clean_words('(Alice,') == ['alice']
    assert count_words(TEST_TXT) == TEST_DICT

# your code here

### DO NOT CHANGE FOLLOWING THIS LINE ###################

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    """
    Gets user input - file name and which option --count or --topcount
    Reads text file, counts and sorts words
    """

    if len(sys.argv) != REQUIRED_NUM_OF_ARGS:
        print("usage: ./wordcount.py {--count | --topcount} file")
        return

    option = sys.argv[ARG_OPTION]
    filename = sys.argv[ARG_FILE_NAME]
    if option == "--count":
        print_words(filename)
    elif option == "--topcount":
        print_top(filename)
    else:
        print("unknown option: " + option)


if __name__ == "__main__":
    all_tests()
    main()
