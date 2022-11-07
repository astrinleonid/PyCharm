import sys

def replace_single(position, string, replacement):
    """
    :param position: position to replace character at
    :param string: string to replace character in
    :param replacement: replacement character
    :return: string with a character replaced
    """
    if position >= 0 and position < len(string):
        return string[:position] + replacement + string[position+1:]
    else:
        raise ValueError("index for the string " + string + " is out of range")



def replacer(params):

    """
    :param params: param1 is a number of lines to handle, after params are coming in the groups of 3:
    position to replace character at, string to replace character in, replacement character
    :return: list of lines with characters replaced
    """


    try:
        num_lines = int(params[0])
    except ValueError as er:
        raise ValueError("Type mismatch i first parameter (number of strings). Expected integer")

    if len(params) != num_lines * 3 + 1:
        raise ValueError("Wrong number of parameters: " + str(num_lines) +
                            " lines declared," + str(num_lines * 3 + 1) + " parameters expected")

    lines = []
    for i in range(num_lines):

        current_index = i * 3 +1
        try:
            position = int(params[current_index])
        except ValueError as er:
            raise ValueError("Wrong input at position " + str(current_index) + " Integer expected")
        except TypeError as er:
            raise TypeError("Wrong input at position " + str(current_index) + " Integer expected")

        current_index += 1
        if isinstance(params[current_index],str):
            input_string = params[current_index]
        else:
            raise TypeError("Wrong input at position " + str(current_index) + " String expected")

        current_index += 1
        replacement = params[current_index]
        if not isinstance(replacement,str):
            raise TypeError("Wrong input at position " + str(current_index) + " single character expected")
        if len(replacement) !=1:
            raise ValueError("Wrong input at position " + str(current_index) + " single character expected")

        try:
            lines.append(replace_single(position,input_string,replacement))
        except ValueError as er:
            raise ValueError(er)

    return lines

# WARNING: DO NOT CHANGE CODE BELOW THIS LINE


HELP_STRING = """Welcome to the replacer!
Replacer knows to replace a character at a given index in a string with a different single character.
It knows to do so for multiple strings.
It prints a the strings after replacement.

Usage:
"ex2-replacer.py --help" - display this message 
"ex2-replacer.py num_replacements [index1 str1 char_to_replace_with1 [index2 str2 char_to_replace_with2]...]"

Examples:
"ex2-replacer.py 0" - do not do any replacements.  Will print "" - empty string
"ex2-replacer.py 1 0 boat g" - will print "goat"
"ex2-replacer.py 2 0 boat g 2 boat o" - will print "goat boot"  
"""

NUM_ARGS_NO_ARGS = 1
NUM_ARGS_HELP = 2


def main():
    if len(sys.argv) == NUM_ARGS_HELP and sys.argv[1] == '--help':
        print(HELP_STRING)
        return
    elif len(sys.argv) == NUM_ARGS_NO_ARGS:
        print(f'ERROR: No arguments were given.\nFor proper usage:\n{HELP_STRING}')
        return

    try:
        result = replacer(sys.argv[1:])
    except Exception as ex:
        print(f'ERROR: {ex}\n\nUsage instructions:\n{HELP_STRING}')
    else:
        print(f'SUCCESS: Result of replacing the letters is:\n', ' '.join(result))


if __name__ == '__main__':
    main()
