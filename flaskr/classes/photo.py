from PIL import Image

class Photo(object):
    """
        Represents the uploaded image. 
    """

    @staticmethod
    def is_image_format_valid(image): # The uploaded photo is inserted and the image format is checked
        img = Image.open(image)
        image_format = img.format
        # If the format is different from jpeg or png, it is error and returns False.
        if image_format.lower() != "jpeg" and image_format.lower() != "png":
            print("The image format is not valid!")
            return False
        else:
            return True