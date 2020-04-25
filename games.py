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

    #Prints bet result
    if (call == "Heads" and result == 1) or (call == "Tails" and result == 2):
        print("You've won " + str(bet) + " dollars!")
        return bet
    else:
        print("You've lost " + str(bet)+" dollars!")
        return -bet


def cho_han(call, bet):
    #Has to bet money
    if bet <= 0:
        print("They say you need money to make money! Make sure your bet is over 0.")
        return 0

    print("Let's play Cho-Han!")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("The sum of the dice is " + str(total))

    if call == "Even" and total % 2 == 0:
        print("You've won " + str(bet)+" dollars!")
        print("------------------")
        return bet
    elif call == "Odd" and total % 2 == 1:
        print("You've won " + str(bet)+" dollars!")
        print("------------------")
        return bet
    else:
        print("You've lost " + str(bet)+" dollars!")
        print("------------------")
        return -bet


#Call your game of chance functions here
