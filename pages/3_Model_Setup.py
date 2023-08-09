import streamlit as st

# Primary accent for interactive elements
primaryColor = '#FFFFFFF'

# Background color for the main content area
backgroundColor = '#FFFFFFF'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '##FFFFFFF'

# Color used for almost all text
textColor = '#000000'

font = "sans serif"

st.set_page_config(layout="wide")

col1, col2 = st.columns([1, 2.5])

with col1:
    st.image("images/ai.jpg", width=330)

with col2:
    st.title("Van Gogh Classifier with Pytorch")
    st.subheader("_Model Setup for AI Image Classification Using Pre-trained Models_")

st.divider()
st.markdown("_Project files are located on Github:_ [link](https://github.com/larsondg2000/VanGogh.git)")
st.header("Models and Training Files")

st.markdown("The project used three pre-trained models:")
st.write("1) VGG19 (weights='VGG19_Weights.DEFAULT')")
st.write("2) RegNet (weights='RegNet_Y_16GF_Weights.DEFAULT')")
st.write("3) EfficientNet (weights='EfficientNet_V2_L_Weights.DEFAULT')")
st.write("")
st.markdown("The models have pre-trained weights with a trainable classifier. It uses three python files to train "
            "the models:")
st.write("1) `train.py`: main() function call")
st.write("2) `train_functions.py`: all the required training functions")
st.write("3) `utils.py`: get_class()  function to return class list ")

st.header("")
st.header("Model Parameters")
st.write("* Optimizer: Adam")
st.write("* Loss Function : CrossEntropyLoss")
st.write("* Epochs: configurable using CLI")
st.write("* Learning Rate: configurable using CLI")
st.write("* Hidden Layers: configurable using CLI")
st.write("* Dropout: set to .4 to .5 (depending on model)")
st.write("* Batch Size: b_size set to 64")
st.write("* Save Directory: configurable using CLI (saves as model name_checkpoint.pth.)")

st.header("Image Data")
st.markdown("A custom dataset was created for the training, testing, and validation.  Images were downloaded and "
            "sorted into two classes: 'vangogh' and 'not_vangogh'. ")
st.write("")
st.markdown("The raw_images folder has all the images and this is the source of the images for this project:")

col11, col22 = st.columns(2)

with col11:
    st.markdown("Van Gogh Images (total paintings/discarded/total in dateset): 604")
    st.write("* Images from Van Gogh Gallery [link](http://www.vggallery.com/index.html)")
    st.write("* Paris (March 1886 - February 1888)- 225/17/208 paintings")
    st.write("* Saint-Remy (May 1889 - May 1890)- 143/4/139 paintings")
    st.write("* Auvers-sur-Oise (May 1890 - July 1890)- 76/1/75 paintings")
    st.write("* Arles (February 1888 - May 1889)- 186/4/182 paintings")
    st.write("* Totals: 630/26/604 (total paintings/discarded/total in dateset)")

with col22:
    st.markdown("Not Van Gogh  Images (random paintings from various time periods): 609")
    st.write("* The images were downloded from the National Gallery of "
             "Art: [link](https://www.nga.gov/collection/collection-search.html)")
    st.write("* Modern Art: [link](https://www.saatchiart.com/paintings/modern)")
    st.write("* Baroque- 80")
    st.write("* German Expressionist- 13")
    st.write("* Impressionist- 77")
    st.write("* Neo-classic- 23")
    st.write("* Post-Impressionist- 80")
    st.write("* Realist- 86")
    st.write("* Renaissance- 62")
    st.write("* Rococo- 64")
    st.write("* Romantic- 84")
    st.write("* Modern- 40")
    st.write("* Total: 609")

st.header("Dataset")
st.markdown("The images in the raw_images folder can be divided into train, test, and vaild folders using "
            "the `setup.py` along with functions in the `utils.py` file.  The `setup.py` randomly assigns raw "
            "images to the folders based on the following percentages:")
st.write("* Train 80%")
st.write("* Test 15%")
st.write("* Validation 5%")

st.header("Predictions")
st.markdown("There are three different prediction functions, each with a main() that calls various functions in "
            "the `predict_functions.py` file:")
st.write("1) `predict.py`:  uses the valid datasets to check the accuracy of the model using the valid dataset.")
st.write("2) `predict_random.py`: randomly selects five images from valid folder and displays image along with "
         "probability, prediction, and correct/incorrect prediction.")
st.write("3) `predict_image.py`: used to check a single unclassified image.")

st.header("Model Accuracy")
st.subheader("Model Accuracy during Validation:")
st.write("* VGG19: 93.8%")
st.write("* RegNet: 97.9%")
st.write("* EfficientNet: 95.8%")
st.subheader("Training and Test: Loss and Accuracy Plots")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("images/regnet 8.png", width=500)

with col2:
    st.image("images/vgg10 10.png", width=500)

with col3:
    st.image("images/effnet 10.png", width=500)