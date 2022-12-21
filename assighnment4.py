#write a program that accepts a sentance and
#calculate the number of digits and numbers
#suppose the following input is supplies to the program
#output should be LETTER 10 #DIGITS 3

sentenceEntered=input("Enter a sentence")
digits=0
letters=0
for cnt in sentenceEntered:
    if cnt.isdigit():
        digits=digits+1
    elif cnt.isalpha():
        letters=letters+1

print("letters",letters)
print("dig",digits)

#Assignment2
# program will first  randomly generate a number unknown to the user
#user need to guess what that number is, if user guess the wrong the program should
# return some sort of indication as to how wrong Eg(The number is too high or too low)
#if the user guess correctily then a positive indication should appear
#maximum of 5 tries . You will need function to check if the user input is actual number,
#to see the difference between the input number and random
from random import randint
def guess(x):
  it = randint(0, 10)
  if x == it:
      print("You got it!")
  elif x > it:
      print("too high")
  else:
      print("too low")

for i in range(5):
    x=int(input("\n Guess number" ))
    print (guess(x))