""" This program has been adapted for use by GVAHIM
       - the main revisions regard pep8 compliance and use of variable names
Copyright 2010 Google Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0

Google's Python Class
http://code.google.com/edu/languages/google-python-class/

Additional basic string exercises  """


# E. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(my_inputs):
    """
    Takes a string as an input and, provided ut is more than 3 characters long,
    suppliments it with 'ing' at the end, or, if it finishes with 'ing' already,
    supplements it with 'ly'
    """
    if not type(my_inputs) is str:
        raise TypeError("Wrong type of argument, should be string")
    length = len(my_inputs)
    if length > 3:
        try:
            my_inputs.index('ing', length-3)
            return my_inputs + 'ly'
        except:
            return my_inputs + 'ing'
    else:
        return my_inputs


# F. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(my_input):
    """
    Takes a string containing a phrase as an input
    and replaces the first 'not ... bad' expression (if found) with 'good'
    """
    if not type(my_input) is str:
        raise TypeError("Wrong type of argument, should be string")
    try:
        first_not = my_input.index('not')
    except:
        return my_input #if not found, returning the string unchanged
    try:
        first_bad = my_input.index('bad', first_not) # looking for the first 'bad' after the first 'not'
    except:
        return my_input #if not found, returning the string unchanged
    return my_input[:first_not] + 'good' + my_input[first_bad + 3 :]


# G. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, input1 and input2, return a string of the form
#  input1-front + input2-front + input1-back + input2-back

def get_string_divider(string):
    return len(string) // 2 + len(string) % 2

def front_back(input1, input2):
    """
    :param input1: a string
    :param input2: a string
    Splits both strings in the middle and reconnects them in the following order:
    input1 first half + input2 first half + input1 second half + input2 second half
    """
    if not (type(input1) and type(input2)) is str:
        raise TypeError("Wrong type of argument, should be string")
    divider_1 = get_string_divider(input1)
    divider_2 = get_string_divider(input2)
    return input1[:divider_1] + input2[:divider_2] + input1[divider_1:] + input2[divider_2:]


# WARNING: Do not change this function!!!
def test(got, expected):
    """ simple test() function used in main() to print
        what each function returns vs. what it's supposed to return. """

    if got == expected:
        prefix = " OK "
    else:
        prefix = "  X "
    print("%s got: %s expected: %s" % (prefix, repr(got), repr(expected)))


# WARNING: Do not change this function!!!
def main():
    """ main() calls the above functions with interesting inputs,
        using test() to check if each result is correct or not. """

    print("\nverbing")
    test(verbing("hail"), "hailing")
    test(verbing("swiming"), "swimingly")
    test(verbing("do"), "do")

    print("\nnot_bad")
    test(not_bad("This movie is not so bad"), "This movie is good")
    test(not_bad("This dinner is not that bad!"), "This dinner is good!")
    test(not_bad("This tea is not hot"), "This tea is not hot")
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print("\nfront_back")
    test(front_back("abcd", "xy"), "abxcdy")
    test(front_back("abcde", "xyz"), "abcxydez")
    test(front_back("Kitten", "Donut"), "KitDontenut")


# WARNING: Do not change this function!!!
if __name__ == "__main__":
    main()
