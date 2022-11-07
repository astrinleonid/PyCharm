
def wipe_coffee(strings):

    """
    Cleans the last word of the phrase from the letters c,o,f,e in the end
    """
    return [" ".join(string.split()[:-1] + [string.split()[-1].rstrip('cofe')]) for string in strings]

def main(str):
    assert wipe_coffee(["Hello Worldcoffffeee","Byecofee"]) == ["Hello World","By"]
    return wipe_coffee(str)

if __name__ == '__main__':

    print(main(["hello worldcoffffofofeeefff"]))
