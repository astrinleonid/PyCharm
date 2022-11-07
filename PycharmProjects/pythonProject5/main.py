# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd

def f(lst=[]): # lst is an optional input and defaults to [] if not specified
    lst.append("hello")
    return lst

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lst ='fuck'
    df = pd.read_excel('sample.xlsx')
#    print(df['name'])
#    for  i in range(2,len(df['name'])) :
    lst = df['name'].values
    print(', '.join(lst))
 #   print(lst)
 #   print(f())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
