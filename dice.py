"""
Dice.py for chuck_a_luck program.

Author: Andrew Nguyen
Version: 3/27/23
"""
import random


# dice_amount = amount of idice, the holy cubes = face value list
def roll_dice(dice_amount, seed_gen=0):  # how many dice, seed generator
    """
    Rolls random number dice between 1-6.
    
    Appends dice_amount to the list with numbers between 1-6.
    Automatically inserts a 6 if either condition isn't met.
    
    Args:
        dice_amount(int): The amount of dice added to the holy cubes list.
        seed_gen(int): The seed the randomly generates 3 random dice face values.
    
    Returns:
        the_holy_cubes(list): The face value of each die.
    """
    the_holy_cubes = []
    random.seed(seed_gen)
    if dice_amount is None:
        for i in range(0, 3):
            the_holy_cubes.append(random.randint(1, 6))
    elif dice_amount > 10 or dice_amount < 1:
        the_holy_cubes = [6]
    else:
        for i in range(0, dice_amount):
            the_holy_cubes.append(random.randint(1, 6))
    return the_holy_cubes

# roll_dice(7)
    
    
def are_valid(the_holy_rolls):
    """
    Checks for valid dice values.
    
    Checks for a True or False boolean for invalid/valid dice roll.
    Checks for 1-10 dice and if each face value is between 1-6.
    
    Args:
        the_holy_rolls(Put something here): The value of the previous list of dice.
    
    Returns:
        bool_roll(bool): A true/false value that represents a valid/invalid dice roll.
    """
    if the_holy_rolls is None:
        return False
    bool_roll = False
    if len(the_holy_rolls) >= 1 and len(the_holy_rolls) <= 10:
        for d in the_holy_rolls:
            if d >= 1 and d <= 6:
                bool_roll = True
            else:
                bool_roll = False
                break
    
    return bool_roll

# print(are_valid(None))
        
        
def count_values(the_holy_cubes, dot_number):
    """
    Counts the repeating values in a dice roll.
    
    If the are_valid function returns false, it returns -1 as an error.
    If the dice roll is valid, dot_number instances are counted.
    
    Args:
        the_holy_cubes(list): The list of tested dice roll numbers.
        dot_number(int): The number of dot_number instances.
        
    Returns:
        count(int): The amount of dot_number instances within the_holy_cubes.
    """
    if are_valid(the_holy_cubes) is False:
        return -1
    else:
        count = 0
        for dot in the_holy_cubes:
            if dot == dot_number:
                count += 1
        return count
        
# print(count_values([3, 3, 5], 3))


def add_values(the_holy_cubes):
    """
    Sums the face value of the dice list.
    
    Adds all the face values of the_holy_cubes and returns the value.
    Unless the are_valid function returns false.
    
    Args:
        the_holy_cubes(list): The list of each face value of every die.
        
    Returns:
        face_sum(int): The sum of all face values in the_holy_cubes.
    """
    if are_valid(the_holy_cubes) is False:
        return -1
    else:
        face_sum = sum(the_holy_cubes)
        return face_sum
    
# print(add_values([7, 7, 7]))
