from PIL import Image, ImageFont, ImageDraw, ImageFilter
from base_editor_helper import color_info, skillname_text_creator, get_rows, drawChar   


###############################################################################################################
###############################################################################################################
#Parse Input
###############################################################################################################
f = open("input.txt", "r", encoding="utf-8")

line1 = f.readline().split('|')
name = line1[0].strip()
title = line1[1].strip()
#print(name + ', ' + title)

line2 = f.readline().split('|')
classtxt = line2[0].strip()
cost = line2[1].strip()
cc = None
promo = False
if len(line2) > 2:
    cc = line2[2].strip()
    promo = True
    #print(cc)
#    print(classtxt + ', ' + cost + '/' + cc)
#else:
#    print(classtxt + ', ' + cost)

line3 = f.readline().split('|')
attr = []
for element in line3:
    attr.append(element.strip())
color = attr[0].strip()
color = color.lower()
#print(attr)
print(color)

line4 = f.readline().split('|')
atk = line4[0].strip()
sup = line4[1].strip()
rang = line4[2].strip()

skills = []
nextline = f.readline()
isSupSkl = False
supskl = 0
supskl1 = None
supskl2 = None
while nextline and not isSupSkl:
    if nextline[0] == '|':
        isSupSkl = True
    else:
        skills.append(nextline.strip())
        nextline = f.readline()
if isSupSkl:
    supskl1 = nextline.strip()
    supskl = 1
    nextline = f.readline()
    if nextline:
        if nextline[0] == '|':
            supskl2 = nextline.strip()
            supskl = 2
#print(skills)
#print(supskl)
###############################################################################################################

###############################################################################################################
###############################################################################################################
#Constants
###############################################################################################################
skillatr = ['lis','bs','hs','cp','db','dv','ts','fs','ccs','cf','gs','us','is','as','lvs2','lvs3','lvs4','lvs5','lvs7']
skilltypes = ['act','auto','cont','bond','spec','supp','hand']

attributes = ['armor','axe','beast','black','blue','bow','brawl','brown','dragon','dragonstone','knife',
            'fang','female','flier','green','lance','male','mirage','monster','purple','red',
            'staff','sword','tome','white','yellow',
            'act','auto','cont','bond','spec','supp','hand','opt',
            #'lis','bs','hs','cp','db','dv','ts','fs','ccs','cf','us','is','as','lvs2','lvs3','lvs4','lvs5','lvs7',
            'flip1','flip2','flip3','flip4','flip5','tap']

actions = ['flip1','flip2','flip3','flip4','flip5','tap']
###############################################################################################################

full = Image.open('attributes/full2.png')

output = full.copy()
#output.paste(bot, (0, h - h2), bot)

#output.paste(top, (0, 0), top)

#attributes
y = 470
i = 0
# for a in attr:
#     atrpic = Image.open('attributes/' + a + '.png')
#     output.paste(atrpic, (29, y))
#     y = y + 97


### adding the skills
# line character limit 60, pixel length is 1090
# get rows
fontsize = 8
font = ImageFont.truetype('georgiab.ttf', fontsize)
charwid = 4
rowheight = 12
rowextra = 2
rowlen = 282
rows = get_rows(skills, charwid, rowheight, rowextra, fontsize, attributes, font, rowlen-25)
print("ROWS:")
print(rows)

# set up space on the card for effects
boty = 100
bgcx, bgcy = output.size
skillx = 25
skilly = bgcy - boty - (rows * rowheight) - (len(skills) * rowextra)
skilltitle = False
#font = ImageFont.truetype('Cousine-Regular.ttf', 40)

