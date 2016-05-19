import random
import sys
import time

pokedex = {
    "Bulbasaur": [200, 32],
    "Ivysaur": [230, 40],
    "Venusaur": [270, 50],
    "Charmander": [188, 30],
    "Charmeleon": [226, 40],
    "Charizard": [266, 84],
    "Squirtle": [198, 48],
    "Wartortle": [228, 31],
    "Blatoise": [268, 41],
    "Caterpie": [200, 15],
    "Metapod": [210, 10],
    "Butterfree": [230, 22],
    "Weedle": [190, 17],
    "Kakuna": [200, 12],
    "Beedrill": [240, 45],
    "Pidgey": [190, 22],
    "Pidgeotto": [236, 30],
    "Pidgeot": [276, 40],
    "Rattata": [170, 28],
    "Raticate": [220, 40],
    "Spearow": [190, 30],
    "Fearow": [240, 45],
    "Ekans": [180, 30],
    "Arbok": [230, 42],
    "Pikachu": [180, 27],
    "Raichu": [230, 45],
    "Sandshrew": [210, 37],
    "Sandslash": [260, 50],
    "Nidoran2": [220, 23],
    "Nidorina": [250, 32],
    "Nidoqueen": [290, 46],
    "Nidoran1": [202, 28],
    "Nidorino": [232, 36],
    "Nidoking": [272, 51],
    "Clefairy": [250, 22],
    "Clefable": [300, 35],
    "Vulpix": [186, 20],
    "Ninetales": [256, 38],
    "Jigglypuff": [340, 22],
    "Wigglytuff": [390, 35],
    "Zubat": [190, 22],
    "Golbat": [260, 40],

}

enemy = random.choice(list(pokedex.keys()))
enemy = [enemy, pokedex[enemy][0]]
player = random.choice(list(pokedex.keys()))
player = [player, pokedex[player][0]]
print("Your pokemon is: %s" % (player[0]))
print("The enemy's pokemon is: %s" % (enemy[0]))
answer = ''

while(player[1] > 0 and enemy[1] > 0):
    if pokedex[player[0]][1] < enemy[1]:
        choice = input("What would you like to do?")
        if choice in ["Attack", "attack", "Kill", "kill"]:
            print("The player has attacked the enemy's %s." % (enemy[0].items()[0][0]))
            enemy[1] -= pokedex[player[0]][1]
            print("The enemy's %s has %d HP remaining!" % (enemy[0], enemy[1]))
        elif choice in ["potion", "Potion"]:
            player[0] = player[0] + 20
        else:
            print "there's no action like this"
            break
else:
    enemy[1] = 0
    print("The enemy's %s has %d HP remaining!" % (enemy[0], enemy[1]))
    print("The player's %s has won!" % (player[0]))

if pokedex[enemy[0]][1] < player[1]:
    print("The enemy has attacked the player's %s." % (player[0]))
    player[1] -= pokedex[enemy[0]][1]
    print("The player's %s has %d HP remaining!" % (player[0], player[1]))
else:
    player[1] = 0
    print("The player's %s has %d HP remaining!" % (player[0], player[1]))
    print("The enemy's %s has won!" % (enemy[0]))
