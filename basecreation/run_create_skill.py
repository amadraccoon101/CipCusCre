from skillCreator import createSkills
import sys, threading

fname = "AM01"
f = open("inputAM01.txt", "r", encoding="utf-8")
fntsize = 8

nextline = f.readline()
while nextline:
    cardName = nextline.strip()
    bordertxt = f.readline().strip()
    #bordertxt = bordertxt.strip()
    border = True
    if bordertxt == "false":
        border = False
    skills = []
    nextline = f.readline()
    while nextline and nextline.strip() != "---------------":
        skills.append(nextline)
        nextline = f.readline()
        print(nextline)
    print(border)
    print(cardName)
    print(skills)
    createSkills(skills, cardName, border, fname, fntsize)
    nextline = f.readline()

limit = sys.getrecursionlimit()
print(limit)
size = threading.stack_size()
print(size)