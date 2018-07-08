import itertools

dictionary = list()

with open("english3.txt") as f:
    for line in f.readlines():
        dictionary.append(line.strip())

"""
    We input a string of letters, and we iterate from the second letter to the end. We don't count the first letter
    because one-letter words like "A" or "I" should be easy to find. 
"""

def find_valid_words(letter_string : str) -> set:
    word_permutations = list()
    for letters in range(2, len(letter_string)):
        for word_perm in itertools.permutations(letter_string, letters):
            word_permutations.append(word_perm)

    real_words = set()

    for word in word_permutations:
        if word in dictionary:
            real_words.add(word)

    return real_words

letter_string = input("Enter a sequence of letters to check if any words can be formed: ")
print("Words: ")
for word in find_valid_words(letter_string):
    print(f"{word}\n")
