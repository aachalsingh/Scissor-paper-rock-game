#CREATING SCISSOR PAPER ROCK
import random
list = ['s','p','r']

your_chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print(" \t \t \t \t scissor,paper,rock Game\n \n")
print("s for scissor \np for paper \nr for rock \n")

# for random computer option
while no_of_chance < your_chance:
    input1 = input('scissor,paper,rock:')
    random = random.choice(list)

    if input == random:
        print("Tie . 0 points received\n ")

    # if user enter s
    if input == "s" and random == "r":
        computer_point = computer_point + 1
        print(f"your guess {input} and computer guess is {random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif input == "s" and random == "p":
        human_point = human_point + 1
        print(f"your guess {input} and computer guess is {random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter p
    elif input == "p" and random == "r":
        computer_point = computer_point + 1
        print(f"your guess {input} and computer guess is {random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    elif input == "p" and random == "s":
        human_point = human_point + 1
        print(f"your guess {input} and computer guess is {random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    # if user enter r

    elif input == "r" and random == "p":
        human_point = human_point + 1
        print(f"your guess {input} and computer guess is {random} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")


    elif input == "r" and random == "p":
        computer_point = computer_point + 1
        print(f"your guess {input} and computer guess is {random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n ")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{your_chance - no_of_chance} is left out of {your_chance} \n")

print("Game over")

if computer_point > human_point:
    print("Computer wins and you loose")

if computer_point < human_point:
    print("you win and computer loose")

print(f"your point is {human_point} and computer point is {computer_point}")
