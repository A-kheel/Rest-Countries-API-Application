import random

def displayMenu():

    print("DIFFICULTY LEVEL\n1. Easy\n2. Moderate\n3. Advanced")
    choice = input("Type it in lowercase please(easy/moderate/advanced): ")
    return choice

def randomInt(difficulty):

    if difficulty == 'easy':
        return 1, 9
    
    elif difficulty == 'moderate':
        return 10, 99
    
    elif difficulty == 'advanced':
        return 100, 999

def decideOperation():
 
    return random.choice(['+', '-'])

def displayProblem(num, num1, math, question):

    if num1 > num:
            num, num1 = num1, num
  
    answerr = int(input(f"{question}. {num} {math} {num1} = "))
    return answerr

def isCorrect(answerr, num, num1, math):

    if math == '-':
        if num1 > num:
            num, num1 = num1, num
        answer = num - num1
    elif math == '+':
        answer = num + num1

    if answerr == answer:
        print("Correct")
        return 10
    else:
        answerr = int(input("wrong, try again: "))
        if answerr == answer:
            print("correct")
            return 5
        else:
            print("wrong.The correct answer was",answer)
            return 0
        
def displayResults(score):

    print("\nYour final score is:", score, "/100")
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
    print("Your grade:", grade,"congrats loser")

def stuff():
    difficulty = displayMenu()
    min_num, max_num = randomInt(difficulty)
    score = 0

    for i in range(1, 11):
        num = random.randint(min_num, max_num)
        num1 = random.randint(min_num, max_num)
        math = decideOperation()
        answerr = displayProblem(num, num1, math, i)
        points = isCorrect(answerr, num, num1, math)
        score += points
        print(score, "/100")

    displayResults(score)

def looper():
    
    game = 'y'
    while game == 'y':
        stuff()
        game = input("play again? (y/n): ")


looper()
