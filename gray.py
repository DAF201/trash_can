from PIL import Image, ImageEnhance, ImageDraw


def factor(scale):
    root = int(scale**(1/2))+1
    fin = None
    top = [x for x in range(root, scale)]
    bottom = [x for x in range(1, root)]
    bottom.reverse()
    if len(top) <= len(bottom):
        for x in top:
            if x != 0:
                if (scale % x) == 0:
                    fin = x
                    return (fin, int(scale/fin))
    else:
        for x in bottom:
            if x != 0:
                if (scale % x) == 0:
                    fin = x
                    return (fin, int(scale/fin))
    return fin


def create_img(file):
    with open(file, 'rb')as file:
        data = file.read()
    img = Image.new('L', factor(len(data)), (255))
    img.save('test.jpg')


with open(r'C:\Users\work_space\source\アイがあるようでないようである _ ナナヲアカリ.mp4', 'rb')as file:
    data = list(file.read())
image = Image.new('L', factor(len(data)))
pixels = image.load()
counter = 0
for i in range(image.size[0]):
    for j in range(image.size[1]):
        pixels[i, j] = data[counter]
        counter += 1
Image1 = Image.open('fzzl.png').convert('L').resize(image.size)
pixels1 = Image1.load()
for x in range(Image1.size[0]):
    for y in range(Image1.size[1]):
        pixels[x, y] += pixels1[x, y]
image.save('test.jpg')


image = Image.open('test.jpg')
image1 = Image.open('fzzl.png').convert('L').resize(image.size)
pixels = image.load()
pixels1 = image1.load()
for x in range(image.size[0]):
    for y in range(image.size[1]):
        pixels[x, y] -= pixels1[x, y]
image.show()
