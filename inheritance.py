import random
class Card:
    '''Represents a standard playing card.'''
    rank_names = [None, 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suit_names = ['Chuon', 'Ro', 'Co', 'Bich']
    #: The default card is the 2 of Clubs.(2 Chuon)
    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} {}'.format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self, other):
        #: Check the ranks
        if self.rank > other.rank: return 1
        elif self.rank < other.rank: return -1
        
        #: If the ranks are the same 
        if self.suit > other.suit: return 1
        elif self.suit < other.suit: return -1
        
        #: If the ranks are the same return 0
        return 0

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        if len(res) == 0 : return 'Empty Card!'
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        return self.cards.append(card)

    def shuffle_card(self):
        return random.shuffle(self.cards)

    def sort_card(self):
        return self.cards.sort()

    def move_cards(self, hand, num):
        '''
        Move num cards into the hand
        '''
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, num_of_hands, num_of_cards):
        hands = []
        if (num_of_hands < 2 or 
            num_of_cards < 1 or 
            num_of_cards * num_of_hands > 52): return 'Invalid number of hands or number of cards'
        self.shuffle_card()
        for i in range(num_of_hands):
            hand = PokerHand()
            self.move_cards(hand, num_of_cards)
            hand.classify()
            hands.append(hand)
        return hands

class Hand(Deck):
    '''
    Represents a hand of playing cards
    '''
    def __init__(self, label = ''):
        self.cards = []
        self.label = label
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        if len(res) == 0 : return 'Empty Card!'
        print(self.label)
        return '\n'.join(res)


class Hist(dict):
    """A map from each item (x) to its frequency."""

    def __init__(self, seq=[]):
        "Creates a new histogram starting with the items in seq."
        for x in seq:
            self.count(x)

    def count(self, x, f=1):
        "Increments the counter associated with item x."
        self[x] = self.get(x, 0) + f
        if self[x] == 0:
            del self[x]

class PokerHand(Hand):
    all_labels = ['straightflush', 'fourkind', 'fullhouse', 'flush',
                  'straight', 'threekind', 'twopair', 'pair', 'highcard']
    
    
    def in_a_row(self, ranks, n):
        """Checks whether the histogram has n ranks in a row.

        hist: map from rank to frequency
        n: number we need to get to
        """
        count = 0
        for i in range(1, 15):
            if ranks.get(i, 0):
                count += 1
                if count == 5: return True
            else:
                count = 0
        return False

    def make_histograms(self):
        '''Computes histograms for suits and hands.

        Creates attributes:

          suits: a histogram of the suits in the hand.
          ranks: a histogram of the ranks.
          sets: a sorted list of the rank sets in the hand.
        '''
        self.suits = Hist()
        self.ranks = Hist()
        
        for c in self.cards:
            self.suits.count(c.suit)
            self.ranks.count(c.rank)

        self.sets = list(self.ranks.values())
        self.sets.sort(reverse=True)

    def check_sets(self, *t):
        """Checks whether self.sets contains sets that are
        at least as big as the requirements in t.

        t: list of int
        """
        for need, have in zip(t, self.sets):
            if need > have: return False
        return True

    def has_highcard(self):
        '''
        Returns True if this hand has a high card (each card is called high card)
        '''
        return len(self.cards)

    def has_pair(self):
        return self.check_sets(2)

    def has_twopair(self):
        return self.check_sets(2, 2)

    def has_threekind(self):
        return self.check_sets(3)
    
    def has_fourkind(self):
        return self.check_sets(4)
    
    def has_fullhouse(self):
        return self.check_sets(3,2)

    def has_flush(self):
        for value in self.suits.values():
            if value >= 5: return True
        return False

    def has_straight(self):
        """Checks whether this hand has a straight."""
        # make a copy of the rank histogram before we mess with it
        ranks = self.ranks.copy()
        ranks[14] = ranks.get(1, 0)

        # see if we have 5 in a row
        return self.in_a_row(ranks, 5)
    
    def has_straightflush(self):
        """Checks whether this hand has a straight flush.

        Clumsy algorithm.
        """
        # make a set of the (rank, suit) pairs we have
        s = set()
        for c in self.cards:
            s.add((c.rank, c.suit))
            if c.rank == 1:
                s.add((14, c.suit))

        # iterate through the suits and ranks and see if we
        # get to 5 in a row
        for suit in range(4):
            count = 0
            for rank in range(1, 15):
                if (rank, suit) in s:
                    count += 1
                    if count == 5: return True
                else:
                    count = 0
        return False

    def classify(self):
        '''Classifies this hand.

        Creates attributes:
          labels:
        '''
        self.make_histograms()
        for label in PokerHand.all_labels:
            f = getattr(self, 'has_' + label)
            if f():
                self.label = label
                break


def find_defining_class(obj, method_name):
    '''Finds and returns the class object that will provide 
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    '''
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None

#: Create queen of diamonds

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle_card()
    hands = deck.deal_hands(7,7)
    for hand in hands:
        print(hand)