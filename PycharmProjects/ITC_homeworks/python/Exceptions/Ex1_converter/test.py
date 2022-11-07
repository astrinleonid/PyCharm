import csv


def read_csv(file):

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = []
        header = next(csv_reader, None)
        for row in csv_reader:
            data.append(row)
    print(f"Header {header}, data {data}")
    file.close()


# read_csv("/User/leonidastrin/test.csv")

file = open("/User/leonidastrin/text.txt",'r')