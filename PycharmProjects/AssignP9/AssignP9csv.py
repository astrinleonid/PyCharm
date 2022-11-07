import random
import csv
# from csv_vocabulary import create_vocabulary_file

def print_logo():  # TODO make a logo
    logo = """
    _____________________
    |      HANGMAN      |
    L___________________]
    H H  //           |
    H H //           ( )                  Welcome to the
    H H//             I                       HANGMAN
    H H             / I \                      game!
    H H            /  I  \   
    H H               I
    H H             /   \                  Don't let them
    H H            |     |                   hang you!
    H H            |     |
    H H

    """
    print(logo)


def welcome():
    print_logo()
    name = input("What is your name? \n >")
    print("Hi", name, "! Welcome to the HANGMAN game!")
    return name

def write_vocabulary_file (file, voc):

    with open(file, mode = 'w') as voc_file:
        voc_writer = csv.writer(voc_file, delimiter = ',')
        i = 0
        for item in voc:
            voc_writer.writerow([item])

def read_vocabulary_file(file):
    voc = []
    try:
        with open(file) as dic_file:
            dic_reader = csv.reader(dic_file, delimiter = ',')
            for row in dic_reader:
                voc.append(row[0])
    except:
        voc_i = ['rat', 'cat', 'bat', 'universe', 'peace', 'unity', 'friend', 'science', 'travel', 'adventure', 'party',
           'birthday', 'TroUble', 'QueStion', 'DEVIATION', 'ANOMALY', 'PROBLEM', 'Dream', 'Tale', 'Country']
        voc = []
        for item in voc_i:
            voc.append(item.lower())
    return voc

def get_the_word():
    word = input("Please enter the word\n >")
    word = word.lower()
    for letter in word:
        if letter < 'a' or letter > 'y':
            print("Invalid input")
            return('')
    return word



def edit_vocabulary(voc):
    while True:
        inp = input("What you want to do? A to add, D to delete, C to clear, E to exit\n >").lower()
        if inp == 'a':
            new_word = get_the_word()
            if len(new_word) > 0:
                if new_word not in voc:
                    voc.append(new_word)
                    print(new_word.upper(), "added to the vocabulary")
        elif inp == 'd':
            word_to_delete = get_the_word()
            if word_to_delete in voc:
                voc.remove(word_to_delete)
                print(word_to_delete.upper(), "deleted from the vocabulary")
        elif inp == 'c':
            voc = []
        elif inp == 'e':
            break
    return voc

def choose_the_word():
    file_name = 'HM_voc.csv'
    voc = []
    voc = read_vocabulary_file(file_name)
    edit_voc = input("Do you want to edit the vocabulary? Y to edit, any other key to proceed to the game\n >")
    if edit_voc.lower() == 'y':
        voc = edit_vocabulary(voc)
    write_vocabulary_file(file_name,voc)
    return random.choice(voc)


def get_players_guess(n):
    while True:
        print("You have ", n, "tries")
        inp = input("What is your guess? Please enter a letter\n >")
        inp = inp.lower()
        if len(inp) == 1 and inp >= 'a' and inp <= 'y':
            return inp
        elif inp == '!':
            return -1
        else:
            print("Your input is invalid")


def guessed_letter(word, wts, c):
    nwts = ''
    for i in range(len(word)):
        if word[i] == c:
            nwts += c
        else:
            nwts += wts[i]
    return nwts


def display_word(word):
    print("******  ", word.upper(), "  ******")


def player_won(word, name):
    print("Congrats,", name, ", you are the best!!!")
    print("You have guessed the word")
    display_word(word)


def hangman_game():
    guesses = ''
    word = choose_the_word()
    word_to_show = ''
    for i in range(len(word)):
        word_to_show += '*'
    players_cash = 10
    name = welcome()
    while players_cash > 0:
        print("Guess the word: ", word_to_show.upper())
        bet = get_players_guess(players_cash)
        if bet == -1:
            break
        if bet in guesses:
            print("This letter was already tried")
            continue
        guesses += bet
        players_cash -= 1
        if bet in word:
            print("Good guess!")
            word_to_show = guessed_letter(word, word_to_show, bet)
            players_cash += 1
        else:
            print("It's a miss, sorry")
        if word_to_show == word:
            player_won(word, name)
            return 0
    print("Sorry,", name, ", no more tries. You lost")
    print("Hidden word was")
    display_word(word)


if __name__ == '__main__':
    hangman_game()


