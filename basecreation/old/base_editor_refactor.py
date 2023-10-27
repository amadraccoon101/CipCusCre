from PIL import Image, ImageFont, ImageDraw, ImageFilter
from base_editor_helper import color_info, skillname_text_creator, get_rows

### stats, later change to import stats from text or input
### PARAMETERS TO CHANGE
title = "Duessel, Traitor to the Empire"
classtxt = "Great Knight"
color = 'purple'
atk = 70
sup = 20
rang = '1'
attrib = 'purple+male+axe+beast'
promo = True
supskl = 0
cost = 3
cc = 2
skills = ["Shield of Seals||CONT| During your opponent's turn, if you have 1 or more orbs, all allies gain +10 attack.",
          "Come, Join Us!||AUTO||OPT| [|flip1|, Send 1 card from your hand to the Retreat Area] At the beginning of your Deployment Phase, you may pay the cost: Reveal a |Red| card from your hand. Until the end of the turn, the Deployment Cost of that card becomes 0.",
          "Origin Falchion||CONT| If this unit is attacking a |Dragon|, this unit gains +20 attack. The |ACT|, |AUTO|, and |SPEC| skills of non-Main Character |Dragonstone| enemies cannot activate.",
          ""]
imgname = 'Duessel1.jpg'
#skills = [#"Knight General of Etruria| |ACT| |OPT| [|flip2|] Choose 1 |Beast| ally from your Retreat Area and deploy it.",
          #'"If we take our time, we can win."| |CONT| During your turn, you have 3 or more |Beast| allies, all |Beast| allies gain +10 attack.',
          #'"We must defend those who cannot defend themselves."| |AUTO| When a |Beast| ally is deployed by the effect of a skill, that ally gains +10 attack until the end of your opponent\'s next turn.',
          #""]
supskl1 = ''
#supskl1 = "ATKSUP|Attack Emblem| |SUPP| Until the end of this combat, your attacking unit gains +20 attack."
supskl2 = ''
#attrib = 'red+male+sword'
skillatr = ['lis','bs','hs','cp','db','dv','ts','fs','ccs','cf','us','is','as','lvs2','lvs3','lvs4','lvs5','lvs7']
skilltypes = ['act','auto','cont','bond','spec','supp','hand']

attributes = ['armor','axe','beast','black','blue','bow','brawl','brown','dragon','dragonstone','knife',
              'fang','female','flier','green','lance','male','mirage','monster','purple','red',
              'staff','sword','tome','white','yellow',
              'act','auto','cont','bond','spec','supp','hand','opt',
              #'lis','bs','hs','cp','db','dv','ts','fs','ccs','cf','us','is','as','lvs2','lvs3','lvs4','lvs5','lvs7',
              'flip1','flip2','flip3','flip4','flip5','tap']

actions = ['flip1','flip2','flip3','flip4','flip5','tap']

loc = color_info(color, promo, cost, cc, supskl)

base = None
costbase = None

### loading bases
if color is 'red':
    if supskl > 0:
        base = Image.open(color + '/supbase.png')
    else:
        base = Image.open(color + '/base.png')
    if promo:
        if cost - 1 == cc:
            costbase = Image.open(color + '/promocostbase.png')
        else:
            costbase = Image.open(color + '/mastercostbase.png')
    else:
        costbase = Image.open(color + '/basecostbase.png')
elif color is 'purple':
    if supskl > 0:
        if promo:
            base = Image.open(color + '/supbasepromo.png')
        else:
            base = Image.open(color + '/supbase' + str(supskl) + '.png')
    else:
        base = Image.open(color + '/base.png')
    if promo:
        costbase = Image.open(color + '/promocostbase.png')
    else:
        costbase = Image.open(color + '/basecostbase.png')

