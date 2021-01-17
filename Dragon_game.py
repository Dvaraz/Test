import string
import random
import time


def name_generator():
    alphabet = string.ascii_lowercase
    name = ""
    for i in range(random.randint(4, 6)):
        name += alphabet[(random.randint(0, len(alphabet) - 1))]
    return name.capitalize()


class Dragon:

    def __init__(self, name):
        self.name = name
        self.health = 100

    def set_health(self, health):
        self.health = health

    def get_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"You hurt me. Now my health is {self.health}.")

    def is_alive(self):
        return self.health > 0

    def get_information(self):
        print(f"My name is {self.name} and my health power is {self.health}.\nI GONNA SMASH YOU!!!!\n")


class Hero:

    def __init__(self, power, name):
        self.name = name
        self.health = 100
        self.power = power

    def set_power(self, power):
        self.power = power

    @staticmethod
    def name_chose():
        name = input("What is your name? ")
        return name

    @staticmethod
    def race_chose():
        race = input("What is your race hero?\nElf\nHuman\nDwarf\n:").lower()
        power = 0
        if race == "elf":
            power = 50
        elif race == "human":
            power = 60
        elif race == "dwarf":
            power = 70
        return power

    def get_information(self):
        print(f"My name is {self.name} and my power is {self.power}\n")


def enemy_generator(enemy):
    for i in range(int(input("How many enemy's do you want to slave stranger? ")) + 1):
        enemy.append(Dragon(name_generator()))
    print("HA-HA-HA!!!!! YOU WILL GET WHAT YOU ARE DESERVE!!!!")
    time.sleep(1)

    for dragon in enemy:
        dragon.set_health(random.randint(150, 250))
        time.sleep(1)
        dragon.get_information()
    return enemy


def main_game():

    enemy = []
    player_1 = Hero(Hero.race_chose(), Hero.name_chose())
    enemy_generator(enemy)
    player_1.get_information()

    while len(enemy) > 0:
        enemy[0].get_information()
        action = input("What you are going to do hero? Attack or block? ").lower()
        if action == "attack":
            enemy[0].get_damage(player_1.power)
        elif action == "block":
            print("You are raise block")

        if not enemy[0].is_alive():
            time.sleep(0.3)
            print(f"You  are winning son. {enemy[0].name} is dying!!!")
            enemy.pop(0)
    else:
        print("You are win!!!!")


main_game()
