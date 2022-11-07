def part3_is_bird_in_list(lst):
    """
    Check if the word "bird" is in the list received
    :param lst: list to check
    :return: message to print that answers the question of whether the word "bird" is in the list
    """
    message = 'No birds here'
    if "bird" in lst:
        message = "I found a bird!"
    return message

def main():
    lst1 = ['ed','srferf','wefearwf','wefaw']
    lst2 = ['ed', 'srferf','bird', 'wefearwf', 'wefaw']
    print(part3_is_bird_in_list(lst1))
    print(part3_is_bird_in_list(lst2))

main()