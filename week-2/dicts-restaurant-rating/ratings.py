"""Restaurant rating lister."""
import sys
from random import choice
import os

list_of_files = os.listdir()

for index in range(len(list_of_files)):
    print(list_of_files[index], index)

input_file = int(input("Pick the number associated with the file. "))
input_file = list_of_files[input_file]


# file_name = sys.argv[1]
restaurant_info = {}

for line in open(input_file):
    line = line.rstrip().split(":")
    restaurant_info[line[0]] = line[1]


def get_user_input():
    print("If you would like to see all restaurants, type 1.")
    print("If you would like to add a restaurant and its rating, type 2.")
    print("If you would like to update a restaurant, type 3.")
    print("If you want to quit, type 4.")
    return input()


def test_user_rating(restaurant_name):
        new_rating = input("Please give us a rating from 1-5: ")

        while new_rating not in "12345":
            print("Please enter a number between 1 and 5.")
            new_rating = input()

        restaurant_info[restaurant_name] = new_rating


user_input = get_user_input()

while user_input != "4":

    if user_input == "1":
        for key in sorted(restaurant_info):
            print("{} is rated at {}.".format(key, restaurant_info[key]))

    elif user_input == "2":
        new_restaurant = input("Please give us a restaurant name: ")
        test_user_rating(new_restaurant)

    elif user_input == "3":
        user_random = input("Do you want to update a random restaurant? y/n: ")

        if user_random.lower() == "y":
            random_restaurant = choice(list(restaurant_info.keys()))
            print(random_restaurant, "is rated at",
                  restaurant_info[random_restaurant] + ".")
            test_user_rating(random_restaurant)

        elif user_random.lower() == "n":
            print("These are the restaurants currently rated.")
            restaurant_keys = list(restaurant_info.keys())

            for i in range(len(restaurant_keys)):
                print(restaurant_keys[i], i)

            user_number = int(input("Please enter the number associated with the restaurant you want to rate."))

            while user_number < 0 or user_number > len(restaurant_keys):
                print("Please enter a valid restaurant number.")
                user_number = int(input())

            test_user_rating(restaurant_keys[user_number])

    user_input = get_user_input()
