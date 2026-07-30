from pathlib import Path
import os
import random


for i in range(35):
    fileObj = os.makedirs(f"/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter10-program(2)/test{i+1}")

state_capitals = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta", "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston", "Lansing", "Saint Paul", "Jackson", "Jefferson City", "Helena", "Lincoln", "Carson City", "Concord", "Trenton", "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus", "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier", "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"]

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

def questions():
    for i in range(50):
        number = random.randint(0,49) 
        question = f"What US Capital belongs to the State of {states[number]}"
        answer1 = state_capitals[random.randint(0,49)]
        answer2 = state_capitals[random.randint(0,49)]
        answer3 = state_capitals[random.randint(0,49)]
        answer4 = state_capitals[number]
        while answer1 == states[number] or answer2 == states[number] or answer3 == states[number]:
            if answer1 == number:
                answer1 = state_capitals[random.randint(0,49)]
            if answer2 == number:
                answer2 = state_capitals[random.randint(0,49)]
            if answer3 == number:
                answer3 = state_capitals[random.randint(0,49)]
        answers = [answer1, answer2, answer3, answer4]
        random.shuffle(answers)
        print(question)
        print(answers)

questions()

# left: 
# Writes the quizzes to 35 text files 
# Writes the answer keys to 35 text files
