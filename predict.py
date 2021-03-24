from keras.layers import Input
from centernet import CenterNet
from PIL import Image

centernet = CenterNet()

while True:
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error!')
    else:
        r_image = centernet.detect_image(image)
        r_image.show()
        r_image.save('./res.jpg')
    if img == '0':
        break
centernet.close_session()
    