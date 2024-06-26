# Streamlit Project for Van Gogh 

![alt-text](vg_mod.png "van Gogh Modern")

## _uses a subset from the VanGogh repository to create the streamlit projetct_

<img alt="alt-text" height="40" src="streamlit.png" title="Streamlit" width="200"/>

## Van Gogh Painting Classification using Pytorch and Pre-trained Models

<img alt="alt-text" height="40" src="pytorch.jpg" title="PyTorch" width="200"/>

## Models
The project uses outputs from three pre-trained models:
  1) VGG19 (weights='VGG19_Weights.DEFAULT')
  2) RegNet (weights='RegNet_Y_16GF_Weights.DEFAULT')
  3) EfficientNet (weights='EfficientNet_V2_L_Weights.DEFAULT')

The models have pre-trained weights with a trainable classifier. It uses three python files to train the models:
  1) `train.py`: main() function call
  2) `train_functions.py`: all the required training functions
  3) `utils.py`: get_class()  function to return class list 

## Model Parameters
* Optimizer: Adam
* Loss Function : CrossEntropyLoss
* Epochs: configurable using CLI
* Learning Rate: configurable using CLI
* Hidden Layers: configurable using CLI
* Dropout: set to .4 to .5 (depending on model)
* Batch Size: b_size set to 64
* Save Directory: configurable using CLI (saves as "model name"_checkpoint.pth.)

## Accuracy
All three models achieved >90% accuracy during the validation runs after training.  The models results were fairly close with the Regnet model performing the best. 

![alt-text](effnet10.png "Accuracy")

## Image Data
A custom dataset was created for the training, testing, and validation. Images were downloaded and sorted into two classes: "Van Gogh" and "not Van Gogh".  

The raw_images folder has all the images and this is the source of the images for this project:

    Van Gogh Images (total paintings/discarded/total in dateset): 605
        (http://www.vggallery.com/index.html)
        Paris (March 1886 - February 1888)- 225/17/208 paintings
        Saint-Remy (May 1889 - May 1890)- 143/4/139 paintings
        Auvers-sur-Oise (May 1890 - July 1890)- 76/1/75 paintings
        Arles (February 1888 - May 1889)- 186/4/182 paintings
        Totals: 630/26/604 (total paintings/discarded/total in dateset)

    Not Van Gogh  Images (random paintings from various time periods): 609
        Baroque- 80
        German Expressionist- 13
        Impressionist- 77
        Neo-classic- 23
        Post-Impressionist- 80
        Realist- 86
        Renaissance- 62
        Rococo- 64
        Romantic- 84
        Modern- 40
        Total: 609

        The images were downloded from the National Gallery of Art:
        https://www.nga.gov/collection/collection-search.html
        
        Modern Art:
        https://www.saatchiart.com/paintings/modern

## Dataset
The images in the raw_images folder can be divided into train, test, and vaild folders using the `setup.py` along with functions in the `utils.py` file.  The `setup.py` randomly assigns raw images to the folders based on the following percentages:
* Train 80%
* Test 15%
* Validation 5%

At the end of the setup, the count_images() function counts all the images in the train, test, and valid folders as a check.

For my training, testing, and validation I used the following folder structure:

Data\

  test\
  
    not_vangogh\
    
    vangogh\
  
  train\
  
    not_vangogh\
    
    vangogh\
  
  valid\
  
    not_vangogh\
    
    vangogh\

There are some additional painting images in the sample_paintings folder that are not classified.

## Prediction App
Uses `predict_functions.py` and `predict_image.py` file to predict a user  uploaded image. It uses the 
RegNet model for the prediction and displays the probability the image is "van Gogh" or "not van Gogh"

![alt-text](rando4.png "Prediction")
    
