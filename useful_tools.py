import random

cats_in_house = 2
people_in_house = 1000
names = ["Jennifer", "Zack", "Napoleon", "PingPong"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)
