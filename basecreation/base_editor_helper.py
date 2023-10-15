from PIL import Image, ImageFont, ImageDraw, ImageFilter

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
