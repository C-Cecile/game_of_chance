import random

money = 100

def flip_coin(call, bet):
    #Has to bet money
    if bet <= 0:
        print("They say you need money to make money! Make sure your bet is over 0.")
        return 0
    
    #Intro to game -> Prints player's call
    print("Let's flip a coin! You called " + call)
    result = random.int(1,2)

    #Prints flip result -> Heads=1 Tails=2
    if result == 1:
        print("Heads!")
    else: print("Tails!")






#Call your game of chance functions here
