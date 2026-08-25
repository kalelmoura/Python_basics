import random

streak = 0

for i in range(10000):
    flip = []
    for i in range(100):
        flip.append(random.choice(["H", "T"]))

    for i in range(95):
        if flip[i] == flip[i + 1] == flip[i + 2] == flip[i + 3] == flip[i + 4] == flip[i + 5]:
            streak +=1
            break

print("The percentage of 100 coin flips that have a 6 Heads or Tails streaks is: " + str(streak / 100) + "%")