import re
import os

file_name = "input.txt"
directory = os.path.dirname(os.path.abspath(__file__))

# Challenge 1
def calcualte_position(file_location):

    with open(file_location) as f:
        lines = f.read().splitlines()

    horizontal_position = sum([int((re.findall('\w+', x))[1]) for x in lines if x.__contains__('forward')])
    vertical_position_up = sum([int((re.findall('\w+', x))[1]) for x in lines if x.__contains__('up')])
    vertical_position_down = sum([int((re.findall('\w+', x))[1]) for x in lines if x.__contains__('down')])
    try:
        if vertical_position_up > vertical_position_down:
            vertical_position = vertical_position_up - vertical_position_down
        else:
            vertical_position = vertical_position_down - vertical_position_up

        position = vertical_position * horizontal_position

        print(f"challenge 1 - position: {position}")
    except Exception:
        print("fail")


calcualte_position(f"{directory}\{file_name}")




# Challenge 2

with open(f"{directory}\{file_name}") as f:
    lines = f.read().splitlines()
    

depth = 0
horizontal_position = 0
aim = 0

for x in lines:
    row = (x.split())
    if row[0]=='down':
        #depth += int(row[1])
        aim += int(row[1])
    elif row[0]=='up':
        #depth -= int(row[1])
        aim -= int(row[1])
    elif row[0]=='forward':
        horizontal_position += int(row[1])
        depth += (aim * int(row[1]))
    #print(f"depth: {depth}")
    #print(f"aim: {aim}")
    #print(f"horizontal_position: {horizontal_position}")
    #print("-------")

print(f"challenge 2 - position: {depth*horizontal_position}") 