from PIL import Image
import sys

# multi_im = ["sikuliximage-1506129382287.png","sikuliximage-1506129382603.png","sikuliximage-1506129382921.png","sikuliximage-1506129383237.png"]

im1 = Image.open(sys.argv[1])
#im1 = Image.open("sikuliximage-1506185019606.png")
pixelMap = im1.load()

im2 = Image.open(sys.argv[2])
#im2 = Image.open("sikuliximage-1506185019938.png")
pixelMap2 = im2.load()

img = Image.new( im1.mode, im1.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixelMap[i,j] == pixelMap2[i,j]:
            pixelsNew[i,j] = (0,0,0)
        else:
            pixelsNew[i,j] = (255,255,255)

response = ""

#img.show()


img_a = Image.open("0.png")
pxl_a = img_a.load()

img_s = Image.open("1.png")
pxl_s = img_s.load()

img_w = Image.open("2.png")
pxl_w = img_w.load()

img_d = Image.open("6.png")
pxl_d = img_d.load()

pxl_list = [pxl_a, pxl_s, pxl_w, pxl_d]
arrow_list = ['a','s','w','d']

for n in range(10):
    w = img.size[0]
    h = img.size[1]
    w2 = int(img.size[0]/10)
    w3 = w2 * 1
    region = (w3*n+int(w2*0.4), 0, w3*n+int(w2*0.8), h)
    cropImg = img.crop(region)
    pixel_crop = cropImg.load()
    #cropImg.show()
    #cropImg.save("%d.png"%(n),"PNG")

    line_count = 0
    for i in range(cropImg.size[0]):
        for j in range(cropImg.size[1]):
            if pixel_crop[i,j][0] == 0:
                line_count = line_count + 1
    if line_count < 15:
        break

    score = 10000
    ans = ''

    for k in range(4):
        pixel_diff = 0
        for i in range(cropImg.size[0]):
            for j in range(cropImg.size[1]):
                if pixel_crop[i,j][0] != pxl_list[k][i,j][0]:
                    pixel_diff = pixel_diff + 1
        if pixel_diff < score:
            score = pixel_diff
            ans = arrow_list[k]

    response += ans

print response
