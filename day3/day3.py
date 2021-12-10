import statistics
from statistics import mode
from collections import Counter

file_name = "input.txt"
directory = "day3"

with open(f"{directory}\{file_name}") as f:
    lines = f.read().splitlines()

gamma_rate_binary = ("".join(map(str, [mode([int(x[i]) for x in lines]) for i in range(int(len(lines[0])))])))
epsilon_rate_binary = ("".join(map(str, [[key for key, value in Counter([int(x[i]) for x in lines]).items() if value == min(Counter([int(x[i]) for x in lines]).values())][0] for i in range(int(len(lines[0])))])))
epsilon_rate = int(epsilon_rate_binary,2)
gamma_rate = int(gamma_rate_binary,2)
power_consumption = epsilon_rate * gamma_rate
print(power_consumption)