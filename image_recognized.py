from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import numpy as np


def image_check(image): # The uploaded photo is inserted and the image format is checked
    img = Image.open(image) 
    image_format = img.format
    # If the format is different from jpeg or png, it is error and returns False.
    if image_format.lower() != "jpeg" and image_format.lower() != "png":
        print("The image format is not valid!")
        return False
    else:
        return True

def image_recognized(img): # Image recognition function
    value = image_check(img)
    if value == True:
        model = VGG16()
        image = load_img(img,target_size=(224, 224))
        # Converting the image to array and then reshaping it.
        image = img_to_array(image)
        image = image.reshape((1,image.shape[0], image.shape[1], image.shape[2]))
        image = preprocess_input(image)
        # After performig the above steps, we are pre-process it and then predicting the output.
        y_pred = model.predict(image)
        first_list = decode_predictions(y_pred, top=1) # top=1 means which we are taking top 1 probability value for the particular prediction.
        #print(first_list)
        # The result is a list that contains a one-tuple list, so we look for the value in the second position of the tuple
        second_list = first_list[0]
        print(second_list)
        my_tuple = second_list[0]
        print(my_tuple)
        x, label, y = my_tuple
        print(label)
        final_label = label.replace(("_", " "))
        return final_label # Returns the image label
    else:
        return None

import os

def main():
    dic = {}
    count = 0
    for file in os.listdir('images'):
        print(file)
        full_path = 'images/' + file
        print(full_path)

        label = image_recognized(full_path)
        dic["Photo {}".format(count)] = label
        count += 1

    print(dic)

if __name__ == "__main__":
    main()