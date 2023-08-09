import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
from predict_functions import load_checkpoint, predict_image

# Primary accent for interactive elements
primaryColor = '#7792E3'

# Background color for the main content area
backgroundColor = '#F39C12'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#B9F1C0'

# Color used for almost all text
textColor = '#FFFFFF'

font = "sans serif"

st.set_page_config(layout="wide")

col1, col2 = st.columns([1, 2.5])

with col1:
    st.image("images/starrynight.jpg", width=330)

with col2:
    st.title("Is it a Van Gogh?")
    st.subheader("_Analysis of a painting to determine if it could be an authentic Van Gogh_")
st.divider()

st.header("Vincent van Gogh")

col3, col4 = st.columns([1, 4.5])

with col3:
    st.image("images/vg.jpg", width=200)

with col4:
    content3 = "Vincent van Gogh (1853-1890) was a Dutch post-impressionist painter whose profound impact on the art " \
           "world continues to resonate today. Renowned for his emotionally charged and vibrant works, " \
           "Van Gogh's unique artistic style is characterized by bold brushwork, intense color palettes, " \
           "and an unparalleled ability to convey raw human emotion. Despite facing personal struggles and limited " \
           "recognition during his lifetime, his art has achieved legendary status, inspiring generations with " \
           "iconic pieces like Starry Night and Sunflowers. Van Gogh's innovative approach to depicting nature, " \
           "portraits, and everyday life has left an indelible mark on art history, cementing his place as a " \
           "visionary artist whose legacy remains both influential and enduring."

    st.markdown(content3)
st.header("")
st.header("Project Overview")

col3, col4 = st.columns([1, 4.5])

with col3:
    st.image("images/vangogh_crop.jpg", width=200)

with col4:
    content2 = "Welcome to my exploration of an intriguing painting, as I try to determine its authenticity " \
           "as a potential Van Gogh masterpiece. My examination examination covers multiple dimensions: starting " \
           "with the front, I will examine the brushwork, color palette, and composition, comparing them against the " \
           "renowned artist's distinctive style. Turning to the back, I will examine the frame and look for any " \
           "hidden clues. The signature, a key element, will be compared to known Van Gogh signed paintings. " \
           "Excitingly, we embrace cutting-edge technology by harnessing an AI image classifier, " \
           "a novel technique in the realm of art authentication. This innovative tool aids us in pattern " \
           "recognition and style analysis, providing a fresh perspective to complement traditional methods. " \
           "As we synergize traditional methods with modern advancements, join me on this captivating journey " \
           "to uncover the truth behind this captivating artwork's origins."

    st.markdown(content2)

st.header("")
st.header("Traditional Authentication Methods")

col5, col6 = st.columns([1, 4.5])

with col5:
    st.image("images/vganalysis.jpg", width=200)

with col6:
    content4 = "Authenticating a painting is a meticulous process that involves a combination of art historical " \
               "research," \
           " scientific analysis, and expert judgment. Art experts and historians scrutinize the provenance, or the" \
           " documented history of ownership, to trace the artwork's origins and verify its trajectory. Scientific " \
           "techniques like spectroscopy, radiography, and pigment analysis help analyze materials and techniques " \
           "used, providing insights into the era and artist's practices. Brushwork, style, and composition are " \
           "compared to the artist's known works and periods, assessing consistency. Additionally, handwriting " \
           "analysis, if relevant, can authenticate signatures and inscriptions. Collaboration between art " \
           "historians, conservators, forensic experts, and technology specialists enhances the accuracy of " \
           "evaluations. Due to the intricate nature of art forgery, a multi-faceted approach is crucial to establish" \
           " the authenticity of a painting with a high degree of confidence."

    st.markdown(content4)

st.header("")
st.header("What Is AI?")

col7, col8 = st.columns([1, 4.5])

with col7:
    st.image("images/a12.png", width=200)

with col8:
    content5 = "Artificial Intelligence (AI) stands at the forefront of modern technological advancement, " \
               "revolutionizing various facets of our lives. At its core, AI refers to the development of " \
               "computer systems that can perform tasks that typically require human intelligence. One " \
               "remarkable application of AI is image classification, a process in which machines learn to " \
               "interpret and categorize images based on patterns and features. This breakthrough technology " \
               "empowers computers to distinguish between various objects, scenes, and even artistic styles, " \
               "with remarkable accuracy. By utilizing vast datasets and advanced algorithms, AI image " \
               "classifiers can discern intricate details that might escape the human eye, enhancing fields " \
               "ranging from healthcare to art authentication. As AI continues to evolve, its capacity to analyze, " \
               "understand, and interpret visual information promises to reshape industries and enrich our " \
               "understanding of the world around us."

    st.markdown(content5)

st.header("")
st.header("_Sound Interesting?_")
para2 = "Upload an image and check the probability it's a van Gogh painting." \

para3 = "A trained AI model predicts the probability it's a van Gogh."

st.markdown("<h5 style='text-align: center; color: blue;'>"
            f"{para2}"
            "</h5>", unsafe_allow_html=True)

col9, col10, col11 = st.columns([3,3,3])

with col9:
    st.write("")

with col10:

    uploaded_file = st.file_uploader("Upload your image (JPG, JPEG, or PNG only)", accept_multiple_files=False)

    st.markdown("<h6 style='text-align: center; color: blue; font-style: italic;'>"
                f"{para3}"
                "</h6>", unsafe_allow_html=True)
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        plt.imshow(image)
        plt.axis("off")
        model = load_checkpoint("RegNet_checkpoint.pth")
        predict_image(model,
                      uploaded_file,
                      class_names = ['not_vangogh', 'vangogh'],
                      gpu="gpu")

with col11:
    st.write("")