# draw the effects on the card
sklcnt = 0
ypos = skilly
for i in skills:
    if i != '':
        xpos = skillx
        skilltext = i.split('|')
        idx = 0
        while idx < len(skilltext):
            #print(idx)
            if idx == 0:
                skillname_text_creator(skilltext[0], charwid, rowheight, rowextra, fontsize, 'default')
                imskl = Image.open('skillname.png', mode = "r")
                imsklend = Image.open('rightSkl.png', mode = "r")
                imsklstrt = Image.open('leftSkl.png', mode = "r")
                x,y = imskl.size
                if '*' not in skilltext[0]:
                    output.paste(imsklstrt, (xpos,ypos), imsklstrt)
                    output.paste(imskl, (xpos+3,ypos))
                    output.paste(imsklend, (xpos+x+3,ypos), imsklend)
                    xpos = xpos + x + 18
                else:
                    output.paste(imskl, (xpos,ypos))
                    output.paste(imsklend, (xpos+x,ypos), imsklend)
                    xpos = xpos + x + 15
                ypos = ypos + rowextra
                #print(ypos)
            elif skilltext[idx].lower() in attributes:
                xpos = xpos - charwid
                skltxt = skilltext[idx].lower()
                imskl = Image.open('icons/'+ skltxt +'.png')
                x,y = imskl.size
                # if y > rowheight:
                #     #print(y)
                #     ratio = rowheight/y
                #     imskl = imskl.resize((int(ratio * x),rowheight))
                #     x,y = imskl.size
                #     print("skill x: " + str(x))
                #     print("skill y: " + str(y))
                # elif y < rowheight:
                #     ratio = rowheight/y
                #     imskl = imskl.resize((int(ratio * x),rowheight))
                #     x,y = imskl.size
                xpos = xpos + x
                ypos = ypos - rowextra
                print(skilltext[idx].lower())
                if xpos > rowlen:
                    xpos = skillx
                    ypos = ypos + rowheight
                    #print(ypos)
                    if y == 30:     # for smaller images
                        output.paste(imskl, (xpos,ypos + 10), imskl)
                    else:
                        output.paste(imskl, (xpos,ypos + 1), imskl)
                    xpos = xpos + x
                else:
                    if y == 30:     # for smaller images
                        output.paste(imskl, (xpos - x, ypos + 10), imskl)
                    else:
                        output.paste(imskl, (xpos - x, ypos), imskl)
                ypos = ypos + rowextra
            elif skilltext[idx].lower() in skillatr:
                xpos = xpos - charwid
                skltxt = skilltext[idx].lower()
                imskl = Image.open('skillheaders/'+ skltxt +'.png')
                x,y = imskl.size
                if y > rowheight:
                    #print(y)
                    ratio = rowheight/y
                    imskl = imskl.resize((int(ratio * x),rowheight))
                    x,y = imskl.size
                elif y < rowheight:
                    ratio = rowheight/y
                    imskl = imskl.resize((int(ratio * x),rowheight))
                    x,y = imskl.size
                xpos = xpos + x
                if xpos > rowlen:
                    xpos = skillx
                    ypos = ypos + rowheight
                    #print(ypos)
                    output.paste(imskl, (xpos,ypos), imskl)
                    xpos = xpos + x
                else:
                    output.paste(imskl, (xpos - x,ypos), imskl)
            else:
                strskl = skilltext[idx].split(' ')
                j = 0
                while j < len(strskl):
                    xpos = xpos + int(font.getlength(strskl[j]))
                    if xpos > rowlen:
                        xpos = skillx
                        ypos = ypos + rowheight

                        draw = ImageDraw.Draw(output)
                        drawChar(draw, xpos, ypos, strskl[j], font)
                        xpos = xpos + int(font.getlength(strskl[j]))
                        #print(ypos)
                    else:
                        xpos = xpos - int(font.getlength(strskl[j]))

                        draw = ImageDraw.Draw(output)
                        drawChar(draw, xpos, ypos, strskl[j], font)
                        xpos = xpos + int(font.getlength(strskl[j]))
                    # accounting for the space after each word
                    xpos = xpos + charwid
                    j = j + 1
            idx = idx + 1
        ypos = ypos + rowheight

charwid = 18
rowheight = 33
rowextra = 3
fontsize = 30
font = ImageFont.truetype('Cousine-Regular.ttf', 30)

output.save("output/fulloutput.png", quality=95)