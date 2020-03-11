import os
from PIL import Image


STD_WIDTH = 400
STD_HEIGHT = 560


# This function is used to resize only an image file by providing the path (can be absolute or relative to RevExtraction directory) to the image
def resizeImage(img_path = ''):
    if not img_path.endswith('.jpg'):
        print(img_path + ' is not a valid image. Provide a valid image file')
        return

    should_resize = False
    img = Image.open(img_path)
    width, height = img.size

    if (width > STD_WIDTH):
        width = STD_WIDTH
        should_resize = True
    if (height > STD_HEIGHT):
        height = STD_HEIGHT
        should_resize = True
    if should_resize:
        newsize = (width, height)
        img = img.resize(newsize, Image.ANTIALIAS)
        img.save(img_path)
        # If you want to see the new resized image decomment the line below
        # img.show()


# This function is used to resize all the images in a set, provide only the set images directory, i.e. 'DMR-17-Images'
def resizeSet(set_name = 'DMX-22-Images'):
    # Get current working directory
    dir_path = os.getcwd() + '/' + set_name
    files = os.listdir(dir_path)
    for file in files:
        img_path = dir_path + '/' + file
        resizeImage(img_path)
    set_name = set_name[:set_name.rfind('-')]
    print('Resize for the ' + set_name + ' set has been successful')


# This function is used to resize an entire block of sets
def resizeBlock():
    cwd = os.getcwd()
    dirs = os.listdir(cwd)
    for dir in dirs():
        if os.path.isdir(dir):
            resizeSet(dir)
    print('Resize for the entire block has been successful')


resizeSet('DMX-22-Images')
