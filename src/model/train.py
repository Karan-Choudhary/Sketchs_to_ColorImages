import tensorflow as tf
from model.build import buildGenerator, buildDiscriminator
from model.loss.losses import discriminator_loss, generator_loss
import time
import yaml

# Build the discriminator
generator = buildGenerator()
# Build the discriminator
discriminator = buildDiscriminator()

# Build the optimizers
generator_optimizer = tf.keras.optimizers.Adam(2e-4, beta_1=0.5)
discriminator_optimizer = tf.keras.optimizers.Adam(2e-4, beta_1=0.5)

def read_params(config_path):
    with open(config_path,'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config

@tf.function()
def train(input_image,target,epoch):

    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        gen_output = generator(input_image,training=True)
        disc_real_output = discriminator([input_image,target],training=True)
        disc_generated_output = discriminator([input_image,gen_output],training=True)

        gen_total_loss, gen_gan_loss, gen_l1_loss = generator_loss(disc_generated_output,gen_output,target)
        disc_loss = discriminator_loss(disc_real_output,disc_generated_output)
    
    generator_gradients = gen_tape.gradient(gen_total_loss,generator.trainable_variables)
    discriminator_gradients = disc_tape.gradient(disc_loss,discriminator.trainable_variables)

    generator_optimizer.apply_gradients(zip(generator_gradients,generator.trainable_variables))
    discriminator_optimizer.apply_gradients(zip(discriminator_gradients,discriminator.trainable_variables))

    # with summary_writter.as_default():
    #     tf.summary.scalar('gen_total_loss',gen_total_loss,step=epoch)
    #     tf.summary.scalar('gen_gan_loss',gen_gan_loss,step=epoch)
    #     tf.summary.scalar('gen_l1_loss',gen_l1_loss,step=epoch)
    #     tf.summary.scalar('disc_loss',disc_loss,step=epoch)
    
def fit(train_ds,epochs):
    config = read_params('params.yaml')
    SAVE_GEN = config['model_dir']['generator']
    SAVE_DISC = config['model_dir']['discriminator']
    for epoch in range(epochs):
        start=time.time()

        for n, (input_image,target_image) in train_ds.enumerate():
            print(".",end="")
            if (n+1)%100 == 0:
                print()
            train(input_image,target_image,epoch)
        print()

        if (epoch+1)%5==0:
            checkpoint.save(file_prefix = checkpoint_prefix)
            generator.save(SAVE_GEN)
            discriminator.save(SAVE_DISC)

        
        print('Time taken for epoch {} is {} sec\n'.format(epoch+1,time.time()-start))