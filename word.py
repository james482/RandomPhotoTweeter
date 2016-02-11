from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import sys
import tweet
import random
import logging


def post(conf, dir):
    width, height = 1024, 512
    update = random.choice(conf.get_word())
    word = update[0]
    status = update[1]
    fontSize = 10

    ttf = random.choice(conf.get_font())
    colour = random.choice(conf.get_word_colour())
    wordColour = colour[0]
    bgColour = colour[1]

    # create the image
    try:
        pic = Image.new("RGB", (width, height), bgColour)
    except ValueError:
        logging.error('Invalid background colour.')
        os.system("Pause")
        sys.exit(1)

    draw = ImageDraw.Draw(pic)

    try:
        font = ImageFont.truetype(ttf, fontSize)
    except OSError:
        logging.error('Invalid font file.')
        os.system("Pause")
        sys.exit(1)
    w, h = font.getsize(word)

    # scale the word
    while w < width-(width*0.2) and h < height-(height*0.15):
        font = ImageFont.truetype(ttf, fontSize)
        w, h = font.getsize(word)
        fontSize += 1
    fontSize -= 1

    # create the image
    try:
        draw.text(((width-w)/2, (height-h)/2), word, font=font, fill=wordColour)
    except ValueError:
        logging.error('Invalid text colour.')
        os.system("Pause")
        sys.exit(1)

    logging.debug('Created the picture at: ' + os.path.join(dir, 'pic.png'))
    logging.debug('Make a copy now if you wish to keep it.')
    pic.save(os.path.join(dir, 'pic.png'))
    p = [os.path.join(dir, 'pic.png'), status]
    tweet.tweet_with_pic(conf, p)

    return
