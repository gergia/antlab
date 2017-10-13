from __future__ import print_function
from PIL import Image, ImageFilter
import argparse
import os

def generateMap(scale=8, imageFile="twoRoomsCropped.pgm", obstacleFile="obstacle.txt"):
    #Read image
    im = Image.open(imageFile )
    current_dir = os.path.dirname(os.path.realpath(__file__))
    pix = im.load()
    (x1, y1, x2, y2) = im.getbbox() 
    print("x1 = %d  y1 = %d    x2 = %d  y2 = %d" % (x1, y1, x2, y2))
    length = int(x2 / scale) - 1
    width = int(y2 / scale) - 1 
    
    print("length = %d  width = %d" % (length, width))
    
    fo = open(current_dir+"/dimension.txt", "w")
    fo.write("%d\n" % length)
    fo.write("%d" % width)
    fo.close()
    
    img = Image.new( 'RGB', (x2,y2), "white") # create a new black image
    pixels = img.load() # create the pixel map
    
    fo = open(current_dir+"/obstacle.txt", "w")
    for count1 in range(0, length + 1):
       for count2 in range(0, width + 1):
           pixels[count1*scale + scale,count2 *scale + scale] = 100
           obstacle_flag = 0;
           for x in range (count1*scale, count1*scale + scale):
               for y in range (count2*scale, count2*scale + scale):
                   occ = (255 - pix[x,y]) / 255.0
                   #fo.write("%f\n" % occ) 
                   if occ > 0.197:
                   #if occ > 0.75:
                       obstacle_flag = 1
           if obstacle_flag == 1:
               fo.write("%d %d\n" % (count1, count2))
               for x in range (count1*scale, count1*scale + scale):
                   for y in range (count2*scale, count2*scale + scale):
                       pixels[x, y] = 255
    fo.close()
    
    count1 = 9
    count2 = 8
    for x in range (count1*scale, count1*scale + scale):
        for y in range (count2*scale, count2*scale + scale):
            pixels[x, y] = 100

    img.show()
            

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scale", default=8)
    parser.add_argument("--image", default="twoRoomsCropped.pgm")
    parser.add_argument("--obstacleFile", default="obstacle.txt")
    parser.add_argument("--dimensionFile", default="dimension.txt")
    args, unknown = parser.parse_known_args()
    scale = int(args.scale)
    imageFile = args.image
    
    generateMap(scale=scale, imageFile=imageFile)
    
    
if __name__ == '__main__':
    main()
