from flask import Flask, request, jsonify
import tensorflow
from tensorflow.keras.models import load_model
from flask_cors import CORS
import numpy as np
import cv2
import os, io, sys, datetime
import base64
from base64 import encodebytes
from PIL import Image


def load(image_file):
    image = tensorflow.io.read_file(image_file)
    image = tensorflow.image.decode_png(image)
    image = tensorflow.cast(image, tensorflow.float32)
    return image

def resize(image, height, width):
    image = tensorflow.image.resize(image, [height, width], method=tensorflow.image.ResizeMethod.NEAREST_NEIGHBOR)
    return image

def normalize(image):
    image = (image / 127.5) - 1
    return image

def load_image_test(image_file):
    image = load(image_file)
    image = resize(image, 256, 256)
    image = normalize(image)
    return image

def get_response_image(image_path):
    pil_img = Image.open(image_path, mode='r') # reads the PIL image
    byte_arr = io.BytesIO()
    pil_img.save(byte_arr, format='PNG') # convert the PIL image to byte array
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    pil_img.close()
    os.remove(image_path)
    return encoded_img

app = Flask(__name__)

CORS(app)

@app.route('/getFiles', methods=['POST'])
def home():
    if request.method == "POST":
        files = request.files.getlist("images")
        
        imagesRec = []
        for file in files:
            imagesRec.append(file.read())
        
        for filename in os.listdir("uploads"):
            os.remove("uploads/" + filename)
            
        for image in imagesRec:
            npimg = np.fromstring(image, np.uint8)
            img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img.astype('uint8'))
            rawBytes = io.BytesIO()
            img.save(rawBytes, "PNG")
            
            path_to_save = os.path.join(os.getcwd(), "uploads")
            img.save(os.path.join(path_to_save, datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".png"))
            cv2.waitKey(2000)
            
        file_path = "uploads"
        evaluation_data = tensorflow.data.Dataset.list_files(file_path+'\\*.png')
        evaluation_data = evaluation_data.map(load_image_test)
        evaluation_data = evaluation_data.batch(len(imagesRec))
        
        generator = load_model("saved_models\generator\gen.h5")
        
        path_to_save = os.path.join(os.getcwd(), "results")
        
        for input_image in evaluation_data:
            prediction = generator(input_image, training=True)
            for img in prediction:
                tensorflow.keras.preprocessing.image.save_img(os.path.join(path_to_save, datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".png"), img)
                cv2.waitKey(2000)
        
        for filename in os.listdir("uploads"):
            os.remove("uploads/" + filename)
        
        encoded_images = []
        for image_path in os.listdir("results"):
            image_path = os.path.join("results", image_path)
            encoded_images.append(get_response_image(image_path))
        
        return jsonify({"images": encoded_images})
    
if __name__ == "__main__":
    app.run()
    