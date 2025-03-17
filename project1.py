import random

print("this is a guessing game where you have to put the range and system will make a random number and then u have to guess it ")

rrange = int(input("enter the end range number "))

correct = random.randrange(rrange)

attempts = 3
completed = 0
while completed < attempts:
  completed += 1
  guess = int(input("enter your guess "))
  if guess == correct:
    print("BINGO")
    break
  elif completed >= attempts and guess != correct:
    print("oops you lost")
    break
  elif guess > correct:
    print("guess a lower number")
  elif guess < correct:
    print("guess a higher number")
