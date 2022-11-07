import json
import csv
import pickle

def read_json(file):

    with open(file) as json_file:
        data = json.load(json_file)
    return data

def write_csv(data, file):
    fieldnames = []
    for item in data[0].keys():
        fieldnames.append(item)

    with open(file, "w") as csv_file:

        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for item in data:
            csv_writer.writerow(item)

def read_csv(file):

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = []
        header = next(csv_reader, None)
        for row in csv_reader:
            data.append(row)
    return [header, data]

def arrange_data(header, data):
    arranged_data = []
    for line in data:
        i_dict = {}
        for i in range(len(header)):
            i_dict[header[i]] = line[i]
        arranged_data.append(i_dict)
    return arranged_data

def write_json(data,file):
    with open(file, "w") as json_file:
        json.dump(data,json_file)

def ex1():
    data = read_json('comments.json')
    write_csv(data, 'comments.csv')
    write_pickle(data,'comments.pkl')

def ex2():
    csv_raw_data = read_csv('hw_25000.csv')
    data = arrange_data(csv_raw_data[0], csv_raw_data[1])
    write_json(data,'hw_25000.json')

def read_pickle(file):
    with open(file,'rb') as pkl_file:
        data = pickle.load(pkl_file)
    return data

def write_pickle(data, file):
    with open(file,'wb') as pkl_file:
        pickle.dump(data,pkl_file)

def ex3():
    data = read_pickle('mlb_players.pkl')
    write_csv(data,'mlb_players.csv')
    write_json(data,'mlb_players.json')

def main():

   ex1()
   ex2()
   ex3()

main()