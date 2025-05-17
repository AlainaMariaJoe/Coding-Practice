import random
def shuffle_cards(l):
    random.shuffle(l)
    return l

cards = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
print(shuffle_cards(cards))
