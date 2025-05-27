from random import shuffle

def shuffle_card(c):
    shuffle(c)
    return c


cards = [i for i in range(0, 10)] + ['J', 'Q', 'K', 'A']
print("Before shuffle : ", *cards)
shuffle_card(cards)
print("After shuffle : ", *cards)