### overlaying atk, sup, and range
bot = base.copy()
image_editable = ImageDraw.Draw(bot)
#statfont = ImageFont.truetype('courier-prime-bold-italic.ttf',200)
#atkstr = str(atk)
#image_editable.text((loc['x']['atk']-30, loc['y']['atk']-20), atkstr, (255,255,255), font=statfont)
#statfont = ImageFont.truetype('courier-prime-bold-italic.ttf',170)
#supstr = str(sup)
#image_editable.text((loc['x']['sup']-20, loc['y']['sup']-20), atkstr, (255,255,255), font=statfont)
atkpic = Image.open(color + '/atk/' + str(atk) + '.png')
bot.paste(atkpic, (loc['x']['atk'], loc['y']['atk']))
suppic= Image.open(color + '/sup/' + str(sup) + '.png')
bot.paste(suppic, (loc['x']['sup'], loc['y']['sup']))
ranpic = Image.open(color + '/range/' + rang + '.png')
bot.paste(ranpic, (loc['x']['range'], loc['y']['range']))

### writing name and class
#name location = (270, 300)
title_font = ImageFont.truetype('arial.ttf', 60)
#30 character limit for title
if len(title) <= 30:
    image_editable.text((loc['x']['title'], loc['y']['title']), title, (237, 230, 211), font=title_font)
else:
    title_font = title_font = ImageFont.truetype('arial.ttf', 50)
    image_editable.text((loc['x']['title'], loc['y']['title'] + 10), title, (237, 230, 211), font=title_font)
#Starting Coordinates: Pillow library uses a Cartesian pixel coordinate system, with (0,0) in the upper left corner.
#Text: String between single or double quotations
#Text color in RGB format
#Font style
class_font = ImageFont.truetype('arial.ttf', 50)
image_editable.text((loc['x']['class'], loc['y']['class']), classtxt, (0, 0, 0), font=class_font)

#bot.save("bot.png", quality = 95)
full = Image.open('attributes/full.png')

w, h = full.size
w2, h2 = bot.size

output = full.copy()
output.paste(bot, (0, h - h2), bot)

### putting the numbers on the deployment cost
dcpic = Image.open(color + '/cost/' + str(cost) + 'cost.png')
costbase.paste(dcpic, (loc['x']['deployCost'], loc['y']['deployCost']))
if promo is True:
    if cost - 1 == cc:
        ccpic = Image.open(color + '/cost/' + str(cc) + 'cc.png')
    else:
        ccpic = Image.open(color + '/cost/' + str(cc) + 'mc.png')
    costbase.paste(ccpic, (loc['x']['classChange'], loc['y']['classChange']))
output.paste(costbase, (0, 0), costbase)

### adding the attributes
attr = attrib.split('+')
y = 470
i = 0
for a in attr:
    if i < 6:
        atrpic = Image.open('attributes/' + a + '.png')
        output.paste(atrpic, (29, y))
        y = y + 97
    i = i + 1

#output.save("nopic.png", quality = 95)

### adding the background image
ogpic = Image.open(imgname)
bgc = ogpic.resize((1466, 2078))

bgc.paste(output, (0,0), output)

#bgc.save("output.png", quality = 95)

### adding the skills
# line character limit 60, pixel length is 1090
# get rows
font = ImageFont.truetype('georgiab.ttf', 40)
charwid = 24
rowheight = 48
rowextra = 8
fontsize = 40
rows = get_rows(skills, charwid, rowheight, rowextra, fontsize, attributes, font)

# set up space on the card for effects
botx, boty = bot.size
bgcx, bgcy = bgc.size
skillx = loc['x']['atk']
skilly = bgcy - boty - (rows * rowheight) - (len(skills) * rowextra)
skilltitle = False
#font = ImageFont.truetype('Cousine-Regular.ttf', 40)

