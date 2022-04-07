from pickletools import string1
import cv2
import os

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

for y in range(0,height-4):
    for x in range(0, width-3):
        pixel = (x,y)
        if CheckAmogusLeft(source,pixel) == "AMOGUS":
            print("Left ", pixel)
            count += 1
        elif CheckAmogusRight(source,pixel) == "AMOGUS":
            print("Right ", pixel) 
            count += 1

for y in range(0,height-3):
    for x in range(0, width-3):
        pixel = (x,y)
        if CheckSmolAmogusLeft(source,pixel) == "AMOGUS":
            print("Smol Left ", pixel)
            count += 1
        elif CheckSmolAmogusRight(source,pixel) == "AMOGUS":
            print("Smol Right ", pixel)
            count += 1

print("Total Amogi: ", count)


 