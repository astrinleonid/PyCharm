import urllib.request
import json

def parse_vocabulary():
    voc = []
    for i in range(ord('a'),ord('y')+1):
        voc = voc + parse_letter(chr(i))
    return voc

def parse_letter(letter):
    file = "https://raw.githubusercontent.com/wordset/wordset-dictionary/master/data/" + letter + ".json"
    data = read_vocabulary_file(file)
    lst = get_nouns(data)
    return lst


def read_vocabulary_file(file):
    voc = []
    get_url = urllib.request.urlopen(file)
#    print ("Responce Status: "+str(get_url.getcode()))
    data_string = get_url.read()
    data = json.loads(data_string)
    return data

def get_nouns(data):
    lst = []
    for word in data:
        try:
            word_desc = data[word]["meanings"]
            for item in word_desc:
                if item["speech_part"] == "noun":
                    i=0
                    for letter in list(word):
                        if letter < 'a' or letter > 'y' :
                            i = 0
                            break
                        else :
                            i += 1
                        if i>7:
                            i = 0
                            break
                    if i > 3:
                        lst.append(word)
                    break
        except:
            continue
    return lst
