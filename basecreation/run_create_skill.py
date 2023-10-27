from skillCreator import createSkills

f = open("input.txt", "r", encoding="utf-8")

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
    createSkills(skills, cardName, border)
    nextline = f.readline()