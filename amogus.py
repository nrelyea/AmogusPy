import cv2
import os
from PIL import Image


######     Scanning Amogi      ######


def Color(image,pixel):
    return [image[pixel[1]][pixel[0]][0], image[pixel[1]][pixel[0]][1], image[pixel[1]][pixel[0]][2]]

def NearbyPixel(originPixel, horizontal, vertical):
    return (originPixel[0]+horizontal,originPixel[1]+vertical)

def CheckAmogusLeft(image, pixel):
    if(
        Color(image,pixel) == 
        Color(image,NearbyPixel(pixel,1,0)) == 
        Color(image,NearbyPixel(pixel,2,0)) ==
        Color(image,NearbyPixel(pixel,2,1)) ==
        Color(image,NearbyPixel(pixel,3,1)) ==
        Color(image,NearbyPixel(pixel,0,2)) ==
        Color(image,NearbyPixel(pixel,1,2)) ==
        Color(image,NearbyPixel(pixel,2,2)) ==
        Color(image,NearbyPixel(pixel,3,2)) ==
        Color(image,NearbyPixel(pixel,0,3)) ==
        Color(image,NearbyPixel(pixel,1,3)) ==
        Color(image,NearbyPixel(pixel,2,3)) ==
        Color(image,NearbyPixel(pixel,0,4)) ==
        Color(image,NearbyPixel(pixel,2,4))
        and
        Color(image,NearbyPixel(pixel,0,1)) == Color(image,NearbyPixel(pixel,1,1))  # eyes same color
        and
        Color(image,pixel) != Color(image,NearbyPixel(pixel,1,1))       # eyes diff color
        and
        Color(image,pixel) != Color(image,NearbyPixel(pixel,1,4))       # between legs diff color
        and
        Color(image,pixel) != Color(image,NearbyPixel(pixel,3,0))       # behind head diff color
        and
        Color(image,pixel) != Color(image,NearbyPixel(pixel,3,3))       # behind leg diff color
        #and
        #Color(image,pixel) != Color(image,NearbyPixel(pixel,3,4))       # behind foot diff color
    ):
        return "AMOGUS"
    else:
        return "NOPE"
    
def CheckAmogusRight(image, pixel):
    if(
        Color(image,NearbyPixel(pixel,1,0)) == 
        Color(image,NearbyPixel(pixel,2,0)) == 
        Color(image,NearbyPixel(pixel,3,0)) ==
        Color(image,NearbyPixel(pixel,0,1)) ==
        Color(image,NearbyPixel(pixel,1,1)) ==
        Color(image,NearbyPixel(pixel,0,2)) ==
        Color(image,NearbyPixel(pixel,1,2)) ==
        Color(image,NearbyPixel(pixel,2,2)) ==
        Color(image,NearbyPixel(pixel,3,2)) ==
        Color(image,NearbyPixel(pixel,1,3)) ==
        Color(image,NearbyPixel(pixel,2,3)) ==
        Color(image,NearbyPixel(pixel,3,3)) ==
        Color(image,NearbyPixel(pixel,1,4)) ==
        Color(image,NearbyPixel(pixel,3,4))
        and
        Color(image,NearbyPixel(pixel,2,1)) == Color(image,NearbyPixel(pixel,3,1))  # eyes same color
        and
        Color(image,NearbyPixel(pixel,1,0)) != Color(image,NearbyPixel(pixel,2,1))       # eyes diff color
        and
        Color(image,NearbyPixel(pixel,1,0)) != Color(image,NearbyPixel(pixel,2,4))       # between legs diff color
        and
        Color(image,NearbyPixel(pixel,1,0)) != Color(image,NearbyPixel(pixel,0,0))       # behind head diff color
        and
        Color(image,NearbyPixel(pixel,1,0)) != Color(image,NearbyPixel(pixel,0,3))       # behind leg diff color
        #and
        #Color(image,NearbyPixel(pixel,1,0)) != Color(image,NearbyPixel(pixel,0,4))       # behind foot diff color
    ):
        return "AMOGUS"
    else:
        return "NOPE"

