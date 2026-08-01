import random

state_capitals = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta", "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka", "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston", "Lansing", "Saint Paul", "Jackson", "Jefferson City", "Helena", "Lincoln", "Carson City", "Concord", "Trenton", "Santa Fe", "Albany", "Raleigh", "Bismarck", "Columbus", "Oklahoma City", "Salem", "Harrisburg", "Providence", "Columbia", "Pierre", "Nashville", "Austin", "Salt Lake City", "Montpelier", "Richmond", "Olympia", "Charleston", "Madison", "Cheyenne"]

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]



def questions():
    testAnswers = {}
    tests = {}
    numbers = []
    for i in range(50):
        number = random.randint(0,49) 
        while number in numbers:
            number = random.randint(0,49) 
        numbers.append(number)
        question = f"Question {i+1} What US Capital belongs to the State of {states[number]}?"
        answer1 = state_capitals[random.randint(0,49)]
        answer2 = state_capitals[random.randint(0,49)]
        answer3 = state_capitals[random.randint(0,49)]
        answer4 = state_capitals[number]
        while answer1 == state_capitals[number] or answer2 == state_capitals[number] or answer3 == state_capitals[number] or answer1 == answer2 or answer2 == answer3 or answer3 == answer1:
                answer1 = state_capitals[random.randint(0,49)]
                answer2 = state_capitals[random.randint(0,49)]
                answer3 = state_capitals[random.randint(0,49)]
        answers = [answer1, answer2, answer3, answer4]
        random.shuffle(answers)
        stringChoices = f"{answers[0]}, {answers[1]}, {answers[2]} or {answers[3]}."
        tests[question] = stringChoices
        testAnswers[f"Question {i+1}"] = f"Question {i+1}: {answer4}"
    return tests, testAnswers

for i in range(35):
    test, testsAnswers = questions()
    testFile = open(f"/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/Chapter10-Test-Answers/test{i+1}.txt", 'w')
    for key, value in test.items():
        testFile.write(key + '\n' + value + '\n')
    testFile.close()
    answersFile = open(f"/Users/gabrielkalel/programing/Python/Automate_Boring_stuff/Chapter10-Test-Answers/testAnswers{i+1}.txt", 'w')
    formatted_testAnswers = "\n".join(testsAnswers.values())
    answersFile.write(formatted_testAnswers)
    answersFile.close()

# state can repeat multiple times
# comparing state to state capitals in the while loop
# wrong answers can repeat
# tests is never cleared, needs to be inside the funtion same with testAnswers
# every answer-key file recieves the same 1,750 answers