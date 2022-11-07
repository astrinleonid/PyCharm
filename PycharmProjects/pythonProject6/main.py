def f(lst=[]): # lst is an optional input and defaults to [] if not specified
    if len(lst) > 0:
        lst.append("hello")
        return lst
    else:
        return ["hello"]



def main():
    print(f())
    print(f())
    print(f())

main()