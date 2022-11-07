
TEST_STRING = "We were more than just a slice"
LEN = len(TEST_STRING)

if __name__ == '__main__':

    print(TEST_STRING[:6])
    print(TEST_STRING[4:28])
    print(TEST_STRING[::2])
    print(TEST_STRING[3:LEN-2:2])
    print(TEST_STRING[::-1])

