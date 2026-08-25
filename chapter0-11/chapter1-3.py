# Script 1
# print("Hello, what's your name?")
# name = input(">")
# print("Hello", name)
# print("The length of your name is", len(name))
# print("How old are you?")
# age = int(input(">"))
# print("You will be", (age + 1), "in 1 year")

# Script 2
# spam = 1
# if spam == 1:
#     print("Hello")
# elif spam == 2:
#     print("Howdy")
# else:
#     print("Greetings")

# Script 3
# import random
# for i in range(5):
#     print(random.randint(1, 10))

# Script 4
# import random
# number = random.randint(1,20)
# print("I am thinking of a number between 1 and 20")
# print("Take a guess")
# i = 0
# while True:
#     guess = int(input(">"))
#     if guess < number:
#         print("Your guess was to low, try again")
#         i=+1
#         continue
#     elif guess > number:
#         print("yout guess was too high, try again!")
#         i+=1
#         continue
#     elif guess == number:
#         i=+1
#         print("Good job! You got it in " + str(i) + " guesses!")
#         break

# Script 5
# import random
# wins = 0
# losses = 0
# ties = 0

# print("ROCK, PAPER, SCISSORS")

# while wins != 3 or losses != 3:
#     move_machine = random.choice(["r", "p", "s"])
#     print(str(wins) + " Wins, " + str(losses) + " Losses, " + str(ties) + " Ties")
#     print("Enter yout move: (r)ock (p)aper (s)cissors or (q)uit")
#     move_human = input(">")
#     if move_human == "q":
#         print("See you later :(")
#         break 
#     else:
#         if move_human == move_machine:
#             ties+=1
#         elif move_human == "r" and move_machine == "s":
#             wins+=1
#         elif move_human == "r" and move_machine == "p":
#             losses+=1
#         elif move_human == "s" and move_machine == "p":
#             wins+=1
#         elif move_human == "s" and move_machine == "r":
#             losses+=1
#         elif move_human == "p" and move_machine == "r":
#             wins+=1
#         elif move_human == "p" and move_machine == "s":
#             losses+=1
#     continue


    