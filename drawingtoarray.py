
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from tensorflow import keras

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.144])

def dta():
    im = np.array(Image.open('image.png'))
    im = rgb2gray(im)
    print("Before trimming:",im.shape)
    im_trim = im[50:750, 50:750]
    print("After trimming:",im_trim.shape)
    img = Image.fromarray(im_trim)
    load_img_rz = np.array(img.resize((28,28)))
    load_img_rz.reshape(28, 28).astype('float32')
    Image.fromarray(load_img_rz)
    f = open("class_names.txt","r")
    class_names = f.readlines()
    class_names = [c.replace('\n','').replace(' ','_') for c in class_names]
    f.close()
    model = keras.models.load_model('hmm')
    pred = model.predict(np.expand_dims(load_img_rz, axis=0))[0]
    ind = (-pred).argsort()[:5]
    latex = [class_names[x] for x in ind]
    print(latex)

    print("After resizing:",load_img_rz.shape)
    plt.imshow(load_img_rz)
    plt.show()
