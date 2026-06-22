import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Communication Assistant",
    page_icon="🌍"
)

st.title("🌍 Language Communication Assistant")
st.write("Translate text between multiple languages.")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Kannada": "kn",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml"
}

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

text = st.text_area(
    "Enter Text",
    height=150
)

if st.button("Translate"):

    if source == target:
        st.error("Source and Target languages cannot be the same.")

    elif text.strip():

        try:
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

        except Exception as e:
            st.error(f"Translation failed: {e}")

    else:
        st.warning("Please enter text.")