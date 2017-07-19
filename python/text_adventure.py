start = '''
Woohoo!!! It's time for another day of Girls Who Code!
Time to head out for Adobe. How will you get there?
You can either take the subway, bus, or walk.
'''


print(start)


print("Type 'subway' to go on the subway, 'bus' to go on the bus, or 'walk' to go walk.")
user_input = input()
if user_input == "subway":
    print("You decide to go on the subway but, oh no, your metrocard has run out of money. Will you add money to the card or go home? Type 'go home' to go home or 'add money' to go on the subway")
    user_input = input()
    while user_input != 'go home' and user_input != 'add money':
        print("You decide to go on the subway but, oh no, your metrocard has run out of money. Will you add money to the card or go home? Type 'go home' to go home or 'add money' to go on the subway")
        user_input = input()

    if user_input == "go home":
        print("So lazy! Sorry, no Girls Who Code for you today")
    elif user_input == "add money":
        print("Your train is here. Do you try to find a seat or will you stand up? Type 'seat' to sit down or 'stand' to stand")
        user_input = input()
        if user_input == "seat":
            print("Welp, you fell asleep and missed your stop. Sorry! No Girls Who Code for you today.")
        elif user_input == "stand":
            print("Oh no, the train suddenly stopped, you fell down. Do you try to get up or do you stay on the floor? Type 'get up' or 'stay on the floor'")
            user_input = input()
            if user_input == "stay on the floor":
                print("Sorry, it's going to be a long ride. Have fun on the subway! No Girls Who Code for you today.")
            elif user_input == "get up":
                print("You persevered! Congratulations, you are now on the 4th floor. Get ready to have the best summer ever by coding at Girls Who Code Adobe.")
    else:
        print("type 'add money' or 'go home'")
        user_input = input()
        # finished the story by writing what happens

elif user_input == "bus":
    print("You decide to go on the bus. Eeeeeek! A weird, smelly guy sits in the seat next to you, do you move or stay seated?") # finished the story writing what happens

elif user_input == "walk":
    print("You decide to walk but you forgot how out of shape you are, which means you can no longer make it all the way to Adobe! Sorry! No Girls Who Code for you today. :(")


else:
    print("type 'subway' 'bus' or 'walk'")
    user_input = input()
