import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Communication Assistant")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml"
}

source = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target = st.selectbox(
    "Target Language",
    list(languages.keys()),
    index=1
)

text = st.text_area("Enter Text")

if st.button("Translate"):

    if text.strip():

        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation Complete")

        st.text_area(
            "Translated Text",
            translated,
            height=150
        )

    else:
        st.warning("Please enter text")