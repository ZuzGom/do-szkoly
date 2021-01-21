from PIL import Image
import glob
import os

size = 128, 128

cord = []
move = []
c = -1  # counter
w = 1920
h = 1080
names = []
for infile in glob.glob("*.jpg"):

    file, ext = os.path.splitext(infile)
    names.append(file)
    img = Image.open(infile)
    im = img.copy()

    im = im.convert('RGBA')
    px = im.load()

    for X in range(0, w):  # width
        for Y in range(0, h):  # height
            pixel_rgb = im.getpixel((X, Y))  # Get pixel's RGB values
            r, g, b, a = pixel_rgb
            brightness = (r + g + b)/3
            if brightness < 50:
                px[X, Y] = (200, 200, 200, 0)
    cord.append(file.split('_'))
    im.save("new_"+file + ".png")
    print(im)
    c += 1

print(cord)
for i in range(1, len(cord)):
    move.append([float(cord[-i][0])-float(cord[-i-1][0]),
                 float(cord[-i][1])-float(cord[-i-1][1])])
print(move)
print(c)
size = (1920 + c*350, 1080+c*45)
print(size)


wynik = Image.new('RGBA', size)
wpx = wynik.load()


new = Image.open("new_"+names[1]+".png")
new2 = Image.open("new_"+names[2]+".png")
px1 = new.load()
px2 = new2.load()
new = new.convert('RGBA')
new2 = new2.convert('RGBA')
for X in range(0, w):  # width
    for Y in range(0, h):  # height
        wpx[X, Y] = new.getpixel((X, Y))

for X in range(0, w):  # width
    for Y in range(0, h):  # height
        try:
            p = new.getpixel((X + 350, Y + 45))
            p2 = new2.getpixel((X, Y))
            r1, g1, b1, a1 = p
            r2, g2, b2, a2 = p2
            if a2 > 0:
                if p == p2:
                    wpx[X + 350, Y + 45] = p
                else:
                    wpx[X + 350, Y + 45] = (int((r1 + r2) / 2),
                                            int((g1 + g2) / 2),
                                            int((b1 + b2) / 2), 255)



        except IndexError:
            break

print(new)
wynik.save("wynik_new.png")
