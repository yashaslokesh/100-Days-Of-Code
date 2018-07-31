
import requests
import json

"""
    Only access public repositories. The requests module is used to make GitHub API calls, 
    from which all information will be taken.
"""

def retrieve(name):
    url = f"https://api.github.com/users/{name}/repos"
    response = requests.get(url)
    return json.loads(response.text)

def process(data):
    pass

def main():
    username = input("Enter your GitHub Username: ")
    data = retrieve(username)


if __name__ == '__main__':
    main()