def CheckSmolAmogusLeft(image, pixel):
    if(
        Color(image,pixel) == 
        Color(image,NearbyPixel(pixel,1,0)) == 
        Color(image,NearbyPixel(pixel,2,0)) ==
        Color(image,NearbyPixel(pixel,2,1)) ==
        Color(image,NearbyPixel(pixel,3,1)) ==
        Color(image,NearbyPixel(pixel,0,2)) ==
        Color(image,NearbyPixel(pixel,1,2)) ==
        Color(image,NearbyPixel(pixel,2,2)) ==
        Color(image,NearbyPixel(pixel,3,2)) ==
        Color(image,NearbyPixel(pixel,0,3)) ==
        Color(image,NearbyPixel(pixel,2,3))
        and
        Color(image,NearbyPixel(pixel,0,1)) == Color(image,NearbyPixel(pixel,1,1))  # eyes same color
        and
        Color(image,pixel) != Color(image,NearbyPixel(pixel,1,1))       # eyes diff color
        and
        Color(image,pixel) != Color(image,NearbyPixel(pixel,1,3))       # between legs diff color
        and
        Color(image,pixel) != Color(image,NearbyPixel(pixel,3,0))       # behind head diff color
        and
        Color(image,pixel) != Color(image,NearbyPixel(pixel,3,3))       # behind leg diff color
    ):
        return "AMOGUS"
    else:
        return "NOPE"

def CheckSmolAmogusRight(image, pixel):
    if(
        Color(image,NearbyPixel(pixel,1,0)) == 
        Color(image,NearbyPixel(pixel,2,0)) == 
        Color(image,NearbyPixel(pixel,3,0)) ==
        Color(image,NearbyPixel(pixel,0,1)) ==
        Color(image,NearbyPixel(pixel,1,1)) ==
        Color(image,NearbyPixel(pixel,0,2)) ==
        Color(image,NearbyPixel(pixel,1,2)) ==
        Color(image,NearbyPixel(pixel,2,2)) ==
        Color(image,NearbyPixel(pixel,3,2)) ==
        Color(image,NearbyPixel(pixel,1,3)) ==
        Color(image,NearbyPixel(pixel,3,3))
        and
        Color(image,NearbyPixel(pixel,2,1)) == Color(image,NearbyPixel(pixel,3,1))  # eyes same color
        and
        Color(image,NearbyPixel(pixel,1,0)) != Color(image,NearbyPixel(pixel,2,1))       # eyes diff color
        and
        Color(image,NearbyPixel(pixel,1,0)) != Color(image,NearbyPixel(pixel,2,3))       # between legs diff color
        and
        Color(image,NearbyPixel(pixel,1,0)) != Color(image,NearbyPixel(pixel,0,0))       # behind head diff color
        and
        Color(image,NearbyPixel(pixel,1,0)) != Color(image,NearbyPixel(pixel,0,3))       # behind leg diff color
    ):
        return "AMOGUS"
    else:
        return "NOPE"

#imageToParse = '10x10_test.png'
#imageToParse = '100x100_piece.png'
imageToParse = 'place_FULL.png'

file_name = os.path.join(os.path.dirname(__file__), imageToParse)
assert os.path.exists(file_name)

source = cv2.imread(file_name)

height, width, _ = source.shape

count = 0

LeftAmogi = []
RightAmogi = []

for y in range(0,height-4):
    for x in range(0, width-3):
        pixel = (x,y)
        if CheckAmogusLeft(source,pixel) == "AMOGUS":
            print("Left ", pixel)
            count += 1
            LeftAmogi.append(pixel)
        elif CheckAmogusRight(source,pixel) == "AMOGUS":
            print("Right ", pixel) 
            count += 1
            RightAmogi.append(pixel)

SmolLeftAmogi = []
SmolRightAmogi = []

for y in range(0,height-3):
    for x in range(0, width-3):
        pixel = (x,y)
        if CheckSmolAmogusLeft(source,pixel) == "AMOGUS":
            print("Smol Left ", pixel)
            count += 1
            SmolLeftAmogi.append(pixel)
        elif CheckSmolAmogusRight(source,pixel) == "AMOGUS":
            print("Smol Right ", pixel)
            count += 1
            SmolRightAmogi.append(pixel)

print("Total Amogi: ", count)


######    Visualizing Amogi    ######


