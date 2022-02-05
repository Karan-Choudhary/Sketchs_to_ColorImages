import matplotlib.pyplot as plt
import datetime
import os

def generate_images(model,test_input,tar,output_path):
    prediction = model(test_input,training=True)
    plt.figure(figsize=(15,15))

    display_list = [test_input[0], tar[0], prediction[0]]
    title = ['Input Image','Ground Truth','Predicted Image']

    for i in range(3):
        plt.subplot(1,3,i+1)
        plt.title(title[i])
        plt.imshow(display_list[i]*0.5*0.5)
        plt.axis('off')
    plt.savefig(os.path.join(output_path,"{}_result.png".format(datetime.datetime.now().strftime("%H-%M-%S"))))
    plt.show()