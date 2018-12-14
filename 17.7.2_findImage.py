#! python3
# check pic dir

import os
from PIL import Image

for root, folders, files in os.walk('.'):
    numPhoteFiles = 0
    numNonPhotoFiles = 0
    for file in files:
        if not(file.lower().endswith('.jpg') or file.lower().endswith('.png')):
            numNonPhotoFiles += 1
            continue

        im = Image.open(os.path.join(root,file))
        width, height = im.size
        if width < 500 and height < 500:
            numNonPhotoFiles += 1
        else:
            numPhoteFiles += 1

        if numPhoteFiles >= numNonPhotoFiles:
            print(root)
