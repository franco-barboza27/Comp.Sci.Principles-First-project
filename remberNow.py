#make a points system 
#FIGURE OUT HOW TO USE RANDOM
#make the result checker function
#make a way for questions to correspond to answers
#make questions CHECK
#make the questions more efficient
#make an introduction
import random
import sys

print("Greetings, this is a quiz I made to practice coding")
print("I made it for fun, and it is inspired by the first project that they are making in CS 3")
startingInput = input("Do you wish to start? Input Y or N\n")

if startingInput == "Y":
  print("Ok, the quiz will now begin")
  totalPoints = 0
else:
  sys.exit("Oh, then what are you even doing here???")
  

questionRando = random.randint (1, 5)



result = False
  
  

def questionResult():
  if result == False:
    print("You are wrong")
  else:
     totalPoints = totalPoints + 100
     print("You are correct! You earned 100 POINTS.")
     print("Your current number of POINTS is", totalPoints)



#question set

qOne = "What is Luke's last name?"
qTwo = "Where do babies come from?"
qThree = "What is the mitochondria?"
qFour = "Where is Utah?"
qFive = "What is an anime that Ms.LaRose likes?"

def rando():
  if questionRando == 1:
    print(qOne)
  elif questionRando == 2:
    print(qTwo)
  elif questionRando == 3:
    print(qThree)
  elif questionRando == 4:
    print(qFour)
  else:
    print(qFive)
  userAnswer = input("Input answer: \n")
  questionRando = random.randint (1, 5)
#answer set
aOne = "Murdock"
aTwo = "Storks" 
aThree = "THE POWERHOUSE OF THE CELL"
afour = "The USA"
afive = "Assasination Classroom"

rando()