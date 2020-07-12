import webbrowser
import random

print("This program will generate a random\nKattis Question based on your Difficulty Peferences!")
print("Please enter your difficulty range\n")
lowerBound = float(input("Please enter Your Lower Bound: "))
upperBound = float(input("Please enter Your Upper Bound: "))

class Problem:

    def __init__(self,Id,diff):
        self.Id = Id
        self.diff = diff

    def getId(self):
        return self.Id

    def getDiff(self):
        return self.diff

data = open('data.txt','r')
lines = data.readlines()

problems = []

for i in lines:
    x = i.split()
    if (float(x[1]) >=lowerBound and float(x[1]) <=upperBound):
        problems.append(Problem(x[0],x[1]))

random.shuffle(problems)

ID = problems[0].getId()

URL = 'https://open.kattis.com/problems/' + ID

webbrowser.open(URL,new=2)

