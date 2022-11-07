class person:

    name = ''
    age = 0
    weight = 0
    height = 0

    def assign_param(self, inp, param):
        if param == "Name":
            if inp == '':
                return False
            else:
                self.name = inp
        elif param == "Age":
            try:
                p = int(inp)
            except:
                return False
            if p < 0 or p > 200:
                return False
            self.age = p
        elif param == "Weight":
            try:
                p = int(inp)
            except:
                return False
            if p < 0 or p > 200:
                return False
            self.weight = p
        elif param == "Height":
            try:
                p = int(inp)
            except:
                return False
            if p < 1 or p > 300:
                return False
            self.height = p/100
        return True

    def get_param(self,param):
        inp = input("Please enter your " + param + '\n' + '>')
        return self.assign_param(inp,param)

    def bmi(self):
        return int(self.weight/(self.height**2))


def get_parameters(pers):
    Parameters = {"Name":'',"Age":0,"Height":0,"Weight":0}
    for item in Parameters:
        while not pers.get_param(item):
            print("Sorry, I can deal with humans only.")
            print("Humans use to weigh from 0 to 200 kg, "
              "have hight between 1 and 300 cm "
              "and live between 0 and 200 years")
            print("And humans have names")

def My_BMI():

    P_count = ["First","Second"]
    Persons = []
    for i in range(2):
        print(P_count[i] + " person data" + '\n')
        print("Age in years, weight in kg, height in cm" +'\n')
        pers = person()
        get_parameters(pers)
        Persons.append(pers)

    for i in range(2):
        print('Name:',Persons[i].name,' Age:',Persons[i].age, 'BMI:', Persons[i].bmi())




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    My_BMI()
