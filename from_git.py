import time
import numpy as np

import cv2
from pathlib import Path

#https://github.com/robintw/RPiNDVI/blob/master/ndvi.py

def disp_multiple(im1=None, im2=None, im3=None, im4=None):
    """
    Combines four images for display.
    """
    height, width = im1.shape

    combined = np.zeros((2 * height, 2 * width, 3), dtype=np.uint8)

    combined[0:height, 0:width, :] = cv2.cvtColor(im1, cv2.COLOR_GRAY2RGB)
    combined[height:, 0:width, :] = cv2.cvtColor(im2, cv2.COLOR_GRAY2RGB)
    combined[0:height, width:, :] = cv2.cvtColor(im3, cv2.COLOR_GRAY2RGB)
    combined[height:, width:, :] = cv2.cvtColor(im4, cv2.COLOR_GRAY2RGB)

    return combined


def label(image, text):
    """
    Labels the given image with the given text
    """
    return cv2.putText(image, text, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)


def contrast_stretch(im):
    """
    Performs a simple contrast stretch of the given image, from 5-95%.
    """
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out


def run():
    image = cv2.imread('nc.jpg')


    # Get the individual colour components of the image
    b, g, r = cv2.split(image)

    # Calculate the NDVI

    # Bottom of fraction
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom == 0] = 0.01  # Make sure we don't divide by zero!

    ndvi = (r.astype(float) - b) / bottom
    ndvi = contrast_stretch(ndvi)
    ndvi = ndvi.astype(np.uint8)

    # Do the labelling
    label(b, 'Blue')
    label(g, 'Green')
    label(r, 'NIR')
    label(ndvi, 'NDVI')

    # Combine ready for display
    combined = disp_multiple(b, g, ndvi, r)

    print(ndvi)

    # Display
    cv2.imshow('image', combined)


    # If we press ESC then break out of the loop
    c = cv2.waitKey()


    # Important cleanup here!
    #cv2.destroyAllWindows()



if __name__ == '__main__':
    run()