from PIL import Image, ImageFont, ImageDraw, ImageFilter

def color_info(color, promo, cost, cc, supskl):
    loc = {'x':{'atk':0,'sup':0,'range':0,'deployCost':0,'classChange':0,'title':0,'class':0,'suplogo1':0,'suplogo1end':0,'supskl1':0,'suplogo2':0,'suplogo2end':0,'supskl2':0},
           'y':{'atk':0,'sup':0,'range':0,'deployCost':0,'classChange':0,'title':0,'class':0,'suplogo1':0,'suplogo1end':0,'supskl1':0,'suplogo2':0,'suplogo2end':0,'supskl2':0}}
    if color is 'red':
        if supskl < 1:
            # no supp skill atk 67, 143
            loc['x']['atk'] = 72
            loc['y']['atk'] = 135
            # no supp skill sup 1188, 171
            loc['x']['sup'] = 1190
            loc['y']['sup'] = 163
            # no supp skill range 397, 200
            loc['x']['range'] = 397
            loc['y']['range'] = 200
            # no supp skill title 280, 305
            loc['x']['title'] = 280
            loc['y']['title'] = 305
            # no supp skill class 280, 305
            loc['x']['class'] = 605
            loc['y']['class'] = 200
        else:
            # supp skill atk 67, 143
            loc['x']['atk'] = 86
            loc['y']['atk'] = 219
            # supp skill sup 1198, 239
            loc['x']['sup'] = 1198
            loc['y']['sup'] = 239
            # supp skill range 406, 285
            loc['x']['range'] = 406
            loc['y']['range'] = 285
            # supp skill title 292, 388
            loc['x']['title'] = 292
            loc['y']['title'] = 388
            # supp skill class 280, 305
            loc['x']['class'] = 609
            loc['y']['class'] = 289
            # supp skill logo 328, 14
            loc['x']['suplogo1'] = 328
            loc['y']['suplogo1'] = 14 
            # supp skill effect 1330, 134
            loc['x']['supskl1'] = 1337
            loc['y']['supskl1'] = 197
        if promo:
            if cost - cc == 1:
                # no mc dc 117, 115 cc 126, 283
                loc['x']['deployCost'] = 117
                loc['y']['deployCost'] = 115
                loc['x']['classChange'] = 126
                loc['y']['classChange'] = 283
            else:
                # mc dc 124, 112 cc 133, 283 
                loc['x']['deployCost'] = 124
                loc['y']['deployCost'] = 112
                loc['x']['classChange'] = 133
                loc['y']['classChange'] = 283
        else:
            # no promo dc 119, 112
            loc['x']['deployCost'] = 119
            loc['y']['deployCost'] = 112
    elif color is 'purple':
        if supskl < 1:
            # no supp skill atk 67, 143
            loc['x']['atk'] = 90
            loc['y']['atk'] = 122
            # no supp skill sup 1188, 171
            loc['x']['sup'] = 1204
            loc['y']['sup'] = 147
            # no supp skill range 397, 200
            loc['x']['range'] = 405
            loc['y']['range'] = 195
            # no supp skill title 280, 305
            loc['x']['title'] = 295
            loc['y']['title'] = 300
            # no supp skill class 280, 305
            loc['x']['class'] = 610
            loc['y']['class'] = 195
        else:
            if supskl > 1:  # dual support done
                # supp skill atk 67, 143
                loc['x']['atk'] = 89
                loc['y']['atk'] = 415
                # supp skill sup 1198, 239
                loc['x']['sup'] = 1200
                loc['y']['sup'] = 428
                # supp skill range 406, 285
                loc['x']['range'] = 410
                loc['y']['range'] = 376
                # supp skill title 292, 388
                loc['x']['title'] = 295
                loc['y']['title'] = 583
                # supp skill class 280, 305
                loc['x']['class'] = 610
                loc['y']['class'] = 480
                # supp skill logo 328, 14
                loc['x']['suplogo1'] = 333
                loc['y']['suplogo1'] = 14
                # supp skill logo 328, 14
                loc['x']['suplogo2'] = 333
                loc['y']['suplogo2'] = 180
                # supp skill effect 1330, 134
                loc['x']['supskl1'] = 1337
                loc['y']['supskl1'] = 170
                # supp skill effect 1330, 134
                loc['x']['supskl1'] = 1337
                loc['y']['supskl1'] = 318
            elif promo:  # promo support done
                # supp skill atk 67, 143
                loc['x']['atk'] = 89
                loc['y']['atk'] = 287
                # supp skill sup 1198, 239
                loc['x']['sup'] = 1203
                loc['y']['sup'] = 296
                # supp skill range 406, 285
                loc['x']['range'] = 417
                loc['y']['range'] = 342
                # supp skill title 292, 388
                loc['x']['title'] = 303
                loc['y']['title'] = 439
                # supp skill class 280, 305
                loc['x']['class'] = 615
                loc['y']['class'] = 344
                # supp skill logo 328, 14
                loc['x']['suplogo1'] = 335
                loc['y']['suplogo1'] = 14
                # supp skill effect 1330, 134
                loc['x']['supskl1'] = 1344
                loc['y']['supskl1'] = 183
            else:  # base support done
                # supp skill atk 67, 143
                loc['x']['atk'] = 94
                loc['y']['atk'] = 288
                # supp skill sup 1198, 239
                loc['x']['sup'] = 1199
                loc['y']['sup'] = 303
                # supp skill range 406, 285
                loc['x']['range'] = 408
                loc['y']['range'] = 357
                # supp skill title 292, 388
                loc['x']['title'] = 300
                loc['y']['title'] = 458
                # supp skill class 280, 305
                loc['x']['class'] = 611
                loc['y']['class'] = 359
                # supp skill logo 328, 14
                loc['x']['suplogo1'] = 333
                loc['y']['suplogo1'] = 14
                # supp skill effect 1330, 134
                loc['x']['supskl1'] = 1337
                loc['y']['supskl1'] = 194
        if promo:
            # no mc dc 117, 115 cc 126, 283
            loc['x']['deployCost'] = 119
            loc['y']['deployCost'] = 122
            loc['x']['classChange'] = 129
            loc['y']['classChange'] = 294
        else:
            # no promo dc 119, 112
            loc['x']['deployCost'] = 128
            loc['y']['deployCost'] = 126
    return loc