def DrawLeftAmogus(image,pixel):
    image.putpixel(pixel,(255,0,0))
    image.putpixel(NearbyPixel(pixel,1,0),(255,0,0))
    image.putpixel(NearbyPixel(pixel,2,0),(255,0,0))
    image.putpixel(NearbyPixel(pixel,2,1),(255,0,0))
    image.putpixel(NearbyPixel(pixel,3,1),(255,0,0))
    image.putpixel(NearbyPixel(pixel,0,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,1,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,2,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,3,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,0,3),(255,0,0))
    image.putpixel(NearbyPixel(pixel,1,3),(255,0,0))
    image.putpixel(NearbyPixel(pixel,2,3),(255,0,0))
    image.putpixel(NearbyPixel(pixel,0,4),(255,0,0))
    image.putpixel(NearbyPixel(pixel,2,4),(255,0,0))
    image.putpixel(NearbyPixel(pixel,0,1),(255,255,255))
    image.putpixel(NearbyPixel(pixel,1,1),(255,255,255)) 

def DrawRightAmogus(image,pixel):
    image.putpixel(NearbyPixel(pixel,3,0),(255,0,0))
    image.putpixel(NearbyPixel(pixel,2,0),(255,0,0))
    image.putpixel(NearbyPixel(pixel,1,0),(255,0,0))
    image.putpixel(NearbyPixel(pixel,1,1),(255,0,0))
    image.putpixel(NearbyPixel(pixel,0,1),(255,0,0))
    image.putpixel(NearbyPixel(pixel,3,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,2,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,1,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,0,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,3,3),(255,0,0))
    image.putpixel(NearbyPixel(pixel,2,3),(255,0,0))
    image.putpixel(NearbyPixel(pixel,1,3),(255,0,0))
    image.putpixel(NearbyPixel(pixel,3,4),(255,0,0))
    image.putpixel(NearbyPixel(pixel,1,4),(255,0,0))
    image.putpixel(NearbyPixel(pixel,3,1),(255,255,255))
    image.putpixel(NearbyPixel(pixel,2,1),(255,255,255)) 

def DrawSmolLeftAmogus(image,pixel):
    image.putpixel(pixel,(255,0,0))
    image.putpixel(NearbyPixel(pixel,1,0),(255,0,0))
    image.putpixel(NearbyPixel(pixel,2,0),(255,0,0))
    image.putpixel(NearbyPixel(pixel,2,1),(255,0,0))
    image.putpixel(NearbyPixel(pixel,3,1),(255,0,0))
    image.putpixel(NearbyPixel(pixel,0,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,1,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,2,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,3,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,0,3),(255,0,0))
    image.putpixel(NearbyPixel(pixel,2,3),(255,0,0))
    image.putpixel(NearbyPixel(pixel,0,1),(255,255,255))
    image.putpixel(NearbyPixel(pixel,1,1),(255,255,255)) 

def DrawSmolRightAmogus(image,pixel):
    image.putpixel(NearbyPixel(pixel,3,0),(255,0,0))
    image.putpixel(NearbyPixel(pixel,2,0),(255,0,0))
    image.putpixel(NearbyPixel(pixel,1,0),(255,0,0))
    image.putpixel(NearbyPixel(pixel,1,1),(255,0,0))
    image.putpixel(NearbyPixel(pixel,0,1),(255,0,0))
    image.putpixel(NearbyPixel(pixel,3,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,2,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,1,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,0,2),(255,0,0))
    image.putpixel(NearbyPixel(pixel,3,3),(255,0,0))
    image.putpixel(NearbyPixel(pixel,1,3),(255,0,0))
    image.putpixel(NearbyPixel(pixel,3,1),(255,255,255))
    image.putpixel(NearbyPixel(pixel,2,1),(255,255,255)) 

img = Image.new('RGB', (width, height))

def IncrementDrawCount(drawCount,count):
    drawCount += 1
    print(str(drawCount) + "/" + str(count) + " drawn")
    return drawCount

drawCount = 0

for a in range(0,len(LeftAmogi)):
    DrawLeftAmogus(img,LeftAmogi[a])
    drawCount = IncrementDrawCount(drawCount,count)

for a in range(0,len(RightAmogi)):
    DrawRightAmogus(img,RightAmogi[a])
    drawCount = IncrementDrawCount(drawCount,count)

for a in range(0,len(SmolLeftAmogi)):
    DrawSmolLeftAmogus(img,SmolLeftAmogi[a])
    drawCount = IncrementDrawCount(drawCount,count)

for a in range(0,len(SmolRightAmogi)):
    DrawSmolRightAmogus(img,SmolRightAmogi[a])
    drawCount = IncrementDrawCount(drawCount,count)
    




expName = os.path.dirname(os.path.realpath(__file__))+'\\'+str(width)+"x"+str(height)+'_amogi.png'
img.save(expName)
img.show()



 