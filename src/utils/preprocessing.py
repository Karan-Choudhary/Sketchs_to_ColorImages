import tensorflow as tf
import yaml


def read_params(config_path):
    with open(config_path, 'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config


def load(image_file):
    image = tf.io.read_file(image_file)
    image = tf.image.decode_png(image)
    w = tf.shape(image)[1]

    w = w//2

    real_image = image[:, :w, :]
    input_image = image[:, w:, :]

    input_image = tf.cast(input_image, tf.float32)
    real_image = tf.cast(real_image, tf.float32)

    return input_image, real_image


def resize(input_image, real_image, height, width):
    input_image = tf.image.resize(
        input_image, [height, width], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    real_image = tf.image.resize(
        real_image, [height, width], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    return input_image, real_image


def normalize(input_image, real_image):
    input_image = (input_image/127.5) - 1
    real_image = (real_image/127.5) - 1
    return input_image, real_image


def random_crop(input_image, real_image):
    config = read_params('params.yaml')
    stacked_images = tf.stack([input_image, real_image], axis=0)
    cropped_image = tf.image.random_crop(stacked_images, size=[
                                         2, config['data_load']['img_height'], config['data_load']['img_width'], 3])
    return cropped_image[0], cropped_image[1]


@tf.function
def random_jitter(input_image, real_image):
    input_image, real_image = resize(input_image, real_image, 286, 286)
    input_image, real_image = random_crop(input_image, real_image)

    if tf.random.uniform(()) > 0.5:
        input_image = tf.image.flip_left_right(input_image)
        real_image = tf.image.flip_left_right(real_image)

    return input_image, real_image