def skillname_text_creator(skillname, charwid, rowheight, rowextra, fontsize, color):
    # line character limit 60, pixel length is 1150
    bgcol = (25,13,100)
    if color is 'default':
        bgcol = (25,13,100)
    font = ImageFont.truetype('georgiab.ttf', fontsize)
    if '*' in skillname:
        namesplit = skillname.split('*')
        skillicon = Image.open('skillheaders/'+namesplit[0]+'.png')
        x,y = skillicon.size
        # if y < (rowheight + rowextra):
        #     ratio = (rowheight + rowextra)/y
        #     skillicon = skillicon.resize((int(ratio * x),rowheight + rowextra))
        #     x,y = skillicon.size
        #print("GS ICON SIZE")
        #print(x)
        im0 = Image.new(mode = "RGBA", size = (x + font.getsize(namesplit[1])[0]+5, rowheight-2), color=bgcol)
        im = Image.new(mode = "RGBA", size = (x + font.getsize(namesplit[1])[0]+5, rowheight), color=(255,255,255))
        im.paste(im0, (0,1), im0)
        draw = ImageDraw.Draw(im)
        im.paste(skillicon, (0,0), skillicon)
        draw.text((x + 5,1), namesplit[1], (255, 255, 255), font=font)
        if (x + int(charwid*len(namesplit[1])) + 10) > 1150:
            im = im.resize((1150,rowheight+rowextra)) 
        im.save("skillname.png", quality=95)
    else:
        #im = Image.new(mode = "RGB", size = (int(charwid*len(skillname)) + 10, rowheight + rowextra), color=bgcol)
        #print('rowheight')
        #print(rowheight)
        im = Image.new(mode = "RGBA", size = (font.getsize(skillname)[0],rowheight), color=(255,255,255))
        im0 = Image.new(mode = "RGBA", size = (font.getsize(skillname)[0],rowheight-2), color=bgcol)
        im.paste(im0, (0,1), im0)
        draw = ImageDraw.Draw(im)
        #draw.text((5,2), skillname, (255, 255, 255), font=font)
        draw.text((0,1), skillname, (255, 255, 255), font=font)
        #print(int(font.getsize(skillname)[0]) + 20)
        if (int(font.getsize(skillname)[0]) + 6) > 280:
            #print('enter')
            im = im.resize((280,rowheight+rowextra))
        im.save("skillname.png", quality=95)

def get_rows(skills, charwid, rowheight, rowextra, fontsize, attributes, font, rowlen):
    rows = 0
    for i in skills:
        if i is not '':
            skilltext = i.split('|')
            idx = 0
            while idx < len(skilltext):
                if idx is 0:
                    skillname_text_creator(skilltext[0], charwid, rowheight, rowextra, fontsize, 'default')
                    imskl = Image.open('skillname.png')
                    x,y = imskl.size
                    x = x + 20
                    rowlen = rowlen - x
                #elif skilltext[idx] in attributes:
                #    rowlen = rowlen - 30
                #    if rowlen < 0:
                #        rowlen = 1150
                #        rows = rows + 1
                #        rowlen = rowlen - 30
                elif  skilltext[idx].lower() in attributes:
                    skltxt = skilltext[idx].lower()
                    imskl = Image.open('icons/'+ skltxt +'.png')
                    x,y = imskl.size
                    if y > 40:
                        #print(y)
                        imskl = imskl.resize((rowheight,rowheight))
                        x,y = imskl.size
                    rowlen = rowlen - x
                    if rowlen < 0:
                        rowlen = 1150
                        rows = rows + 1
                        rowlen = rowlen - x
                else:
                    strskl = skilltext[idx].split(' ')
                    j = 0
                    while j < len(strskl):
                        # decreasing row length per character
                        rowlen = rowlen - (int(font.getsize(strskl[j])[0]))
                        if rowlen < 0:
                            rowlen = 1150
                            rows = rows + 1
                            rowlen = rowlen - (int(font.getsize(strskl[j])[0]))
                        else:
                            # accounting for the space after each word
                            rowlen = rowlen - int(font.getsize(' ')[0])
                        j = j + 1
                idx = idx + 1
            rows = rows + 1
    return rows

