


def dividable(list,n):
    """
    Takes a list of numbers and filters out those which are not dividable by n
    """
    return [i for i in list if i % n == 0]

def main(list,n):
    assert dividable([4,3,6,7,11],3) == [3,6]
    return dividable(list,n)

if __name__ == '__main__':
    print(main([5,8,7,3,10,123,56,9,44,64,79,48,33],3))

