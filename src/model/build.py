import tensorflow as tf
from sample import downsample, upsample, downs
import argparse
import yaml

def read_params(config_path):
    with open(config_path,'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config

def buildGenerator():
    config = read_params('params.yaml')
    IMG_WIDTH = config['data_load']['img_width']
    IMG_HEIGHT = config['data_load']['img_height']
    OUTPUT_CHANNELS = config['model']['output_channels']
    inputs = tf.keras.layers.Input(shape=[IMG_HEIGHT,IMG_WIDTH,3])

    down_stack = [
        downsample(64,4, (None, 256, 256, 3), apply_batchnorm=False),
        downsample(128,4, (None, 128, 128, 64)),
        downsample(256, 4, (None, 64, 64, 128)),
        downsample(512, 4, (None, 32, 32, 256)),
        downsample(512, 4, (None, 16,16, 512)),
        downsample(512, 4, (None, 8, 8, 512)),
        downsample(512, 4, (None, 4, 4, 512)),
        downsample(512, 4, (None, 2, 2, 512))
    ]

    up_stack = [
        upsample(512, 4, (None, 1, 1, 512), apply_dropout=True),
        upsample(512, 4, (None, 2, 2, 1024), apply_dropout=True),
        upsample(512, 4, (None, 4, 4, 1024), apply_dropout=True),
        upsample(512, 4, (None, 8, 8, 1024)),
        upsample(256, 4, (None, 16, 16, 1024)),
        upsample(128, 4, (None, 32, 32, 512)),
        upsample(64, 4, (None, 64, 64, 256))
    ]

    initializer = tf.random_normal_initializer(0.,0.02)
    last = tf.keras.layers.Conv2DTranspose(OUTPUT_CHANNELS,4,strides=2,
                                                padding='same',
                                                kernel_initializer=initializer,
                                                activation='tanh')
    
    x = inputs

    skips = []
    for down in down_stack:
        x = down(x)
        skips.append(x)

    skips = reversed(skips[:-1])
    
    for up, skip in zip(up_stack,skips):
        x = up(x)
        x = tf.keras.layers.Concatenate()([x,skip])
    
    x = last(x)

    return tf.keras.Model(inputs=inputs,outputs=x)


def buildDiscriminator():
    config = read_params('params.yaml')
    IMG_WIDTH = config['data_load']['img_width']
    IMG_HEIGHT = config['data_load']['img_height']

    initializer = tf.random_normal_initializer(0.,0.02)
    inp = tf.keras.layers.Input(shape=[IMG_HEIGHT,IMG_WIDTH,3],name='input_image')
    tar = tf.keras.layers.Input(shape=[IMG_HEIGHT,IMG_WIDTH,3], name='target_image')

    x = tf.keras.layers.concatenate([inp,tar])

    down1 = downs(64,4,False)(x)
    down2 = downs(128,4)(down1)
    down3 = downs(256,4)(down2)

    zero_pad1 = tf.keras.layers.ZeroPadding2D()(down3)
    conv = tf.keras.layers.Conv2D(512,4,strides=1,
                                                                kernel_initializer=initializer,
                                                                use_bias=False)(zero_pad1)

    batchnorm1 = tf.keras.layers.BatchNormalization()(conv)

    leaky_relu = tf.keras.layers.LeakyReLU()(batchnorm1)

    zero_pad2 = tf.keras.layers.ZeroPadding2D()(leaky_relu)

    last = tf.keras.layers.Conv2D(1,4,strides=1,
                                                            kernel_initializer= initializer)(zero_pad2)
    
    return tf.keras.Model(inputs=[inp,tar],outputs=last)