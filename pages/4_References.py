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

st.title("References")
st.divider()

para = "Code for streamlit project on Github: https://github.com/larsondg2000/vgstreamlit.git"

st.markdown("<h6 style='text-align: center; color: blue; font-style: italic;'>"
                f"{para}"
                "</h6>", unsafe_allow_html=True)
st.markdown("Van Gogh Museum [link](https://www.vangoghmuseum.nl/nl)")
st.markdown("The Vincent Van Gogh Gallery [link](http://www.vggallery.com/index.html)")
st.markdown("Kroller-Muller Museum [link](https://krollermuller.nl/)")
st.markdown("Dubois Beaux Arts Article [link](https://qz.com/quartzy/1178218/the-death-of-a-venerable-paris-art-"
            "store-shows-the-latin-quarters-days-are-numbered)")
st.markdown("National Gallery of Art Search [link](https://www.nga.gov/collection-search-result.html?"
            "sortOrder=DEFAULT&artobj_"
            "classification=painting&artobj_downloadable=Image_download_available&pageSize=90&pageNumber="
            "1&lastFacet=pageSize)")
st.markdown("The Van Gogh fakes scandal: the tally one year later [link](https://www.theartnewspaper.com/"
            "1998/07/01/the-van-gogh-fakes-scandal-the-tally-one-year-later)")
st.markdown("List of works by Vincent van Gogh [link](https://en.wikipedia.org/wiki/List_of_works_by_"
            "Vincent_van_Gogh#Paintings_(The_Hague-Drenthe))")
st.markdown("New Data Shows Why Van Gogh Changed His Color Palette [link](https://www.artnome.com/news/2018/11/26"
            "/new-data-shows-why-van-gogh-changed-his-color-palette-to-bright-yellow)")
st.markdown("Vincent van Gogh - The Letters [link](https://vangoghletters.org/vg/)")
st.markdown("The account book of Theo van Gogh and Jo van Gogh-Bonger [link](https://archive.org/details/the-account-"
            "book-of-theo-van-gogh-and-jo-van-gogh-bonger/page/146/mode/1up)")
st.markdown("Deep learning approaches to pattern extraction and recognition in paintings and drawings: an overview "
            "[link](https://link.springer.com/article/10.1007/s00521-021-05893-z)")
st.markdown("Compare the performance of the models in art classification [link](https://journals.plos.org/"
            "plosone/article?id=10.1371/journal.pone.0248414)")
st.markdown("Image Processing for Artist Identification "
            "[link](https://services.math.duke.edu/~ingrid/publications/Imag.pdf)")
st.markdown("Identifying Van Gogh’s paintings "
            "[link](https://medium.com/@preethi.madhusudhan/identifying-van-goghs-paintings-c610eeeda17f)")
st.markdown("Provenance Guide [link](https://www.ifar.org/Provenance_Guide.pdf)")
