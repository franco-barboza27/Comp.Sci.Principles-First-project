#make a points system CHECK
#FIGURE OUT HOW TO USE RANDOM
#make the result checker function
#make a way for questions to correspond to answers
#make questions CHECK
#make the questions more efficient
import random

#question set

one = "What is Luke's last name?"
two = "Where do babies come from?"
three = "What is the mitochondria?"
four = "Where is Utah?"
five = "What is an anime that Ms.LaRose likes?"

#answer set

aOne = "Murdock"
aTwo = "Storks" 
aThree = "THE POWERHOUSE OF THE CELL"
afour = "The USA"
afive = "Assasination Classroom"

result = False

def questionResult():
  totalPoints = 0
  if result == False:
    print("You are wrong")
  else:
     totalPoints = totalPoints + 100
     print("You are correct! You earned 100 POINTS.")
     print("Your current number of POINTS is", totalPoints)

def questionAnswer():
  