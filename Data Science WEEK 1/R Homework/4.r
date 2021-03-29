import random
# Returns the value of a simulated roll of two dice
def roll_dice():
    input("Press ENTER to roll the dice...")
    a = random.randint(-50, 50)
    b = random.randint(-50, 50)
    return a + b
print(roll_dice())