from collections import OrderedDict
import random
from pprint import pprint

def learn_from_text(what_comes_next, text):
    index = 1
    while text[index] != "<END>":
        temp = tuple(text[index-1:index+1])
        if temp not in what_comes_next:
            what_comes_next[temp] = [text[index+1]]
        else:
            what_comes_next[temp].append(text[index+1])
        index += 1
    # print(what_comes_next)

def learn_from_file(what_comes_next, filename):
    text = ["<START>","<START>"]
    with open(filename) as f:
        for line in f:
            text += [word.strip() for word in line.split()]
    text.append("<END>")

    learn_from_text(what_comes_next, text)

def generateText(what_comes_next):
    result = ["<START>","<START>"]
    index = 1
    while True:
        temp = random.choice(what_comes_next[tuple(result[index-1:index+1])])
        result.append(temp)
        if temp == "<END>":
            return result
        index += 1

def main():
    what_comes_next = OrderedDict()
    learn_from_file(what_comes_next, "adventureOfTheEngineersThumb.txt")
    result = generateText(what_comes_next)
    result = result[2:-1]
    print()
    pprint(' '.join(result), width=80,indent=4)
    print()

if __name__ == '__main__':
    main()