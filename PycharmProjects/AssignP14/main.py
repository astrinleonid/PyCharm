def part4_get_str_mult_of_3(num):
    """
    Return a string of a's and b's that answers whether a number from 0 till given num are multiples of 3
    If a number is a multiple of 3, return 'a' for this number, and 'b' otherwise.
    :param num: Number up to which to check (not inclusive)
    :return: String of a's and b's, a's for all number from 0 till num that are multiples of 3, b otherwise
    """
    message =''
    for number in range(num+1):
        # add 'a' if the number is a multiple of 3, otherwise add 'b'
        if (number % 3) == 0:
            message = message + 'a'
        else:
            message = message + 'b'
    return message


def main():
    num = 10
    print(part4_get_str_mult_of_3(num))

main()