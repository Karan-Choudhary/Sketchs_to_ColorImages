import tensorflow as tf
import yaml
import os
from model.train import fit
import argparse
from read_params import read_params
from get_data import get_data
from display.showOutput import generate_images
from tensorflow.keras.models import load_model


def train_model(config_path):
    config = read_params(config_path)
    EPOCHS = config['model']['epochs']

    train_dataset, test_dataset = get_data(config_path)
    fit(train_dataset, EPOCHS)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml",
                      help="Directory params.yaml")
    parsed_args = args.parse_args()
    train_model(config_path=parsed_args.config)
