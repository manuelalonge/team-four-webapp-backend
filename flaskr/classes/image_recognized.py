from tensorflow.keras.applications.vgg19 import VGG19, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from flaskr.classes.photo import Photo
from tensorflow.keras.models import Model

class ImageRecognized(object):
    """
        It represents the recognition of the object within the image
    """

    @staticmethod
    def image_recognized(imag):
        img = Photo()
        value = img.is_image_format_valid(imag)
        if value == True:
            base_model = VGG19(weights = 'imagenet')
            # model = Model(inputs=base_model.input, outputs=base_model.get_layer('block4_pool').output)
            image = load_img(imag,target_size=(224, 224))
            # Converting the image to array and then reshaping it.
            image = img_to_array(image)
            image = image.reshape((1,image.shape[0], image.shape[1], image.shape[2]))
            image = preprocess_input(image)
            # After performig the above steps, we are pre-process it and then predicting the output.
            y_pred = base_model.predict(image)
            first_list = decode_predictions(y_pred, top=1) # top=1 means which we are taking top 1 probability value for the particular prediction.
            # The result is a list that contains a one-tuple list, so we look for the value in the second position of the tuple
            second_list = first_list[0]
            my_tuple = second_list[0]
            x, label, y = my_tuple
            return label # Returns the image label
        else:
            return None