

def samesame(input_list):
    """
    Takes a list of the same-type elements as an argument and returns the sum of the elemnts in the list
    """
    element_type = type(input_list[0])
    for i, item in enumerate(input_list):
        if not isinstance(item, element_type):
            raise Exception("Cannot add up elements of different types" )
        elif i == 0:
            sum_of_elements = item
        else:
            sum_of_elements += item
    return sum_of_elements





if __name__ == '__main__':
    print(samesame(['a5', 'drfer']))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
