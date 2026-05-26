import requests

def main():
    response = requests.get("https://api.github.com/repos/anthropics/anthropic-sdk-python")
    data = response.json()
    print(f"Repo: {data['full_name']}")
    print(f"Stars: {data['stargazers_count']}")
    print(f"Description: {data['description']}")


if __name__ == "__main__":
    main()
