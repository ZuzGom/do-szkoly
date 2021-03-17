from PIL import ImageDraw, ImageFont, Image

imag = Image.open('sq.jpg')
w, h = imag.size
imag = imag.convert('RGB')
out = open('sq.txt','w')
pixel = imag.load()
asci =['@','#','S','%','*','+',';',':',',','.']


a = int(w/600)
b = int(h/200)
lines = [[] for col in range(h)]
if a == 0:
    a = 1

if b == 0:
    b = 1
for X in range(0, w):  # width
    Y = 0
    if X%a==0:
        while Y < h :  # height
            rgb = imag.getpixel((X,Y))
        
            rgb = sum(rgb)
            i = int(rgb/76.5) - 1
            if i < 0:
                i = 0
            lines[Y].append(asci[i])
            Y += b
    #out.write(line+'\n')


for x in lines:
    for y in x:
        out.write(y)
        #out.write(y)
    if len(x)>1:
        out.write('\n')
out.close()



