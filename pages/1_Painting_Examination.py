import streamlit as st

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

st.title("Painting Examination")
st.subheader("_Inspection of the Front, Back, and Signature_")
st.divider()

st.header("Front of Painting")
st.subheader("Comparison to Other Works")

content2 = "The style of the painting is like others from Van Gogh, the subject matter of wheat fields and cypress " \
           "trees appear frequently in his paintings.  Based on the style and subject matter, it is probably from the" \
           " time he was in Saint Remy.  Examining his other works, three paintings standout as very similar to " \
           "this painting- Wheatfield with Cypresses (June 1889), Road with Cypress and Star (May 1890), and " \
           "Wheatfiled with Crows (July 1890). Road with Cypress and Stars (shown below) looks like a night version " \
           "of my painting.  The road and cypress tree, along with the cottage in the background, look almost " \
           "identical. The Road with Cypress and Star is believed to be one of his final paintings in Saint Remy " \
           "before moving to Auvers-sur-Oise.  " \

st.markdown(content2)

col1, col2, col3, col4  = st.columns([1,2, 2, 1])

with col1:
    st.write("")

with col2:
    st.write("")
    st.image("images/road_cypress_stars.jpg", width=285)
    st.caption("Road with Cypress and Star (1890)")

with col3:
    st.write("")
    st.image("images/vangogh_crop.jpg", width=475)
    st.caption("Front of My Painting")

with col4:
    st.write("")

st.subheader("Brush Strokes and Style")

content3 = "Vincent van Gogh's painting style is renowned for its distinctive and innovative qualities. He was a " \
           "master of post-impressionism, a movement that rejected the strict realism of traditional art in " \
           "favor of expressing emotional and subjective experiences. Van Gogh's brushstrokes are a defining " \
           "feature of his style, characterized by their boldness, energy, and expressive quality. He employed " \
           "thick impasto technique, layering paint on the canvas in a textured manner that added depth and " \
           "dimension to his works. His brushwork often follows a visible, directional pattern, imbuing his " \
           "paintings with a sense of movement and dynamism. Van Gogh's use of color is equally remarkable – he " \
           "employed vibrant and contrasting hues to evoke mood and emotion. His signature swirls, dynamic lines, " \
           "and thick, often jagged strokes create a sense of tension and intensity in his compositions. Overall, " \
           "van Gogh's painting style and brushstrokes are not only a visual delight but also a profound " \
           "expression of his inner emotional turmoil and artistic vision.  The images below show the thick impasto" \
           " technique and swirls that characterize his paintings."
st.markdown(content3)

col11, col21, col31, col41 = st.columns(4)

with col11:
    st.write("")
    st.image("images/close1.jpg", width=200)
    st.caption("Close-up of Sun")

with col21:
    st.write("")
    st.image("images/close2.jpg", width=200)
    st.caption("Close-up of Cypress Tree")

with col31:
    st.write("")
    st.image("images/close3.jpg", width=200)
    st.caption("Example of Brushstrokes")

with col41:
    st.write("")
    st.image("images/close4.jpg", width=200)
    st.caption("Example of Impasto")

st.header("")
st.subheader("Signature on Painting")

content4 = "Van Gogh did not sign all of his paintings but the paintings he did sign were signed 'Vincent'.  The " \
           "four images below show some examples of paintings that he signed along with the signature from my painting."
st.markdown(content4)

col12, col22, col32, col42 = st.columns(4)

with col12:
    st.write("")
    st.image("images/sig1.jpg", width=200)
    st.caption("Example of Van Gogh Signature #1")

with col22:
    st.write("")
    st.image("images/sig2.jpg", width=200)
    st.caption("Example of Van Gogh Signature #2")

with col32:
    st.write("")
    st.image("images/sig3.jpg", width=200)
    st.caption("Example of Van Gogh Signature #3")

with col42:
    st.write("")
    st.image("images/sig4.jpg", width=200)
    st.caption("Example of Van Gogh Signature #4")

col121, col222, col323= st.columns([1,2,1])

with col121:
    st.write("")


with col222:
    st.write("")
    st.image("images/mysig_resize.jpg", width=300)
    st.caption("Signature on My painting")

with col323:
    st.write("")

st.header("")
st.header("Back of Painting")
st.subheader("Comparison of Frame/Stretcher from 1885")

content3 = "The frame used in the painting is typical of a frame/stretcher from Europe in the late 19th century.  " \
           "The images below show a stretcher from 1885 on the left  and  my painting on the right."

st.markdown(content3)

col5, col6, col7, col8 = st.columns(4)

with col5:
    st.write("")


with col6:
    st.write("")
    st.image("images/back.jpg", width=300)
    st.caption("Back of Painting from 1885")

with col7:
    st.write("")
    st.image("images/back_my_resize.jpg", width=250)
    st.caption("Back of My Painting")

with col8:
    st.write("")

st.header("")
st.subheader("Stamp on Back of Painting")


content3 = "The stamp on the back of my painting has faded or been partially washed away but there is enough" \
           " to identyify it's orgin.  The stamp is from the art supply house Merlin et Denis in Paris.  " \
           "The rough translation of the stamp is: Color Factory - Canvas and Drawing Items - House of Merlin- " \
           "Paul Denis Succ = Paris - 19 Medicis Road 19.  Merlin et Denis changed it's name to Dubois Beaux Arts " \
           "sometime in the early 20th century and the location changed from 19 Rue de Medicis  to 20 Rue Soufflot." \
           "As shown below, Rue de medicis is about 10km from the van Gogh residence."

st.markdown(content3)

col9, col10, col11 = st.columns(3)

with col9:
    st.write("")
    st.image("images/stamp_denis.jpg", width=300)
    st.caption("Stamp from Merlin, Denis")

with col10:
    st.write("")
    st.image("images/mystamp.jpg", width=340)
    st.caption("Stamp on My Painting")

with col11:
    st.write("")
    st.image("images/ruedemedicis.jpg", width=340)
    st.caption("Rue de Medicis to van Gogh residence")