def drawChar(draw, xpos, ypos, inpchar, font):
    # layer 1
    draw.text((xpos, ypos), inpchar, font=font, fill=(255,255,255))

    draw.text((xpos, ypos-1), inpchar, font=font, fill=(255,255,255))
    draw.text((xpos, ypos+1), inpchar, font=font, fill=(255,255,255))
    draw.text((xpos-1, ypos), inpchar, font=font, fill=(255,255,255))
    draw.text((xpos+1, ypos), inpchar, font=font, fill=(255,255,255))

    draw.text((xpos-1, ypos-1), inpchar, font=font, fill=(255,255,255))
    draw.text((xpos+1, ypos-1), inpchar, font=font, fill=(255,255,255))
    draw.text((xpos-1, ypos+1), inpchar, font=font, fill=(255,255,255))
    draw.text((xpos+1, ypos+1), inpchar, font=font, fill=(255,255,255))
    # layer 2
    # draw.text((xpos, ypos-2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos, ypos+2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos-2, ypos), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos+2, ypos), inpchar, font=font, fill=(255,255,255))

    # draw.text((xpos-2, ypos-1), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos+2, ypos-1), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos-2, ypos+1), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos+2, ypos+1), inpchar, font=font, fill=(255,255,255))

    # draw.text((xpos-1, ypos-2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos+1, ypos-2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos-1, ypos+2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos+1, ypos+2), inpchar, font=font, fill=(255,255,255))

    # draw.text((xpos-2, ypos-2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos+2, ypos-2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos-2, ypos+2), inpchar, font=font, fill=(255,255,255))
    # draw.text((xpos+2, ypos+2), inpchar, font=font, fill=(255,255,255))
    if font.getsize == 30:
        # layer 3
        draw.text((xpos-3, ypos-2), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+3, ypos-2), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos-3, ypos+2), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+3, ypos+2), inpchar, font=font, fill=(255,255,255))

        draw.text((xpos-2, ypos-3), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+2, ypos-3), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos-2, ypos+3), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+2, ypos+3), inpchar, font=font, fill=(255,255,255))

        draw.text((xpos-3, ypos-1), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+3, ypos-1), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos-3, ypos+1), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+3, ypos+1), inpchar, font=font, fill=(255,255,255))

        draw.text((xpos-1, ypos-3), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+1, ypos-3), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos-1, ypos+3), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+1, ypos+3), inpchar, font=font, fill=(255,255,255))

        draw.text((xpos-3, ypos-3), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+3, ypos-3), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos-3, ypos+3), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+3, ypos+3), inpchar, font=font, fill=(255,255,255))
        # layer 4
        draw.text((xpos-4, ypos-2), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+4, ypos-2), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos-4, ypos+2), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+4, ypos+2), inpchar, font=font, fill=(255,255,255))

        draw.text((xpos-2, ypos-4), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+2, ypos-4), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos-2, ypos+4), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+2, ypos+4), inpchar, font=font, fill=(255,255,255))

        draw.text((xpos-4, ypos-1), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+4, ypos-1), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos-4, ypos+1), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+4, ypos+1), inpchar, font=font, fill=(255,255,255))

        draw.text((xpos-1, ypos-4), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+1, ypos-4), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos-1, ypos+4), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+1, ypos+4), inpchar, font=font, fill=(255,255,255))

        draw.text((xpos-4, ypos-3), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+4, ypos-3), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos-4, ypos+3), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+4, ypos+3), inpchar, font=font, fill=(255,255,255))

        draw.text((xpos-3, ypos-4), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+3, ypos-4), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos-3, ypos+4), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+3, ypos+4), inpchar, font=font, fill=(255,255,255))

        draw.text((xpos-4, ypos-4), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+4, ypos-4), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos-4, ypos+4), inpchar, font=font, fill=(255,255,255))
        draw.text((xpos+4, ypos+4), inpchar, font=font, fill=(255,255,255))
    # writing
    draw.text((xpos, ypos), inpchar, font=font, fill=(0,0,0))
    #draw.text((xpos-1, ypos-1), inpchar, font=font, fill=(0,0,0))
    #draw.text((xpos+1, ypos-1), inpchar, font=font, fill=(0,0,0))
    #draw.text((xpos-1, ypos+1), inpchar, font=font, fill=(0,0,0))
    #draw.text((xpos+1, ypos+1), inpchar, font=font, fill=(0,0,0))
