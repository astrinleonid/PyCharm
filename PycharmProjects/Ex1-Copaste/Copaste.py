
def get_file_name(path):
    return path.split('/')[-1]

def copaste(path1, path2):
    """
     Copies a file at path1 into the folder at path2
    """
    file1 = open(path1,'rb')
    file2 = open("/".join([path2,get_file_name(path1)]),"wb")
    file2.write(file1.read())
    file1.close()
    file2.close()

def main():

    copaste('/Users/leonidastrin/myrepo/instagram.ico','/Users/leonidastrin/myrepo/writeme')
    file1 = open('/Users/leonidastrin/myrepo/README.txt',"rb")
    file2 = open('/Users/leonidastrin/myrepo/writeme/README.txt',"rb")
    assert file1.read() == file2.read()
    file1.close()
    file2.close()


if __name__ == '__main__':
    main()