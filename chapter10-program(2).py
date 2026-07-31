from pathlib import Path
import os
import random

state_capitals = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta", "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston", "Lansing", "Saint Paul", "Jackson", "Jefferson City", "Helena", "Lincoln", "Carson City", "Concord", "Trenton", "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus", "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier", "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"]

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

tests = {}

testAnswers = []

def questions():
    for i in range(50):
        number = random.randint(0,49) 
        question = f"Question {i+1} What US Capital belongs to the State of {states[number]}?"
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
        stringAnswers = f"Answer for question {i+1}: {answers[0]}, {answers[1]}, {answers[2]} or {answers[3]}?"
        tests[question] = str(stringAnswers)
        testAnswers.append(f"Question {i+1}: {answer4}")
    return tests

for i in range(35):
    fileObj = open(f"/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter10-program(2)/test{i+1}", 'w')
    questions()
    formatted_questions = "\n".join(tests.keys())
    formatted_answers = "\n".join(tests.values())
    formatted_testAnswers = "\n".join(testAnswers)
    fileObj.write(formatted_questions + '\n' + formatted_answers)
    fileObj.close()

for i in range(35):
    fileObj = open(f"/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/chapter10-program(2)/testAnswers{i+1}", 'w')
    formatted_testAnswers = "\n".join(testAnswers)
    fileObj.write(str(formatted_testAnswers))
    fileObj.close()

# state can repeat multiple times
# comparing state to state capitals in the while loop
# wrong answers can repeat
# tests is never cleared, needs to be inside the funtion same with testAnswers
# every answer-key file recieves the same 1,750 answers