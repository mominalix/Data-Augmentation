import cv2
import numpy as np
from skimage import io
from skimage.transform import rotate, AffineTransform, warp
import matplotlib.pyplot as plt
import random
from skimage import img_as_ubyte
import os
from skimage.util import random_noise

#Lets define functions for each operation
def anticlockwise_rotation(image):
    return rotate(image, 90)

def clockwise_rotation(image):
    return rotate(image, -90)

def h_flip(image):
    return  np.fliplr(image)

def v_flip(image):
    return np.flipud(image)

def add_noise(image):
    return random_noise(image)

def blur_image(image):
    return cv2.GaussianBlur(img, (9,9),0)

#I would not recommend warp_shifting, because it distorts image, but can be used in many use case like
#classifying blur and non-blur images
def warp_shift(image):
    transform = AffineTransform(translation=(0,40))  #chose x,y values according to your convinience
    warp_image = warp(image, transform, mode="wrap")
    return warp_image


transformations = {'rotate anticlockwise': anticlockwise_rotation,
                   'rotate clockwise': clockwise_rotation,
                   'horizontal flip': h_flip,
                   'vertical flip': v_flip,
                   'adding noise': add_noise,
                   }  # use dictionary to store names of functions
images_path = os.path.join(os.getcwd(), 'sample images') # path to original images
augmented_path = os.path.join(os.getcwd(), 'images')  # path to store aumented images
images = []  # to store paths of images from folder

for im in os.listdir(images_path):  # read image name from folder and append its path into "images" array
    images.append(os.path.join(images_path, im))

images_to_generate = 1  # you can change this value according to your requirement
i = 89  # variable to iterate till images_to_generate
a = 1
for image in images:
    original_image = io.imread(image)
    print(image)
    transformed_image = None
    #     print(i)
    n = 0  # variable to iterate till number of transformation to apply
    transformation_count = random.randint(1, len(
        transformations))  # choose random number of transformation to apply on the image
    new_image_path = "%s/%s.jpg" % (augmented_path, i)
    #orig_image=img_as_ubyte(image)
    #orig_image= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #cv2.imwrite(new_image_path, image)
    for key in list(transformations):
        i = i + 1
        #key = random.choice(list(transformations))  # randomly choosing method to call
        transformed_image = transformations[key](original_image)
        new_image_path = "%s/%s.jpg" % (augmented_path, i)
        transformed_image = img_as_ubyte(
            transformed_image)  # Convert an image to unsigned byte format, with values in [0, 255].
        transformed_image = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB)  # convert image to RGB before saving it
        cv2.imwrite(new_image_path, transformed_image)  # save transformed image to path

# to generate more images, put above 3 statement inside while n<... loop