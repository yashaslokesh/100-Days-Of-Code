
import re

def regex_finder():
    text = input("Input the text you would like to search through with a regular expression: ")
    pattern = re.compile(input("Enter the regular expression you would like to use to query the text: "))
    matches = pattern.search(text)
    if not matches.groups():
        print("No matches found")
    else:
        print(f"{len(matches.groups())} matches found")
        for match in matches.groups():
            print(f"Match found: {match}")
    
if __name__ == "__main__":
    regex_finder()