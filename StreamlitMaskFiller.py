from MaskFiller import MaskFiller
import streamlit as st
from transformers.pipelines import PipelineException

st.title("Mask Filler")
st.write("This app uses a :blue[BERT] model to fill in the blank in a sentence.")

user_input = st.text_input("Enter a sentence with a blank:")
if user_input != "":
    st.write(f"Your sentence: {user_input}")
    st.write("Here are some possible words to fill in the blank:")
    maskFiller = MaskFiller()
    try:
        results = maskFiller.fill_mask(user_input, colorful=True)

        for result in results:
            st.write(result)
    except PipelineException:
        st.write(":red[An error occurred while processing your request.]")
        st.write("Example: :orange[Would you like to [MASK] with me?]")