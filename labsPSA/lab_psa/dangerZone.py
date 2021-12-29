from PIL import Image
from random import randint
def main():
    image = Image.open('danger_zone.png')
    red = 0
    blue = 0
    redArea = 0
    imrgb = image.convert("RGB")
    #for px in imrgb.getdata():
    #    if px == (255,0,0):
    #        red+=1
    #     else:
    #        blue+=1
    #    redArea = red/(red+blue)*42
    n = 100000
    for _ in range(n):
        x = randint(0,image.width-1)
        y = randint(0,image.height-1)
        coor = x,y
        if (imrgb.getpixel( coor ) == (255,0,0)):
            red+=1
        else:
            blue+=1
    redArea = (red/(red+blue)*42)
    print(redArea)
if __name__ == '__main__':
    main()