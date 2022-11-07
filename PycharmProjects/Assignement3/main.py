import math

def calculator():
    double_argument = ['+','-','/','*']    # list of the operations with two arguments, refer to line 40
    try: # error corrected: no control for invalid entry
        f_num = float(input('What is the first number? '))
    except:
        calculator()
    operation = input('''
What operation would you like to complete? Please enter the wanted option:
===========================
***************************
===========================
+\t\t| addition
-\t\t| subtraction
*\t\t| multiplication
/\t\t| division
sqrt\t| squareroot
pi/\t\t| Divide number with pi
pi*\t\t| Multiply number with pi
fact\t| Factorial calculation of the number
===========================
***************************
===========================

Enter requested operator: ''')

    if operation == 'fact': # corrected error: operation name 'factorial' instead of 'fact'
        print('{} s factorial is '.format(f_num), end='') # error corrected: wrong syntax, format and content
        try:    # error corrected: make sure that argument is legitimate
            print(math.factorial(f_num)) # error corrected: missed print operator
        except:
            print('undefined')
    elif operation == 'sqrt':
        print('{} square root = '.format(f_num), end='')
        try:    # error corrected: make sure that argument is legitimate
            print(math.sqrt(f_num)) # error corrected: f_num mistakengly converted to a string
        except:
            print('undefined')
    elif operation == 'pi/':
        print('{} / pi = '.format(f_num), end='')
        print(f_num / math.pi)
    elif operation == 'pi*':
        print('{} * pi = '.format(f_num), end='')
        print(f_num * math.pi)
    elif operation in double_argument :  #error corrected: wrong condition
        try:  # error corrected: no control for invalid entry
            l_num = float(input('Please enter the second number: '))   #error corrected, allow second argument to be float
            if operation == '+':
                print('{} + {} = '.format(f_num, l_num), end='')
                print(f_num + l_num) # error corrected: substraction instead of addition
            elif operation == '-':
                print('{} - {} = '.format(f_num, l_num), end='') # error corrected: missing closing bracket
                print(f_num - l_num)

            elif operation == '*':
                print('{} * {} = '.format(f_num, l_num), end='')
                print(f_num * l_num)

            elif operation == '/':
                print('{} / {} = '.format(f_num, l_num), end='')
                try:  # error corrected: make sure that argument is legitimate
                    print(f_num / l_num)
                except:
                    print('undefined')

        except:
            print('invalid entry, operation aborted')
    else:
        print('You have not typed a valid operator, please run the program again.')

    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
ENTER HERE:  ''')

    if calc_again.upper() == 'N': # error corrected: Y instead of N
        print('See you later.')
    elif calc_again.upper() == 'Y': # error corrected: N instead of Y
        calculator()
    else:
        again()


calculator()