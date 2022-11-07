# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def My_BMI():

    P1 = []
    print("First person data" + '\n')
    inp = input("Please enter your name" + '\n' +'>')
    P1.append(inp)
    try:
      inp = int(input("Please enter your age" + '\n' +'>'))
    except:
        print("Wrong input")
    P1.append(inp)
    try:
      inp = int(input("Please enter your hight" + '\n' +'>'))/100
    except:
        print("Wrong input")
    P1.append(inp)
    try:
      inp = int(input("Please enter your weight" + '\n' +'>'))
    except:
        print("Wrong input")
    P1.append(inp)
    P1.append(int(P1[3]/(P1[2]**2)))

    P2 = []
    print("Second person data" + '\n')
    inp = input("Please enter your name" + '\n' +'>')
    P2.append(inp)
    try:
      inp = int(input("Please enter your age" + '\n' +'>'))
    except:
        print("Wrong input")
    P2.append(inp)
    try:
      inp = int(input("Please enter your hight" + '\n' +'>'))/100
    except:
        print("Wrong input")
    P2.append(inp)
    try:
      inp = int(input("Please enter your weight" + '\n' +'>'))
    except:
        print("Wrong input")
    P2.append(inp)
    P2.append(int(P2[3]/(P2[2]**2)))

    print('Name:',P1[0],' Age:',P1[1], 'BMI:', P1[4])
    print('Name:', P2[0], ' Age:', P2[1], 'BMI:', P2[4])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    My_BMI()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
