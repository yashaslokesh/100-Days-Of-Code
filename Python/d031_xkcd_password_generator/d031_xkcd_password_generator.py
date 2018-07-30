import secrets

def load_list():
    with open("supporting_files/english3.txt") as f:
        return [line.strip() for line in f.readlines() if len(line.strip()) >= 5]

def make_password(words, num_words):
    random_words = [secrets.choice(words) for _ in range(num_words)]
    password = ''.join(random_words)
    words_used = ', '.join(random_words)
    return f"Password: {password}\n\nWords Used: {words_used}"

def main():
    num_words = int(input("How many words long would you like your password to be? The words will all be >= 5 characters: "))

    words = load_list()
    print(f"\n{make_password(words, num_words)}\n")

if __name__ == '__main__':
    main()
