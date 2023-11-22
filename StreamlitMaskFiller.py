from MaskFiller import MaskFiller
import streamlit as st

st.title("Mask Filler")
st.write("This app uses a :blue[BERT] model to fill in the blank in a sentence.")
# use user input to fill in the blank
user_input = st.text_input("Enter a sentence with a blank:")
if user_input != "":
    st.write(f"Your sentence: {user_input}")
    st.write("Here are some possible words to fill in the blank:")
    maskFiller = MaskFiller()
    results = maskFiller.fill_mask(user_input, colorful=True)

    # Pretty print the results
    for result in results:
        st.write(result)
