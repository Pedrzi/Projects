import random as rand


def dice_roller(sides=6, rolls=1):
    value = 0
    throws = list()

    if sides < 1:
        raise Exception("sides must be a positive integer")
    elif rolls < 1:
        raise Exception("rolls must be a positive integer")

    elif rolls == 1:
        value += rand.randint(1, sides)
        return value

    for roll in range(rolls):
        throws.insert(-1, rand.randint(1, sides))

    return throws


def bad_dice(sides=6, dice_num=2):
    dices = set()

    for i in range(dice_num):
        dices.add(dice_roller(sides))

    for i in range(sides):
        if i in dices:
            return i, dices


def good_dice(sides=6, dice_num=2):
    dices = set()

    for i in range(dice_num):
        dices.add(dice_roller(sides))

    for i in range(sides):
        dice_value = sides-i
        if dice_value in dices:
            return dice_value, dices


def calc_dice_mean(sides=6, dice_num=1):
    return ((sides + 1)/2)*dice_num
