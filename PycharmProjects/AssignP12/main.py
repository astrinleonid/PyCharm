def part2_delete_list_members(lst):
    """
    Delete list members
    :param lst: list whose members need to be deleted
    :return: updated list
    """
    for i in range(len(lst)):
        del lst[0]

    return lst


def main():
    lst = ['ed','srferf','adwed','ded']
    lst = part2_delete_list_members(lst)
    print(lst)

main()