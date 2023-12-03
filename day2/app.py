from functools import reduce
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

with open("input.txt") as input:

    inp = input.read().splitlines()

# part 1
limits = {
    'red': 12,
    'green': 13,
    'blue': 14
    }

game_sum = 0
game_powers = 0

for game in inp:
    game_mins = {'red': 0, 'blue': 0, 'green': 0}
    game_number = int(game[5:game.find(':')])
    turns = game[game.find(': ') + 2:].split('; ')
    turn_counter = len(turns)
    for cubes in turns:
        cube_list = cubes.split(', ')
        cube_counter = 0
        for cube in cube_list:
            cube_number, cube_colour = cube.split(' ')
            if int(cube_number) > limits[cube_colour]:
                pass
            else:
                cube_counter += 1

            if game_mins[cube_colour] < int(cube_number):
                game_mins[cube_colour] = int(cube_number)
            
        if cube_counter == len(cube_list):    
            turn_counter -= 1

    if turn_counter == 0:
        game_sum += game_number

    game_powers += game_mins['red'] * game_mins['blue'] * game_mins['green']
    
print(game_sum)

print(game_powers)

