import random
import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

hands = {
    "player": [],
    "computer": []
}

def reset():
    hands["player"] = []
    hands["computer"] = []

def pl_hit():
    hands["player"].append(random.choice(cards))
    if sum(hands["player"]) > 21 and 11 in hands["player"]:
        hands["player"][-1] = 1
        print(f"Your cards: {hands["player"]}, current score: {sum(hands["player"])}")
        print(f"Computer's first card: {hands["computer"][0]}")
        blackjack()
    elif sum(hands["player"]) > 21:
        print(f"\nYour final hand: {hands["player"]}, final score: {sum(hands["player"])}")
        print(f"Computer's final hand: {hands["computer"][0]}, final score: {sum(hands["computer"])}")
        print("Bust, you lose!")
        reset()
        blackjack()
    elif sum(hands["player"]) < 21:
        print(f"Your cards: {hands["player"]}, current score: {sum(hands["player"])}")
        print(f"Computer's first card: {hands["computer"][0]}")
        blackjack()

def blackjack():
    if sum(hands["player"]) > 0:
        continue_prompt = input("Hit? y/n").lower()
        if continue_prompt == "y":
            pl_hit()
        else:
            calc_final()
    else:
        play_prompt = input("Fancy a game of Blackjack? y/n: ").lower()[0]
        if play_prompt == "y":
            ace = 11
            hands["player"].append(random.choice(cards))
            hands["computer"].append(random.choice(cards))
            hands["player"].append(random.choice(cards))
            hands["computer"].append(random.choice(cards))

            print(f"Your cards: {hands["player"]}, current score: {sum(hands["player"])}")
            print(f"Computer's first card: {hands["computer"][0]}")

            if sum(hands["computer"]) == 21 and ace in hands["computer"] and 10 in hands["computer"]:
                print(f"\nYour final hand: {hands["player"]}, final score: {sum(hands["player"])}")
                print(f"Computer's final hand: {hands["computer"]}, final score: {sum(hands["computer"])}")
                print("Computer Blackjack, you lose!")
            elif sum(hands["player"]) == 21 and ace in hands["player"] and 10 in hands["player"]:
                print(f"\nYour final hand: {hands["player"]}, final score: {sum(hands["player"])}")
                print(f"Computer's final hand: {hands["computer"][0]}, final score: {hands["computer"][1]}")
                print("Blackjack, you win!")
            else:
                blackjack()
        else:
            print("Cya!")
            return

def calc_final():
    if sum(hands["computer"]) < 17:
        hands["computer"].append(random.choice(cards))
    print(f"\nYour final hand: {hands["player"]}, final score: {sum(hands["player"])}")
    print(f"Computer's final hand: {hands["computer"]}, final score: {sum(hands["computer"])}")
    if sum(hands["computer"]) > 21:
        print("Computer Bust, you win!")
        reset()
        blackjack()
    else:
        if sum(hands["player"]) > sum(hands["computer"]):
            print(f"Player wins with {sum(hands["player"])}!")
            reset()
            blackjack()
        elif sum(hands["computer"]) == sum(hands["player"]):
            print("It's a draw!")
            reset()
            blackjack()
        elif sum(hands["computer"]) > sum(hands["player"]) and sum(hands["computer"]) < 21:
            print(f"Computer wins with {sum(hands["computer"])}")
            reset()
            blackjack()

blackjack()