from PIL import Image
import cv2
import numpy as np

from tkinter.filedialog import *

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
ASCII_CHARS = ASCII_CHARS[:: -1]

def gray_img():                                                         # This function is dedicated to convert input image to a grayscaled image.

    img = Image.open(askopenfilename())                                 #Image file is opened
    gray = img.convert('L')                                             #File is converted to greyscale
    gray = gray.save('Grey.jpg')                                        #Converted image is saved.


def cartoon():                                                          # This function is dedicated to convert input image to a cartoonifyed image.
    
    photo = askopenfilename()                                           #Image file is opened
    pic = cv2.imread(photo)                                             #Image file is read.

    grey = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)                        #The image is first converted to a grayscaled image.
    grey = cv2.medianBlur(grey, 5)                                      #It is then blurred.
    edges = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)       #Adjusting its dimensions.

    colour = cv2.bilateralFilter(pic, 9, 250, 250)                                                      #Colour corrections are performed
    cartoon = cv2.bitwise_and(colour, colour, mask = edges)

    cv2.imwrite("cartoon.jpg", cartoon)                                 #Finalised cartoonifyed image is produced and saved.


def sketch():                                                           # This function is dedicated to convert input image to a sketched image.
    
    photo = askopenfilename()                                           #Image file is opened
    copy_photo = cv2.imread(photo)                                      #Image file is read.

    grey_img = cv2.cvtColor(copy_photo, cv2.COLOR_BGR2GRAY)             #The image is first converted to a grayscaled image.
    invert = cv2.bitwise_not(grey_img)                                  #The grayscaled image is then colour-inverted.
    blur = cv2.GaussianBlur(invert, (21, 21), 0)                        #Resulting image is blurred.
    invertedblur = cv2.bitwise_not(blur)                                #Then, it is inverted again.
    sketch = cv2.divide(grey_img, invertedblur, scale = 256.0)      
    cv2.imwrite("sketch.png", sketch)                                   #Image is finally converted to a sketch and saved.                           
    




''' This block of code will display and save an ASCII-characters equivalent of the input image.
    Several functions are required for this, and are discussed below.'''

def resize (image, new_width = 100):                                    #This function is used to resize the input image for conversion.
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int(aspect_ratio * new_width)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image                                                    #Returns the resized image to the do() finction.

def grayscale(image):                                                   #Returns the greyed image to the do() function.
    
    return image.convert('L')

def modify(image, buckets = 25):                                        #This function compares the pixels of the image with the ASCII characters, and matches the two according to the pixel intensity.
    
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)                                          #Returns the ASCII character equivalent of the image pixels to do() function.

def do(image, new_width = 100):                                         #This function is dedicated to, finally, render the image into ASCII characters.

    
    image = resize(image)                                                  #Receives resized image from resize() function.
    image = grayscale(image)                                               #Recives greyed image from grayscale() function.

    pixels = modify(image)                                                 #ASCII equivalent of the pixels is returned.
    len_pixels = len(pixels)                                               #Length of the total characters returned is calculated.

    new_image = [pixels[index:index + new_width] for index in range(0, len_pixels, new_width)]
    return '\n'.join(new_image)                                            #Finally, the characters are joined together to form the image.

def start():

    image = Image.open(askopenfilename())                                   #An image file is opened.

    image = do(image)                                                       #And passed to the do() function. the do() function, then, returns the desired image.
    
    print(image)                                                            #The converted image is printed on the screen.

    with open("ascii_image.txt", "w") as f:                                 #It is saved as a .txt file, in the same location as the program.
        f.write(image)

    f.close()


password = "my_Program@2021"                                                #Password protects the program run from unauthorised access.

print("\n***************|    Welcome to DEVELOPTERS PHOTO_KIT    |***************\n") #Introduction

entry = input("To enter, please enter the password: ")

turn = "Y"
if (entry == password):                                                     #The program runs only if the user inputs  the correct password.

    while (turn == "Y" or turn == "y"):                                     #This condition asks whether the user wants to continue after every turn.
        
        choice = input("What would you like to convert your image to: \n 1. Asciiform \n 2. Grayscaled \n 3. Cartoonify \n 4. Sketch \n")
        if (choice == "1"):                                                 #ASCII-characters conversion
            start()
            turn = input("Wanna continue? (Y/N): ")
        elif (choice == "2"):                                               #Conversion to greyscaled image
            gray_img()
            turn = input("Wanna continue? (Y/N): ")
        elif (choice == "3"):                                               #Cartoonify image
            cartoon()
            turn = input("Wanna continue? (Y/N): ")
        elif(choice == "4"):                                                #Conversion of image to sketch
            sketch()
            turn = input("Wanna continue? (Y/N): ")
        else:
            print("Wrong choice")

    print("\n~~~~~~~~~~~~~~~|   Thanks for tuning in :D   |~~~~~~~~~~~~~~~")

else:
    print("Wrong password :x !!!")
    
    





