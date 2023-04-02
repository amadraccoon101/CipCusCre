from PIL import Image, ImageFont, ImageDraw, ImageFilter
from base_editor_helper import color_info, skillname_text_creator, get_rows, drawChar

def card_creator(inp):
    ###############################################################################################################
    ###############################################################################################################
    #Parse Input
    ###############################################################################################################
    f = open(inp, "r", encoding="utf-8")

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
        print(cc)
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



    ###############################################################################################################
    ###############################################################################################################
    #Constants
    ###############################################################################################################
    skillatr = ['lis','bs','hs','cp','db','dv','ts','fs','ccs','cf','us','is','as','lvs2','lvs3','lvs4','lvs5','lvs7']
    skilltypes = ['act','auto','cont','bond','spec','supp','hand']

    attributes = ['armor','axe','beast','black','blue','bow','brawl','brown','dragon','dragonstone','knife',
                'fang','female','flier','green','lance','male','mirage','monster','purple','red',
                'staff','sword','tome','white','yellow',
                'act','auto','cont','bond','spec','supp','hand','opt',
                #'lis','bs','hs','cp','db','dv','ts','fs','ccs','cf','us','is','as','lvs2','lvs3','lvs4','lvs5','lvs7',
                'flip1','flip2','flip3','flip4','flip5','tap']

    actions = ['flip1','flip2','flip3','flip4','flip5','tap']



    ###############################################################################################################
    ###############################################################################################################
    #Choose Bases
    ###############################################################################################################
    base = None
    costbase = None
    cardType = ''
    rangePic = rangePic = Image.open(color + '/range/' + rang + '.png')
    fontColor = (255,255,255)
    ccFontColor = None
    loc = {'x':{'atk':0,'sup':0,'range':0,'deployCost':0,'classChange':0,'title':0,'class':0,'suplogo1':0,'suplogo1end':0,'supskl1':0,'suplogo2':0,'suplogo2end':0,'supskl2':0,'name':0,'title':0,'class':0},
        'y':{'atk':0,'sup':0,'range':0,'deployCost':0,'classChange':0,'title':0,'class':0,'suplogo1':0,'suplogo1end':0,'supskl1':0,'suplogo2':0,'suplogo2end':0,'supskl2':0,'name':0,'title':0,'class':0}}

    if color == "green":
        cardType = 'Green '
        ccFontColor = (0,128,0)
        print('got here green')
        if promo:
            print('got here')
            if int(cost) - 1 == int(cc):
                base = Image.open(color + '/promobase.png')
                costbase = Image.open(color + '/promocostbase.png')
                cardType = cardType + 'Promo '
            else:
                base = Image.open(color + '/mcbase.png')
                costbase = Image.open(color + '/mastercostbase.png')
                rangePic = Image.open(color + '/range/' + rang + 'mc.png')
                fontColor = (0,0,0)
                cardType = cardType + 'Master '
                loc = {'x':{'atk':92,'sup':1200,'range':420,'deployCost':115,'classChange':125,'title':0,'class':0,'suplogo1':0,'suplogo1end':0,'supskl1':0,'suplogo2':0,'suplogo2end':0,'supskl2':0,'name':1180,'title':280,'class':800},
                    'y':{'atk':145,'sup':170,'range':245,'deployCost':80,'classChange':252,'title':0,'class':0,'suplogo1':0,'suplogo1end':0,'supskl1':0,'suplogo2':0,'suplogo2end':0,'supskl2':0,'name':345,'title':360,'class':248}}
        else:
            if supskl > 0:
                if 'monster' in attr or 'fang' in attr or 'Incarnate' in classtxt:
                    base = Image.open(color + '/supbaseFixed.png')
                else:
                    base = Image.open(color + '/supbase.png')
                costbase = Image.open(color + '/basecostbase.png')
                cardType = cardType + 'Base '
            elif 'monster' in attr or 'fang' in attr or 'Incarnate' in classtxt:
                if 'monster' in attr or 'fang' in attr or 'Incarnate' in classtxt:
                    base = Image.open(color + '/supbaseFixed.png')
                costbase = Image.open(color + '/basecostbase.png')
                cardType = cardType + 'Base '
            else:
                base = Image.open(color + '/base.png')
                costbase = Image.open(color + '/basecostbase.png')
                cardType = cardType + 'Fixed '
    print(cardType)



    ###############################################################################################################
    ###############################################################################################################
    #Create Cost Base
    ###############################################################################################################
    #attack
    # title_font = ImageFont.truetype('cambriaz.ttf', 155)
    bot = base.copy()
    # image_editable = ImageDraw.Draw(bot)
    # if len(atk) < 2:
    #     image_editable.text((loc['x']['atk']+33,loc['y']['atk']), atk, (255, 255, 255), font=title_font)
    # elif len(atk) > 2:
    #     title_font = ImageFont.truetype('cambriaz.ttf', 145)
    #     image_editable.text((loc['x']['atk']-40,loc['y']['atk']), atk, (255, 255, 255), font=title_font)
    # else:
    #     image_editable.text((loc['x']['atk'],loc['y']['atk']), atk, (255, 255, 255), font=title_font)
    # #support
    # title_font = ImageFont.truetype('cambriaz.ttf', 135)
    # if len(sup) < 2:
    #     image_editable.text((loc['x']['sup']+30,loc['y']['sup']), sup, (255, 255, 255), font=title_font)
    # else:
    #     image_editable.text((loc['x']['sup'],loc['y']['sup']), sup, (255, 255, 255), font=title_font)
    # #range
    # bot.paste(rangePic, (loc['x']['range'], loc['y']['range']))
    # #title
    # title_font = ImageFont.truetype('georgiab.ttf', 45)
    # image_editable.text((loc['x']['title'],loc['y']['title']), title, fontColor, font=title_font)
    # #name
    # title_font = ImageFont.truetype('georgiab.ttf', 70)
    # image_editable.text((loc['x']['name']-(len(name)*45),loc['y']['name']), name, fontColor, font=title_font)
    # #class
    # title_font = ImageFont.truetype('timesbi.ttf', 48)
    # image_editable.text((loc['x']['class'],loc['y']['class']), classtxt, (0, 0, 0), font=title_font)
    # ### ^^^ POTENTIALLY DO THIS MANUALLY ^^^ ###

    # bot.save("output/test.png", quality=95)

    ###############################################################################################################
    ###############################################################################################################
    #Create Cost Base
    ###############################################################################################################
    # top = costbase.copy()
    # image_editable = ImageDraw.Draw(top)
    # #deployment cost
    # title_font = ImageFont.truetype('cambriaz.ttf', 155)
    # image_editable.text((loc['x']['deployCost'],loc['y']['deployCost']), cost, (255, 255, 255), font=title_font)
    # #cc cost
    # title_font = ImageFont.truetype('cambriaz.ttf', 130)
    # image_editable.text((loc['x']['classChange'],loc['y']['classChange']), cc, ccFontColor, font=title_font)
    # top.save("output/test2.png", quality=95)

    ###############################################################################################################
    ###############################################################################################################
    #Create Full Output
    ###############################################################################################################
    full = Image.open('attributes/full.png')

    w, h = full.size
    w2, h2 = bot.size

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
    fontsize = 30
    font = ImageFont.truetype('georgiab.ttf', fontsize)
    charwid = 24
    rowheight = 40
    rowextra = 4
    rows = get_rows(skills, charwid, rowheight, rowextra, fontsize, attributes, font)

    # set up space on the card for effects
    botx, boty = bot.size
    bgcx, bgcy = output.size
    skillx = loc['x']['atk']
    skilly = bgcy - boty - (rows * rowheight) - (len(skills) * rowextra) + 50
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
                        output.paste(imskl, (xpos+10,ypos))
                        output.paste(imsklend, (xpos+x+10,ypos), imsklend)
                        xpos = xpos + x + 20
                    else:
                        output.paste(imskl, (xpos,ypos))
                        output.paste(imsklend, (xpos+x,ypos), imsklend)
                        xpos = xpos + x + 10
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
                    if xpos > 1350:
                        xpos = skillx
                        ypos = ypos + rowheight
                        #print(ypos)
                        if y == 30:     # for smaller images
                            output.paste(imskl, (xpos,ypos + 10), imskl)
                        else:
                            output.paste(imskl, (xpos,ypos), imskl)
                        xpos = xpos + x
                    else:
                        if y == 30:     # for smaller images
                            output.paste(imskl, (xpos - x,ypos + 10), imskl)
                        else:
                            output.paste(imskl, (xpos - x,ypos), imskl)
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
                    if xpos > 1350:
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
                        xpos = xpos + int(font.getsize(strskl[j])[0])
                        if xpos > 1350:
                            xpos = skillx
                            ypos = ypos + rowheight

                            draw = ImageDraw.Draw(output)
                            drawChar(draw, xpos, ypos, strskl[j], font)
                            xpos = xpos + int(font.getsize(strskl[j])[0])
                            #print(ypos)
                        else:
                            xpos = xpos - int(font.getsize(strskl[j])[0])

                            draw = ImageDraw.Draw(output)
                            drawChar(draw, xpos, ypos, strskl[j], font)
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

    output.save("output/fulloutput.png", quality=95)

    ###############################################################################################################
    ###############################################################################################################
    #Add Card Image
    ###############################################################################################################
    bgc = Image.open("InputImages/Ike6_4.png")

    bgc.paste(output, (0,0), output)

    bgc.save("output/Ike6_4.png", quality=95)



card_creator("input.txt")