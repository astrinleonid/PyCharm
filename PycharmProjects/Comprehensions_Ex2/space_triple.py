
def space_triple(str_to_triple):

    """
    Takes string containing a phrase as a parameter
    Returns the string with every word tripled
    """
    return " ".join([word*3 for word in str_to_triple.split()])

def main(str):
    assert space_triple("hello world") == "hellohellohello worldworldworld"
    return space_triple(str)

if __name__ == '__main__':
    print(main('Hello World'))
