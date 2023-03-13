from skimage.transform import resize

def resize_image(image, proportion):
	assert 0 <= proportion <= 1, "The proportion must be in the range [0, 1]"
	height = round(image.shape[0]*proportion)
	width = round(image.shape[1]*proportion)
	resized_image = resize(image, (height, width), anti_aliasing=True)
	return resized_image
