from deck import Deck
class PokerHand:
    """
    Class representing a poker hand
    We will rank the hand and determine trips, full house, 4 of a kind, etc
    """
    def __init__(self):
        deck = Deck()
        deck.shuffle()
        _cards = []
        for i in range(5):
            _cards.append(deck.deal())
        self._cards = _cards

    def __str__(self):
        return str(self._cards)

    @ property
    def is_flush(self):
        first_card_suit = self._cards[0].suit
        for i in range(1,5):
            # checking if it is NOT a flush
            if first_card_suit != self._cards[i].suit: # != means not equal
                return False
        return True

    @ property
    def matches(self):
        # need to compare each card against all the others and count matches
        matches = 0
        for card1 in self._cards:
            for card2 in self._cards:
                if card1.rank == card2.rank:
                   continue # skips over comparing to itself, doesn't count as match
                if card1.rank == card2.rank:
                    matches += 1
        return matches

    @property
    def is_fullhouse(self):
        return self.matches == 8 # AAABB - 3x2 matches for A and 2x1 matches for B = 8

iterations = 0
hits = 0
while True:
    hand = PokerHand()
    iterations += 1
    if hand.is_fullhouse:
        # print(hand)
        # print("Done it in ", iterations)
        hits += 1
    if hits == 100:
        prob = hits / iterations * 100
        print(f"probability of a flush is {prob}%")
        break

hand = PokerHand()
print(hand)