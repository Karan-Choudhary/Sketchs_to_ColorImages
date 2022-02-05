## Sketch to Color Image Generation Using Conditional GANs
* Sketch to Color Image generation is an image-to-image translation model using [Conditional Generative Adversarial Networks](https://arxiv.org/abs/1411.1784)
* This project is developed with [DVC](https://dvc.org/) pipeline
* Dataset used - [Anime Sketch Colorization Pair](https://www.kaggle.com/ktaebum/anime-sketch-colorization-pair)\
* Model is only trained for 35 epochs on Google Colab
* You can train it according to your need by changing parameters in [params.yaml](https://github.com/Karan-Choudhary/Sketchs_to_ColorImages/blob/main/params.yaml) file
* [U-Net architecture](=U-Net%20is%20an%20architecture,architecture%20of%20a%20convolutional%20network.&text=In%20total%20the%20network%20has%2023%20convolutional%20layers.,-Original%20MATLAB%20Code) is followed for building Generator and Discriminator Models.

### Requirements
* [Create a new virtual environment](https://docs.python.org/3/library/venv.html).
* Python 3.6 or greater.
* DVC
* Run Command-
```
pip install -r requirements.txt
```

### Usage:
* Change parameters and directories according to your system (recommendation - do not change) in [params.yaml](https://github.com/Karan-Choudhary/Sketchs_to_ColorImages/blob/main/params.yaml).
* Setup the Directory named ***Results*** in the same directory.
* Make sure you have DVC initialized in the same directory</br>
You can do it with the command:
```
dvc init
```
* Add **data\train** & **data\val** for data tracking in dvc by using command:
```
dvc add data\train
dvc add data\val
```
* Finally, run:
```
dvc repro
```
* Trained models will be saved in ***saved_models*** directory.
* Results will be saved in ***Results\present_datatime*** directory with name **present_time_result.png**.
 
Warning: Do not try to change **dvc.lock file** and ***.dvc directory***

### Results:
![14-31-08_result](https://user-images.githubusercontent.com/54716931/152635488-6db2cc5e-2a20-4b9f-bba2-2d4de6bc368b.png)
![14-31-49_result](https://user-images.githubusercontent.com/54716931/152635490-c95f15ec-a72f-4cea-bfa0-06ca002ec844.png)
