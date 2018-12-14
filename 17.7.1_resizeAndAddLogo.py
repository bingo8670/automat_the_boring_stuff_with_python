#! python3
# put watermark into many .jpg or .png
import os

# to make a watermark pic without background color
from PIL import Image
f = Image.open('catlogo.png')
w,h = f.size
for x in range(w):
    for y in range(h):
        if f.getpixel((x,y)) == (255,255,255,255):
            f.putpixel((x,y),(0,0,0,0))
f.save('catlogo.png')

# in a 300x300 square, and adds catlogo.png to the lower-right corner.
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# TODO: Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.lower().endswith('.jpg')
            or filename.lower().endswith('.png')
            or filename.lower().endswith('.gif')
            or filename.lower().endswith('.bmp')) or (filename == LOGO_FILENAME):
        continue
    print(filename)
    im = Image.open(filename)
    width, height = im.size

# TODO: Check if image needs to be resized.
    if width < 2 * logoWidth or height < 2 * logoHeight:
        continue
    elif width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
# TODO: Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

# TODO: Resize the image.
        print('resizing the pic')
        im = im.resize((width, height))
        print(width, height)

# TODO: Add the logo.
    print('adding watermark into %s...' % filename)
    im.paste(logoIm,(width - logoWidth, height - logoHeight),logoIm)
    print(width - logoWidth, height - logoHeight)

# TODO: Save changes.
    im.save(os.path.join('withLogo', filename))
