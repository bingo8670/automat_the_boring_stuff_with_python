#! python3
# make card for different guests

import os
from PIL import Image, ImageDraw

os.makedirs('card_dir', exist_ok=True)
os.chdir('card_dir')
with open('guests.txt') as f:
    for guest in f.readlines():
        im = Image.open('card_mo.png')
        draw = ImageDraw.Draw(im)
        draw.text((50,50),guest.strip().title(),fill='blue')
        card_name = 'card_to_%s.png' % guest.strip()
        im.save(card_name)

        print('card-making work is done!')
