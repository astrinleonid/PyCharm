import pickle
with open('mlb_players.pkl', 'rb') as pkl_file:
    data = pickle.load(pkl_file)
print(data)