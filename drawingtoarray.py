import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def dta():
    im = np.array(Image.open('image.png'))
    print("Before trimming:",im.shape)
    im_trim = im[50:750, 50:750]
    print("After trimming:",im_trim.shape)
    img = Image.fromarray(im_trim)
    load_img_rz = np.array(img.resize((28,28)))
    Image.fromarray(load_img_rz)
    print("After resizing:",load_img_rz.shape)
    plt.imshow(load_img_rz)
    plt.show()