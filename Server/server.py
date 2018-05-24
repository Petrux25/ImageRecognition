###############Import Section####################

import sys            #Imports system fuctions
from PIL import Image #imports the image library



#############Code Section########################


#Funtion: OpenImage
#Input: name of an image in the actual directory
#Output: grayscaled image
#E.g
# >>> OpenImageGrayScale("imagename.jpg")
# >>> img  

def OpenImageGrayScale(name):
    try:
        img = Image.open(name).convert('LA')      #Opens an image and 
        return img                                #applies gray scale
    except OSError as err:
        print("OS error: {0}".format(err))        #Returns none if file
        return None                               #doesn't exist

###########OpenImageGrayScale##############


#Funtion: CreateMatrix
#Input: width, height
#Output: initialized matrix with zeros
#E.g
# >>> CreateMatrix(2,5)
# >>> [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def CreateMatrix(width,height): 
    return [[0 for x in range(width)] for y in range(height)] 
    
###########CreateMatrix##############
    

#Funtion: Local binary pattern
#Input: grayscaled image
#Output: image
#E.g
# >>> LocalBinaryPattern(image)
# >>> image

def LocalBinaryPattern(img):
    dimensions=img.size #Gets the dimensions of img
    width=dimensions[0] #Gets the width of img
    height=dimensions[1] #Gets the height of img
    pixels=img.load() #loads the pixels of the image
    
###########LocalBinaryPattern##############

