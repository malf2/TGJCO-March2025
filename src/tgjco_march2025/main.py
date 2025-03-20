import requests
from rich import print

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    @property
    def scores(self) -> list[int]:
        scores = [0]
        for card in self.hand:
            card = card[:-1]
            if card.isdigit():
                scores = [s + int(card) for s in scores]
            elif card in "KQJ":
                scores = [s + 10 for s in scores]
            elif card == "A":
                new_scores = []
                for score in [s + 1 for s in scores]:
                    new_scores.append(score)
                for score in [s + 11 for s in scores]:
                    new_scores.append(score)
                scores = new_scores
        return scores

    @property
    def bust(self) -> bool:
        return all(score > 21 for score in self.scores)

    @property
    def highest_score(self) -> int:
        return max(s for s in self.scores if not s > 21)

    def choice(self, player=None):
        choice = input("Hit or Stand? type H or S: ")
        while choice not in "HS":
            choice = input("Hit or Stand? type H or S")

        if choice == "H":
            return get_card()
        elif choice == "S":
            return None

class Dealer(Player):
    def choice(self):
        if self.highest_score < 17: return get_card()


def get_hand():
    hand = []
    for i in range(2):
        hand.append(get_card())
    return hand

def get_card() -> str:
    return requests.get("http://localhost:9090/get-card").json()["card"]

def shuffle() -> bool:
    return requests.get("http://localhost:9090/shuffle").ok


def print_scores(player: Player):
    print(f"{player.name} current score: {player.scores}")

def main() -> None:
    shuffle()
    player_name = input("Hi, please enter your name: ")
    player = Player(player_name, get_hand())
    dealer = Dealer("dealer", get_hand())
    print(f"Player starting hand is {player.hand}")
    print(f"Dealer starting hand is {dealer.hand}")

    while not player.bust or dealer.bust:
        print_scores(player)
        print_scores(dealer)
        p_choice = player.choice()
        if p_choice:
            print(f"You got {p_choice} card")
            player.hand.append(p_choice)
        else:
            print(f"Player stuck on {player.scores}")

        d_choice = dealer.choice()
        if d_choice:
            print(f"Dealer got {d_choice} card")
            dealer.hand.append(d_choice)
        else:
            print(f"Dealer stuck on {dealer.scores}")

        if not p_choice or d_choice:
            break

    print_scores(player)
    print_scores(dealer)

    if player.bust and dealer.bust:
        print("no winner, both bust")
    elif player.bust:
        print("dealer wins, player bust")
    elif dealer.bust:
        print("player wins, dealer bust")
    elif player.highest_score == dealer.highest_score:
        print("no winner, both highest scores are the same, with no more hits")
    elif player.highest_score > dealer.highest_score:
        print("player wins, dealer stood and player hit without busting")
    else:
        print("dealer wins, player stood while dealer had higher score")






if __name__ == "__main__":
    main()

