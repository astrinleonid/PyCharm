""" This program has been adapted for use by GVAHIM
       - the main revisions regard pep8 compliance and use of variable names

Copyright 2010 Google Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0

Google's Python Class
http://code.google.com/edu/languages/google-python-class/

Additional basic list exercises """


# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    new_nums = []
    previous_number = None
    for number in nums:
        if not number == previous_number:
            new_nums.append(number)
        previous_number = number
    return new_nums


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
#
# NOTE - DO NOT use return sorted(sorted1 + sorted2) - that's too easy :-)
#
def linear_merge(sorted1, sorted2):

    iterated1 = iter(sorted1)
    iterated2 = iter(sorted2)

    merged = []

    value1 = next(iterated1)
    value2 = next(iterated2)

    while True: #comparing and adding the values untill one of the lists is exsausted
        if value1 > value2:
            merged.append(value2)
            try:
                value2 = next(iterated2)
            except:
                merged.append(value1)
                break
        else:
            merged.append(value1)
            try:
                value1 = next(iterated1)
            except:
                merged.append(value2)
                break

    while True:  #appending a "tail" of the first list (if exists)
        try:
            merged.append(next(iterated1))
        except:
            break

    while True: #appending a "tail" of the second list (if exists)
        try:
            merged.append(next(iterated2))
        except:
            break

    return merged


# WARNING: DO NOT CHANGE OR DELETE THE FOLLOWING CODE:
def test(got, expected):
    """ simple test() function used in main() to print
        what each function returns vs. what it's supposed to return. """
    if got == expected:
        prefix = " OK "
    else:
        prefix = "  X "
    print("%s got: %s expected: %s" % (prefix, repr(got), repr(expected)))


# WARNING: DO NOT CHANGE OR DELETE THE FOLLOWING CODE:
def main():
    """ main() calls the above functions with interesting inputs,
        using test() to check if each result is correct or not. """

    print("\nremove_adjacent")
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print("\nlinear_merge")
    test(linear_merge(["aa", "xx", "zz"], ["bb", "cc"]), ["aa", "bb", "cc", "xx", "zz"])
    test(linear_merge(["aa", "xx"], ["bb", "cc", "zz"]), ["aa", "bb", "cc", "xx", "zz"])
    test(linear_merge(["aa", "aa"], ["aa", "bb", "bb"]), ["aa", "aa", "aa", "bb", "bb"])


# WARNING: DO NOT CHANGE OR DELETE THE FOLLOWING CODE:
if __name__ == "__main__":
    main()
