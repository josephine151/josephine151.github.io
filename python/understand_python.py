from random import *

sides = ["kani salad", "seaweed salad", "caesar salad", "potato salad", "egg salad", "greek salad"]
main_courses = ["steak", "chicken", "salmon", "tuna", "turkey", "roast pork"]
desserts = ["ice cream", "cupcake", "popsicle", "cake pops", "jello", "pudding"]

print(desserts[0])

sides_used = []
main_courses_used = []
desserts_used = []

for index in range(len(sides)):
    rand_sides = sides[randint(0, len(sides) - 1)]
    rand_main_courses = main_courses[randint(0, len(main_courses) - 1)]

    rand_desserts = desserts[randint(0, len(desserts) - 1)]


    print("Enjoy your meal of " + str(rand_sides) + " " + str(rand_main_courses) + " " + str(rand_desserts))
