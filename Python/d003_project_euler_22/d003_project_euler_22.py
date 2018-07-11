import csv

names = list()

with open("../supporting_files/project_euler_p022_names.csv","r") as names_file:
    reader = csv.reader(names_file)
    for row in reader:
        for col in row:
            names.append(col)

names.sort()

def calcNameScore( name : str, position : int) -> int:
    value = 0
    for letter in list(name):
        value += ord(letter) - 64
    return value * position

sum = 0
for name in names:
    sum += calcNameScore(name, names.index(name) + 1)

print(sum)