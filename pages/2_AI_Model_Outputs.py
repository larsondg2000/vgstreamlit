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

col31, col32 =st.columns([1, 2])

with col31:
    st.title("Model")
    st.title("Probabilities &")
    st.title("Predictions  ")

with col32:
    st.title("")
    st.image("images/cnn.jpg", width=700)

st.divider()

st.title("")
st.header("My Painting Probabilities and Predictions")
st.subheader("_Predictions and Probabilities from Three Models_")

col1, col2, col3 =st.columns(3)

with col1:
    st.image("images/eff_out.png")

with col2:
    st.image("images/out_reg.png")

with col3:
    st.image("images/vgg_out.png")

st.header("My Painting Probabilities and Predictions")
st.subheader("_Segmented Images with EfficientNet_")
col11, col21, col31 =st.columns(3)

with col11:
    st.image("images/close1_pred.png")

with col21:
    st.image("images/close2_pred.png")

with col31:
    st.image("images/close5_pred.png")

st.header("Random Paintings from validation Set")
st.subheader("_Random Van Gogh and Not Van Gogh Paintings with EfficientNet_")
col12, col22, col32 =st.columns(3)

with col12:
    st.image("images/rando1.png")

with col22:
    st.image("images/rando2.png")

with col32:
    st.image("images/rando4.png")

st.header("Famous Paintings")
st.subheader("_Da Vinci, Dali, and Surat Paintings with EfficientNet_")
col13, col23, col33 =st.columns(3)

with col13:
    st.image("images/mona.png")

with col23:
    st.image("images/dali.png")

with col33:
    st.image("images/surat_pred.png")