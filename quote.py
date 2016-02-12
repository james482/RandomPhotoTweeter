from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFilter
import os
import tweet
import random
import textwrap
import math
import logging


def post(conf, dir):
    width, height = 768, 768
    update = random.choice(conf.get_quote())
    name = "- " + update[0]
    status = update[1]
    textColor = update[2]
    quote = update[4]

    ttf = random.choice(conf.get_font())

    fontSize = 6
    nameSize = 36

    # try opening the image, resizing it and cropping to fit the image
    try:
        pic = Image.open(update[3])
        shortSide = min(pic.size[0], pic.size[1])

        pic = pic.crop((int(pic.size[0]/2-shortSide/2),
                            int(pic.size[1]/2-shortSide/2),
                            int(pic.size[0]/2+shortSide/2),
                            int(pic.size[1]/2+shortSide/2)))

        pic = pic.resize((width, height), Image.ANTIALIAS)

        pic = pic.filter(ImageFilter.GaussianBlur(radius=2))
    # otherwise create a black image
    except IOError:
        pic = Image.new("RGB", (width, height), "black")

    # create the canvas
    draw = ImageDraw.Draw(pic)
    # set the font
    try:
        font = ImageFont.truetype(ttf, fontSize)
    except OSError:
        conf.error('Invalid font file.')
    font = ImageFont.truetype(ttf, fontSize)

    # wrap the quote based on its size
    wrap = textwrap.wrap(quote, width=int((math.sqrt(font.getsize(quote)[0])*2)))
    m = 0
    # find the longest line
    for line in wrap:
        if font.getsize(line)[0] > m:
            m = font.getsize(line)[0]
            test = line
    # size the text based on longest line
    w = font.getsize(test)[0]
    while w < width-(width*0.15):
        font = ImageFont.truetype(ttf, fontSize)
        w, h = font.getsize(test)
        fontSize += 1
    fontSize -= 1

    wrapH = ((height-h)/2)-((font.getsize(wrap[1])[1])*(len(wrap)/2))
    # draw text including 8 way shadow
    for line in wrap:
        wrapW = (width-draw.textsize(line, font=font)[0])/2
        draw.text((wrapW-2, wrapH), line, font=font, fill='black')
        draw.text((wrapW+2, wrapH), line, font=font, fill='black')
        draw.text((wrapW, wrapH-2), line, font=font, fill='black')
        draw.text((wrapW, wrapH+2), line, font=font, fill='black')
        draw.text((wrapW-2, wrapH-2), line, font=font, fill='black')
        draw.text((wrapW+2, wrapH+2), line, font=font, fill='black')
        draw.text((wrapW+2, wrapH-2), line, font=font, fill='black')
        draw.text((wrapW-2, wrapH+2), line, font=font, fill='black')
        try:
            draw.text((wrapW, wrapH), line, font=font, fill=textColor)
        except ValueError:
            conf.error('Invalid text colour.')

        wrapH += font.getsize(line)[1]

    font = ImageFont.truetype(ttf, nameSize)
    wName, hName = draw.textsize(name, font=font)
    # if name too long, shorten it
    while wName > width-(width*0.1):
        font = ImageFont.truetype(ttf, nameSize)
        wName, hName = font.getsize(name)
        nameSize -= 10
    # draw the name including 8 way shadow
    draw.text(((width-wName-(width*0.1))-2, (height-h-(height*0.05))), name, font=font, fill='black')
    draw.text(((width-wName-(width*0.1))+2, (height-h-(height*0.05))), name, font=font, fill='black')
    draw.text(((width-wName-(width*0.1)), (height-h-(height*0.05))-2), name, font=font, fill='black')
    draw.text(((width-wName-(width*0.1)), (height-h-(height*0.05))+2), name, font=font, fill='black')
    draw.text(((width-wName-(width*0.1))-2, (height-h-(height*0.05))-2), name, font=font, fill='black')
    draw.text(((width-wName-(width*0.1))+2, (height-h-(height*0.05))+2), name, font=font, fill='black')
    draw.text(((width-wName-(width*0.1))+2, (height-h-(height*0.05))-2), name, font=font, fill='black')
    draw.text(((width-wName-(width*0.1))-2, (height-h-(height*0.05))+2), name, font=font, fill='black')
    try:
        draw.text((width-wName-(width*0.1), height-h-(height*0.05)), name, font=font, fill=textColor)
    except ValueError:
        conf.error('Invalid text colour.')

    logging.debug('Created the picture at: ' + os.path.join(dir, 'pic.png'))
    logging.debug('Make a copy now if you wish to keep it.')
    pic.save(os.path.join(dir, 'pic.png'))
    p = [os.path.join(dir, 'pic.png'), status]
    tweet.tweet_with_pic(conf, p)

    return
