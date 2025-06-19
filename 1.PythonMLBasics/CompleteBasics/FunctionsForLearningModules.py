import random

feet_in_miles = 5280
meters_in_kilometers = 1000
people = ["Jean McKenzie", "Louis Smith", "Armstrong Hill", "Alex White"]

def get_file_ext(file_name):
    return file_name[file_name.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)