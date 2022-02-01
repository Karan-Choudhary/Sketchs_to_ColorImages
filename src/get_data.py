import yaml
import argparse
import tensorflow as tf
from read_params import read_params
from utils.preprocessing import load, resize, normalize,random_jitter

def load_image_train(image_file):
    input_image, real_image = load(image_file)
    input_image, real_image = random_jitter(input_image, real_image)
    input_image, real_image = normalize(input_image, real_image)
    return input_image, real_image

def load_image_test(image_file):
    config=read_params('params.yaml')
    IMG_WIDTH = config['data_load']['img_width']
    IMG_HEIGHT = config['data_load']['img_height']
    input_image, real_image = load(image_file)
    input_image, real_image = resize(input_image, real_image, IMG_HEIGHT, IMG_WIDTH) 
    input_image, real_image = normalize(input_image, real_image)
    return input_image, real_image

def get_data(config_path):
    config = read_params(config_path)
    train_path = config['data_path']['train_path']
    val_path = config['data_path']['val_path']
    BATCH_SIZE = config['data_load']['batch_size']
    BUFFER_SIZE = config['data_load']['buffer_size']


    # Get training data
    train_dataset = tf.data.Dataset.list_files(train_path+'\\*.png')
    train_dataset = train_dataset.map(load_image_train, num_parallel_calls=tf.data.experimental.AUTOTUNE)
    train_dataset = train_dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE)

    # Get validation data
    test_dataset = tf.data.Dataset.list_files(val_path+'\\*.png')
    test_dataset = test_dataset.map(load_image_test)
    test_dataset = test_dataset.batch(BATCH_SIZE)

    return train_dataset, test_dataset


if __name__ =="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default = "params.yaml",help="Directory params.yaml")
    parsed_args = args.parse_args()
    tain_dataset,test_dataset = get_data(config_path = parsed_args.config)
    print(train_dataset,test_dataset)