from random import shuffle

QUOTES = ["a", "b", "c", "d", "e"]

def random_quote(quotes=None, cycles=1):
    if quotes is None:  # default to use QUOTES
        quotes = QUOTES.copy()  # don't mess with original
    else:
        quotes = quotes.copy()

    for cycle in range(cycles):  # if all quotes used, shuffle again
        shuffle(quotes)
        for quote in quotes:
            yield quote

for counter, quote in enumerate(random_quote()):
    print(quote)
    if counter == 3:
        break
    
input()
