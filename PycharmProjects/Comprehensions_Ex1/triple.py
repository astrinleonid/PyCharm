

def triple(str_to_triple):
    """
    Takes string containing a phrase as a parameter
    Returns the string with every letter tripled
    """
    return "".join([i*3 for i in list(str_to_triple)])



def main(str):
    assert triple("Hello") == "HHHeeellllllooo"
    return triple(str)

if __name__ == '__main__':
    print(main('Hello World'))
