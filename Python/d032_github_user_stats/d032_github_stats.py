""" This module is used to retrieve and display a GitHub user's public repos info.

"""

import datetime
import requests
import json

def retrieve(name):
    url = f"https://api.github.com/users/{name}/repos"
    response = requests.get(url)
    data = json.loads(response.text)
    with open("d032_github_user_stats/data.json","w") as f:
        f.write(json.dumps(data, indent=2))
    return data

def process(data):
    repo_results = [
        (f'Repo: {repo["name"]}\nDescription: {repo["description"]}\nLink: {repo["html_url"]}\n'
        f'Stars: {repo["stargazers_count"]}\nForks: {repo["forks_count"]}\n')
        for repo in data
    ]

    return '\n'.join(repo_results)

def main():
    username = input("Enter your GitHub Username: ")
    data = retrieve(name=username)
    result = process(data)

    today = datetime.datetime.today().strftime("%m-%d-%Y")
    with open(f"github-repos-{today}.txt","w") as f:
        f.write(result)


if __name__ == '__main__':
    main()