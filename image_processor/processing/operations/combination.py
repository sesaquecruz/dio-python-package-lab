import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(image1, image2):
    assert image1.shape == image2.shape, "The images shape must be the same"
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (_, diff_image) = structural_similarity(gray_image1, gray_image2, full=True, data_range=1.0)
    diff_image = (diff_image*np.min(diff_image))/(np.max(diff_image)*np.min(diff_image))
    return diff_image

def transfer_histogram(image1, image2):
    matched_image = match_histograms(image1, image2, channel_axis=-1)
    return matched_image
