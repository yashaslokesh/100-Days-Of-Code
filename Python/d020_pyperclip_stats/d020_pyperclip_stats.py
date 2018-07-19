import pyperclip

text_input = pyperclip.paste()

print(f"Your text is {len(text_input)} characters long.")

def countVowels(text):
    vowels = "aeiou"
    conson = "bcdfghjklmnpqrstvwxyz"
    v_count = 0
    c_count = 0
    for letter in text_input.strip().lower():
        if letter in vowels:
            v_count += 1
        elif letter in conson:
            c_count += 1
    print(f"Your text has {v_count} vowels and {c_count} consonants")

countVowels(text_input)