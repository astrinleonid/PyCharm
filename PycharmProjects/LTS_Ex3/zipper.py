

def zipper(input1,input2):
    """
    Takes two lists as arguments and return the list of tuples
    containing same-index elements of the two given lists.
    Tail of the longer list is ignored
    """
    iterated1 = iter(input1)
    iterated2 = iter(input2)
    output_list = []
    while True:
        try:
            output_list.append((next(iterated1),next(iterated2)))
        except:
            break
    return output_list

if __name__ == '__main__':
    print(zipper([1,2,3],[4,5,6]))
    print(zipper([1,"hello world"],[3,2,4,5,6,7]))

