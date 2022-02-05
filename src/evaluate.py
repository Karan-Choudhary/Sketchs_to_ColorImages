import tensorflow as tf
import yaml
import argparse
from read_params import read_params
from get_data import get_data
from display.showOutput import generate_images
from tensorflow.keras.models import load_model
import datetime
import os

def evaluate(config_path):
    config = read_params(config_path)
    GEN_MODEL_DIR = config['model_dir']['generator']
    FINAL_SAMPLES = config['evaluate']['final_sample']
    OUTPUT_PATH = config['generate_output']['output_path']

    _,test_dataset = get_data(config_path)

    generator = load_model(GEN_MODEL_DIR)

    present_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    os.makedirs(os.path.join(OUTPUT_PATH,present_time), exist_ok=True)
    
    OUTPUT_PATH = os.path.join(OUTPUT_PATH,present_time)
    for example_input, example_target in test_dataset.take(FINAL_SAMPLES):
        generate_images(generator, example_input, example_target, OUTPUT_PATH)
        

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml",
                        help="Directory params.yaml")
    parsed_args = args.parse_args()
    evaluate(config_path = parsed_args.config)