# draw the effects on the card
sklcnt = 0
ypos = skilly
for i in skills:
    if i is not '':
        xpos = skillx
        skilltext = i.split('|')
        idx = 0
        while idx < len(skilltext):
            #print(idx)
            if idx is 0:
                skillname_text_creator(skilltext[0], charwid, rowheight, rowextra, fontsize, 'default')
                if '*' not in skilltext[0]:
                    imsklstrt = Image.open('leftSkl.png', mode = "r")
                    bgc.paste(imsklstrt, (xpos,ypos+4), imsklstrt)
                imskl = Image.open('skillname.png', mode = "r")
                bgc.paste(imskl, (xpos+10,ypos+3))
                imsklend = Image.open('rightSkl.png', mode = "r")
                x,y = imskl.size
                bgc.paste(imsklend, (xpos+x+10,ypos+3), imsklend)
                xpos = xpos + x + 20
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
                if xpos > 1350:
                    xpos = skillx
                    ypos = ypos + rowheight
                    #print(ypos)
                    bgc.paste(imskl, (xpos,ypos), imskl)
                    xpos = xpos + x
                else:
                    if y >= 44:
                        bgc.paste(imskl, (xpos - x,ypos), imskl)
                    else:
                        bgc.paste(imskl, (xpos - x,ypos + int((rowheight - y)/2)+5), imskl)
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
                if xpos > 1350:
                    xpos = skillx
                    ypos = ypos + rowheight
                    #print(ypos)
                    bgc.paste(imskl, (xpos,ypos), imskl)
                    xpos = xpos + x
                else:
                    bgc.paste(imskl, (xpos - x,ypos), imskl)
            else:
                strskl = skilltext[idx].split(' ')
                j = 0
                while j < len(strskl):
                    xpos = xpos + int(font.getsize(strskl[j])[0])
                    if xpos > 1350:
                        xpos = skillx
                        ypos = ypos + rowheight

                        draw = ImageDraw.Draw(bgc)
                        # layer 1
                        draw.text((xpos, ypos), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-1, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-1, ypos+1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos+1), strskl[j], font=font, fill=(255,255,255))
                        # layer 2
                        draw.text((xpos-2, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-2, ypos+1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos+1), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-1, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-1, ypos+2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos+2), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-2, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-2, ypos+2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos+2), strskl[j], font=font, fill=(255,255,255))
                        # layer 3
                        draw.text((xpos-3, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-3, ypos+2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos+2), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-2, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-2, ypos+3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos+3), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-3, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-3, ypos+1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos+1), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-1, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-1, ypos+3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos+3), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-3, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-3, ypos+3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos+3), strskl[j], font=font, fill=(255,255,255))
                        # layer 4
                        draw.text((xpos-4, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-4, ypos+2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos+2), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-2, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-2, ypos+4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos+4), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-4, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-4, ypos+1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos+1), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-1, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-1, ypos+4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos+4), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-4, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-4, ypos+3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos+3), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-3, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-3, ypos+4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos+4), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-4, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-4, ypos+4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos+4), strskl[j], font=font, fill=(255,255,255))
                        # writing
                        draw.text((xpos, ypos), strskl[j], font=font, fill=(0,0,0))
                        #draw.text((xpos-1, ypos-1), strskl[j], font=font, fill=(0,0,0))
                        #draw.text((xpos+1, ypos-1), strskl[j], font=font, fill=(0,0,0))
                        #draw.text((xpos-1, ypos+1), strskl[j], font=font, fill=(0,0,0))
                        #draw.text((xpos+1, ypos+1), strskl[j], font=font, fill=(0,0,0))
                        xpos = xpos + int(font.getsize(strskl[j])[0])
                        #print(ypos)
                    else:
                        xpos = xpos - int(font.getsize(strskl[j])[0])

                        draw = ImageDraw.Draw(bgc)
                        # layer 1
                        draw.text((xpos, ypos), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-1, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-1, ypos+1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos+1), strskl[j], font=font, fill=(255,255,255))
                        # layer 2
                        draw.text((xpos-2, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-2, ypos+1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos+1), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-1, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-1, ypos+2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos+2), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-2, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-2, ypos+2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos+2), strskl[j], font=font, fill=(255,255,255))
                        # layer 3
                        draw.text((xpos-3, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-3, ypos+2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos+2), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-2, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-2, ypos+3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos+3), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-3, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-3, ypos+1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos+1), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-1, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-1, ypos+3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos+3), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-3, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-3, ypos+3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos+3), strskl[j], font=font, fill=(255,255,255))
                        # layer 4
                        draw.text((xpos-4, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos-2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-4, ypos+2), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos+2), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-2, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-2, ypos+4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+2, ypos+4), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-4, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos-1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-4, ypos+1), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos+1), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-1, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-1, ypos+4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+1, ypos+4), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-4, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos-3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-4, ypos+3), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos+3), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-3, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-3, ypos+4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+3, ypos+4), strskl[j], font=font, fill=(255,255,255))

                        draw.text((xpos-4, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos-4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos-4, ypos+4), strskl[j], font=font, fill=(255,255,255))
                        draw.text((xpos+4, ypos+4), strskl[j], font=font, fill=(255,255,255))
                        # writing
                        draw.text((xpos, ypos), strskl[j], font=font, fill=(0,0,0))
                        #draw.text((xpos-1, ypos-1), strskl[j], font=font, fill=(0,0,0))
                        #draw.text((xpos+1, ypos-1), strskl[j], font=font, fill=(0,0,0))
                        #draw.text((xpos-1, ypos+1), strskl[j], font=font, fill=(0,0,0))
                        #draw.text((xpos+1, ypos+1), strskl[j], font=font, fill=(0,0,0))
                        xpos = xpos + int(font.getsize(strskl[j])[0])
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

