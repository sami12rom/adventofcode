import os

file_name = "input.txt"
directory = os.path.dirname(os.path.abspath(__file__))

with open(f"{directory}\{file_name}") as f:
    lines = f.read().splitlines()

#Challenge 1
result = [x for i, x in enumerate(lines) if int(lines[i]) > int(lines[i-1])]
print(f"challenge 1: {len(result)}")

#Challenge 2
window_size = 3
new_input = [sum(list(map(int, lines[x:x+window_size]))) for x in range(len(lines)-window_size+1)]
result = [x for i, x in enumerate(new_input) if int(new_input[i]) > int(new_input[i-1])]
print(f"challenge 2: {len(result)}")
