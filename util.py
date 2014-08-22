from random import randint

# In Flight from the Dark, the Random Number Table contains 100 numbers ranging
# between 0 and 9, each number occuring ten times. To someone not familiar with
# the table after many playthroughs (I'm looking at you) this is equivilant to
# rolling a ten-sided die.
def castD10():
    return randint(0, 9)
