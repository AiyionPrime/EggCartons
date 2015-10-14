#!/usr/bin/python3
from math import floor


class EggCartons(object):
    """A virtual represantation of egg-cartons (a modulo and floor() example)

    EggCartons shows the proper distribution of eggs in an amount of cartons.
    Initialize it with an amount of eggs and it holds the amount of boxes
    needed to contain these eggs and the amount of eggs, that are left over
    (that are not enough to fill another full box).

    It's a basic example of the modulo operator and the use of math.floor()
    primarily written to answer https://stackoverflow.com/q/32855052/3458484

    Attributes:
        self.full_boxes: An integer containing the amount of boxes,
            that may be filled completely
        self.leftover:  An integer holding the amount of eggs,
            that are leftover after filling all boxes fully
    """

    def __init__(self, egg_amount, egg_limit=12):
        """Inits EggCartons with an egg amount and an optional egg-limit"""
        self.full_boxes = floor(egg_amount / egg_limit)
        self.leftover = egg_amount % egg_limit

    def __str__(self):
        """Returns a string of relevant information about the instance"""
        result = "full Boxes: " + str(self.full_boxes)
        result += "\nleftover eggs: " + str(self.leftover)
        return result

if __name__ == "__main__":
    # example ful 12-slot egg_cartons
    egg_amount = input("How many eggs have you got?\n")
    some_cartons = EggCartons(int(egg_amount))
    print(some_cartons)

    # example for 25 slot egg cartons
    egg_amount = input("How many eggs have you got? (25 slot cartons)\n")
    some_cartons = EggCartons(int(egg_amount), 25)
    print(some_cartons)
