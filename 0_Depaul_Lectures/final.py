# write a function rolls() that takes no arguments and simulate a sequence of rolls of a pair dice.The simulation should continue rolling the pair of dice and stop only when a rolled pair matches the pair on the original roll. when comparing rolls, the pair of numbers should be the same regardless of order. E.g.g the pair (2,4) matches both the pair (2,4) and the pair (4,2). The function then returns the total number of rolls made. 

# >>> rolls()  # Suppose rolls were : (2,4) (3,5) (4,2)
# 3 

# >>> rolls()  # (5,1) (2,4) (3,3) (4,5) (4,2) (5,1)
# 6




# Implement a class StopLight that represents a traffic signal, which during each cycle goes from green, to yellow, to red. Each StopLight will have 4 numeric attributes: 1)-3) are the duration (in seconds) of the green, yellow, and red signals and 4) is the current time in the cycle. 

# __init__  constructor - accepts four optional arguments. Each of these is stored as an attribute , no validation required. The arguments are: 1. duration of green ( defaults to 30.0), 2. duration of yellow (defaults to 10.0), 3. duration of red  (defaults to 40.0), 4. current time in the cycle (defaults to 0.0).

# __repr__ - see sample below

# >> light1 = StopLight(20.0, 15.0, 30.0, 12.0) # green, yellow, red, time
# >> light1
# StopLight(20.0, 15.0, 30.0, 12.0)
# >> light2 = StopLight() # use defaults
# light2
# StopLight(30.0, 10.0, 40.0, 0.0)


def countsByLetter(str):
    words_list = str.split(" ")

    words_count = {}

    for word in words_list:
        if word[0].upper() in words_count:
            words_count[word[0].upper()] += 1
        else:
            words_count[word[0].upper()] = 1

    return words_count


# countsByLetter("Hello how are you")
# countsByLetter("Buffalo buffalo buffalo buffalo buffalo buffalo buffalo buffalo")


def listMax(list1, list2):
    max_list = []

    for i in range(len(list1)):
        if list1[i] > list2[i]:
            max_list.append(list1[i])
        else:
            max_list.append(list2[i])

    return max_list


# print(listMax([1, 2, 3], [4, 1, 5]))
# print(listMax([1, 2, 3, 4], [2, 3, -7, -10]))


import random


def roll_dice():
    first_die_num = random.randint(1, 6)
    second_die_num = random.randint(1, 6)

    return (first_die_num, second_die_num)


def rolls():
    total_rolls = 1

    initial_roll = roll_dice()

    while True:
        next_roll = roll_dice()
        total_rolls += 1
        
        if set(initial_roll) == set(next_roll):
            break

    return total_rolls


# print(rolls())



class StopLight:
    def __init__(self, green_duration=30.0, yellow_duration=10.0, red_duration=40.0, current_time=0.0):
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration
        self.red_duration = red_duration
        self.current_time = current_time
    
    def __repr__(self):
        return f"StopLight({self.green_duration}, {self.yellow_duration}, {self.red_duration}, {self.current_time})"



light1 = StopLight(20.0, 15.0, 30.0, 12.0)
print(light1)

light2 = StopLight()
print(light2)


