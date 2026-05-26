prompts = ["what is an apple", "could you generate a prompt", "what is banana", "how can you help me", "what is claude code"]


def count_tokens_approx(text: str) -> int:
    return len(text) // 4


def main():
    result =[(p,count_tokens_approx(p)) for p in prompts if len(p) > 20]
    for item in result:
        print(f"Prompt: {item[0]}, Token: {item[1]}")


if __name__ == "__main__":
    main()