

import random

def print_logo():
    logo = """
    .\.\.\.\.\.\.\.\.\.\.\.\ game WAR game /././././././././././././.
    --------------------✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫✫---------------------- 
    """
    print(logo)


def welcome():

    print_logo()
    name = input("Say your name \n >")
    print("Hi",name,"! Welcome to hell 【ㆆ̀︹ ́ㆆ】")
    print("You have 50 piastres to bet")
    return name

def get_players_bet(limit):
    while True:
        inp = input("What is your bet?\n >")
        try:
            bet = int(inp)
            if bet > limit:
                print("You dont have that much. Get out and cheat somewhere else")
                return -1
            elif bet == 0:
                print("No cash no play")
            elif bet < 0:
                print("Are you betting your bank loan? I need real money")
            else:
                return bet
        except:
            print("I didn't get you")

def player_wins():
    pl_card = random.randint(1,12)
    c_card = random.randint(1,12)
    print("Your card is", pl_card, "my card is", c_card)
    if pl_card > c_card:
        return True
    return False

def propose_new_game():
    while True:
        inp = input("Another bet? Press Y to lose more money, N to bag it and run\n >")
        inp = inp.lower()
        if inp == 'y':
            return True
        elif inp == 'n':
            return False

def game_of_war():

    player_continues = True
    players_cash = 50
    name = welcome()

    while player_continues:
        bet = get_players_bet(players_cash)
        if bet < 0:
            return -1
        if player_wins():
            players_cash += bet
            print("You beat me! Now you have", players_cash)
        else:
            players_cash -= bet
            print("You lost! Now you have", players_cash)
        if players_cash > 0:
            player_continues = propose_new_game()
        else:
            print("You lost all your money. Bye bye broke!")
            player_continues = False


if __name__ == '__main__':
    game_of_war()


