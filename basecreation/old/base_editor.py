from PIL import Image, ImageFont, ImageDraw, ImageFilter

title = "Marth, Hero King of Archanaea"
classtxt = "Lodestar"
color = 'red'
atk = 80
sup = 30
rang = 1
promo = True
supskl = 1
cost = 5
cc = 4
attrib = 'red+male+sword'

#base dimensions = (1466, 478)
base = None
if color is 'green':
    if supskl > 0:
        base = Image.open(color + '/base2.png')
    else:
        if cost - cc == 2:
            base = Image.open(color + '/base2.png')
        else:
            base = Image.open(color + '/base.png')
else:
    base = Image.open(color + '/base.png')
bot = base.copy()
x = 0
y = 0
atkpic = Image.open(color + '/atk/' + str(atk) + '.png')
#choosing location for attack pic
if color is 'red':
    x = 77
    y = 150
    if supskl:
        x = x + 8
if color is 'green':
    x = 88
    y = 161
    if cost - cc == 2:
        y = y + 50
bot.paste(atkpic, (x, y))
bot.save("bot.png", quality = 95)
suppic= Image.open(color + '/sup/' + str(sup) + '.png')
#choosing location for support pic
if color is 'red' or 'green':
    x = 1191
    y = 171
    if color is 'green':
        if cost - cc == 2:
            y = y + 50
bot.paste(suppic, (x, y))
ranpic = Image.open(color + '/range/' + str(rang) + '.png')
if color is 'red':
    x = 415
    y = 200
if color is 'green':
    x = 425
    y = 200
    if cost - cc == 2:
        y = y + 45
bot.paste(ranpic, (x, y))

#name location = (270, 300)
image_editable = ImageDraw.Draw(bot)
title_font = ImageFont.truetype('arial.ttf', 60)
#30 character limit for title
image_editable.text((280,305), title, (237, 230, 211), font=title_font)
#Starting Coordinates: Pillow library uses a Cartesian pixel coordinate system, with (0,0) in the upper left corner.
#Text: String between single or double quotations
#Text color in RGB format
#Font style
#class location = (605, 210)
class_font = ImageFont.truetype('arial.ttf', 50)
image_editable.text((605,200), classtxt, (0, 0, 0), font=class_font)

full = Image.open(color + '/full.png')
output = full.copy()
output.paste(bot, (0, 1600), bot)

if promo:
    if cost - 1 == cc:
        costbase = Image.open(color + '/promocostbase.png')
        costpic = Image.open(color + '/cost/' + str(cost) + 'cost.png')
        costbase.paste(costpic, (121, 112))
        ccpic = Image.open(color + '/cost/' + str(cc) + 'cc.png')
        costbase.paste(ccpic, (127, 282))
        output.paste(costbase, (0, 0), costbase)
    else:
        costbase = Image.open(color + '/masterclassbase.png')
        costpic = Image.open(color + '/cost/' + str(cost) + 'cost.png')
        costbase.paste(costpic, (121, 112))
        ccpic = Image.open(color + '/cost/' + str(cc) + 'mc.png')
        costbase.paste(ccpic, (128, 283))
        output.paste(costbase, (0, 0), costbase)
else:
    costbase = Image.open(color + '/basecostbase.png')
    costpic = Image.open(color + '/cost/' + str(cost) + 'cost.png')
    costbase.paste(costpic, (121, 112))
    output.paste(costbase, (0, 0), costbase)

attr = attrib.split('+')
#print(attr)

y = 470

i = 0
for a in attr:
    if i < 6:
        atrpic = Image.open('attributes/' + a + '.png')
        output.paste(atrpic, (29, y), atrpic)
        y = y + 97
    i = i + 1

ogpic = Image.open('Marth3.jpg')
bgc = ogpic.resize((1466, 2078))

bgc.paste(output, (0,0), output)

bgc.save("output.png", quality = 95)