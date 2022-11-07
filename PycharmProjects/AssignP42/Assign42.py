
def My_BMI():



    Persons = [['First','name',{"Age":0,"Hight":0,"Weight":0},0],['Second','name',{"Age":0,"Hight":0,"Weight":0},0]]
    for i in range(2):
        print(Persons[i][0] + " person data" + '\n')
        inp = input("Please enter your name" + '\n' +'>')
        Persons[i][1] = inp
        for item in Persons[i][2] :
            try:
              inp = int(input("Please enter your " + item + '\n' +'>'))
            except:
                print("Wrong input")
            Persons[i][2][item]= inp

        Persons[i][3] = int(Persons[i][2]["Weight"]/(Persons[i][2]["Hight"]**2)*10000)

    for i in range(2):
        print('Name:',Persons[i][0],' Age:',Persons[i][2]["Age"], 'BMI:', Persons[i][3])




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    My_BMI()
