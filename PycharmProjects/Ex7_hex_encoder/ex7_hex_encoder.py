
string = "hello world"
print("".join([str(hex(ord(char)))[2:] for char in list(string)]))