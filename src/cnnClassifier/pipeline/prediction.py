import numpy as np
from tensorflow.keras.models import load_model #NEED CHANGES
from tensorflow.keras.preprocessing import image
import os


MODEL_PATH = os.path.join("artifacts", "training", "model.h5")
class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        #model = load_model(os.path.join("model", "model.h5"))
        model = load_model(MODEL_PATH)
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)
       

        if result[0] == 1:
            prediction = 'Tumor'
            return [{ "image" : prediction}]
        else:
            prediction = 'Normal'
            return [{ "image" : prediction}]
        

    