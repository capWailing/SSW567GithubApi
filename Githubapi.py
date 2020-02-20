"""
    author: Zituo Yan
    description: An Github Api to send requests to get the number of outputs.
    date: 19/2/2020
"""
import requests


def form_restful(user_id):
    """
        transform url to add user id.
    """
    url = "https://api.github.com/users/<ID>"
    url = url.replace("<ID>", user_id)
    return url


def print_information(user_id):
    """
        print information of repos and number of commits
    """
    url = form_restful(user_id)
    for offset, result in enumerate(get_repos(url)):
        print(f"Repo: {result[0]} Number of commits: {result[1]}")


def get_repos(url):
    """
        send request to ask repos and for each repos, ask number of commits
    """
    repos_url = url + "/repos"
    commit_url = url.replace("users", "repos", 1)
    result = requests.get(repos_url)
    repos_json = result.json()
    for i in repos_json:
        yield i.get("name"), get_commits(commit_url + f'/{i.get("name")}/commits')


def get_commits(url):
    """
        send request to ask number of commits
    """
    result = requests.get(url)
    commits_json = result.json()
    return len(commits_json)


def main():
    name = ""
    while len(name) == 0:
        name = input("Please enter your Github ID:\n")
    print_information(name)


if __name__ == '__main__':
    main()