# adding support skill 1
if supskl1 is not "":
    skilltext = supskl1.split('|')
    supskllogo1 = Image.open('attributes/' + skilltext[0] + '.png')
    x,y = supskllogo1.size
    bgc.paste(supskllogo1, (loc['x']['suplogo1'], (2078 - boty) + loc['y']['suplogo1']))

    xpos = loc['x']['suplogo1'] + x + 10
    ypos = (2078 - boty) + loc['y']['suplogo1']
    print(ypos)
    #print(skilltext)
    skillname_text_creator(skilltext[1], charwid, rowheight, rowextra, fontsize, color)
    imskl = Image.open('skillname.png')
    bgc.paste(imskl, (xpos,ypos))
    x,y = imskl.size
    xpos = xpos + x
    ypos = ypos + rowextra
    print(ypos)

    count = 2
    while count < len(skilltext):
        if skilltext[count] is not '':
            if skilltext[count].lower() in attributes:
                xpos = xpos - charwid
                skltxt = skilltext[count].lower()
                imskl = Image.open('icons/'+ skltxt +'.png')
                x,y = imskl.size
                if y > rowheight:
                    #print(y)
                    ratio = rowheight/y
                    imskl = imskl.resize((int(ratio * x),rowheight))
                    x,y = imskl.size
                xpos = xpos + x
                if xpos > loc['x']['supskl1']:
                    xpos = loc['x']['suplogo1'] + 120
                    ypos = ypos + rowheight
                    print(ypos)
                    bgc.paste(imskl, (xpos,ypos))
                    xpos = xpos + x
                else:
                    bgc.paste(imskl, (xpos - x,ypos))
            else:
                strskl = skilltext[count].split(' ')
                j = 0
                while j < len(strskl):
                    xpos = xpos + int(font.getsize(strskl[j])[0])
                    if xpos > loc['x']['supskl1']:
                        xpos = loc['x']['suplogo1'] + 120
                        ypos = ypos + rowheight
                        print(ypos)
                        draw = ImageDraw.Draw(bgc)
                        draw.text((xpos, ypos), strskl[j], font=font, fill=(255,255,255))
                        xpos = xpos + int(font.getsize(strskl[j])[0])
                    else:
                        xpos = xpos - int(font.getsize(strskl[j])[0])
                        draw = ImageDraw.Draw(bgc)
                        # layer 1
                        draw.text((xpos, ypos), strskl[j], font=font, fill=(255,255,255))
                        xpos = xpos + int(font.getsize(strskl[j])[0])
                    xpos = xpos + charwid
                    j = j + 1
        count = count + 1

bgc.save("output/Duessel1.png", quality = 95)