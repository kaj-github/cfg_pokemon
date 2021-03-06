print("~~ You are now playing Pokemon Top Trumps ~~ ")
playername = input("Player, please enter your name: ")
print("Welcome " + playername + ".\nGet ready for battle!")
computername = "Computer"
print("You are playing against " + computername +
      "\nChoose your best stats to win and become a master of pokemon!\nYou must score at least 8 to win!")

import random
import requests
import time
#add time pauses


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'base_experience': pokemon['base_experience'],
        'order': pokemon['order'],
    }


def compare_stats():

    player_choice = random_pokemon()
    my_pokemon_stats = {
        'name': (player_choice['name']),
        'id': (player_choice['id']),
        'height': (player_choice['height']),
        'weight': (player_choice['weight']),
        'base_experience': (player_choice['base_experience']),
        'order': (player_choice['order']),
    }
    print('You were given {}'.format(my_pokemon_stats['name'])),
    print('id: {}'.format(my_pokemon_stats['id'])),
    print('height: {}'.format(my_pokemon_stats['height'])),
    print('weight: {}'.format(my_pokemon_stats['weight'])),
    print('base_experience: {}'.format(my_pokemon_stats['base_experience'])),
    print('order {}'.format(my_pokemon_stats['order'])),

    choose_stats = input('What stat would you like to use? ')
    if choose_stats == 'id':
        print('You have chosen to play id: {}'.format(player_choice['id']))
    if choose_stats == 'height':
        print('You have chosen to play height: {}'.format(player_choice['height']))
    if choose_stats == 'weight':
        print('You have chosen to play weight: {}'.format(player_choice['weight']))
    if choose_stats == 'base_experience':
        print('You have chosen to base experience: {}'.format(player_choice['base_experience']))
    if choose_stats == 'order':
        print('You have chosen to play order: {}'.format(player_choice['order']))
    opponent_choice = random_pokemon()
    print('Your opponent has chosen {}'.format(opponent_choice['name']))
    opponent_pokemon_stats = {
        'name': (opponent_choice['name']),
        'id': (opponent_choice['id']),
        'height': (opponent_choice['height']),
        'weight': (opponent_choice['weight']),
        'base_experience': (opponent_choice['base_experience']),
        'order': (opponent_choice['order']),
    }
    player_stats = player_choice[choose_stats]
    opponent_stats = opponent_choice[choose_stats]


    win = player_stats > opponent_stats

    if win is True:
        player_score = 2
        print('With a {} of {}!'.format(choose_stats, opponent_stats))
        win_msg = "You won! You scored " + str(player_score)
        print(win_msg)

    elif win is False:
        player_score = 0
        print(opponent_stats)
        lose_msg = "Uh-oh, the opponent won. You score " + str(player_score)
        print(lose_msg)

    else:
        player_score = 1
        print(opponent_stats)
        tie_msg = "It's a tie! You scored " + str(player_score)
        print(tie_msg)

    return player_score


Scores = []


for number in range(5):
    player_score = compare_stats()
    Scores.append(player_score)

final_score = sum(Scores)

winner = final_score >= 8

if winner is True:
    end_message = "CONGRATULATIONS! You won the game. You scored " + str(final_score) + ". You win!"

    print(end_message)

if winner is False:
    end_message = "Bad luck, you lose. Your final score was " + str(final_score) + ". Try again!"

    print(end_message)


with open("highscore.txt", "w+") as text_file:
    text_file.write(str(final_score))

with open('highscore.txt', 'r') as newscore_file:
    new_score = newscore_file.read()

highscore = final_score + int(new_score)

print(("Your high score is " + str(highscore)))
