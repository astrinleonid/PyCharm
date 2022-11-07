
"""
General note: the function is implemented as per assignement. 
It should be noted however, that the common abbreviations will be intepreted wrongly, 
like NASA will be spelled as Nasa
I assume that the task of dealing with abbreviations is out of the scope of the assignement,
and probably requires ML to deal with it correctly
"""

def encode_title(string,length):
    """
    Takes a string containing a phrase and an integer representing the minimum length of a title.
    Returns a prase converted into a title (all words capitalized)
    padded with zeroes to reach the minimum length
    """
    capitalized_title = string.title()
    return capitalized_title.zfill(length)

def main():
    string = input("Please input the string you want to make a title:")
    length_str = input("Please provide the minimum length of a title:")
    try:
        length = int(length_str)
    except:
        raise Exception("Length should be an integer")
    print(encode_title(string,length))


if __name__ == '__main__':
    main()

