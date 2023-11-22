from MaskFiller import MaskFiller

import streamlit as st
import tensorflow

st.title("Mask Filler")
st.write("This app uses a :blue[BERT] model to fill in the blank in a sentence.")
# use user input to fill in the blank
user_input = st.text_input("Enter a sentence with a blank:")
if user_input != "":
    st.write(f"Your sentence: {user_input}")
    st.write("Here are some possible words to fill in the blank:")
    maskFiller = MaskFiller()
    try:
        results = maskFiller.fill_mask(user_input, colorful=True)

        # Pretty print the results
        for result in results:
            st.write(result)
    except:
        st.write(":red[Input error.]")
        st.write("Example: :orange[Would you like to [MASK] with me?]")
