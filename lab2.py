from PIL import Image, ImageDraw
import re

canvas = Image.new('RGBA', (540, 960), "pink")
imaged = ImageDraw.Draw(canvas)

file = open('DS2.txt')
strfile = file.readlines()
strfilesplit = []

for i in range(len(strfile)):
    strfilesplit.append(re.findall(r'\d+', strfile[i]))

for a in range(len(strfilesplit)):
    imaged.point((int(strfilesplit[a][0]), int(strfilesplit[a][1])), fill="black")

canvas.save("picture.png", "PNG")
canvas.show()



