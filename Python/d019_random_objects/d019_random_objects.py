import argparse
import random

def coinFlip():
    result = random.choice(["Heads", "Tails"])
    print(f"Coin Flip: {result}")

def cardDraw():
    rank = random.choice("Two Three Four Five Six Seven Eight Nine Ten Ace King Queen Jack".split())
    suit = random.choice("Hearts Diamonds Spades Clubs".split())
    print(f"Card Draw: {rank} of {suit}")

def sixDie():
    die = random.randrange(1,7)
    print(f"Six-Sided Die Roll: {die}")

def twentyDie():
    die = random.randrange(1,21)
    print(f"Twenty-Sided Die Roll: {die}")

def main():
    parser = argparse.ArgumentParser(description="Call randomly-generating functions using command line arguments!")

    parser.add_argument("-f", "--flip", action='store_true', help="Generate a coin flip result picked from 100 coin flips")
    parser.add_argument("-c", "--cards", action='store_true', help="Call this to randomly obtain a card from a deck of 52 cards")
    parser.add_argument("-s", "--six", action='store_true', help="Call this to simulate a six-sided dice roll")
    parser.add_argument("-t", "--twenty", action='store_true', help="Call this to simulate the rolling of a twenty-sided die")

    print("\n")
    args = parser.parse_args()

    if args.flip:
        coinFlip()
    if args.cards:
        cardDraw()
    if args.six:
        sixDie()
    if args.twenty:
        twentyDie()
    print("\n")

if __name__ == '__main__':
    main()