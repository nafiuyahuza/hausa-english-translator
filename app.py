import streamlit as st
from difflib import get_close_matches

# Basic dictionary
translation_dict = {
    "hello": "sannu",
    "goodbye": "sai anjima",
    "how are you": "yaya kake",
    "thank you": "na gode",
    "yes": "eh",
    "no": "a'a",
    "please": "don Allah",
    "what is your name": "menene sunanka",
    "my name is": "sunana",
    "i am fine": "lafiya lau",
}

# Reverse dictionary for Hausa to English
reverse_dict = {v: k for k, v in translation_dict.items()}

# Translator logic
def translate(text, lang):
    text = text.lower().strip()
    if lang == "English to Hausa":
        if text in translation_dict:
            return translation_dict[text]
        else:
            suggestion = get_close_matches(text, translation_dict.keys(), n=1)
            if suggestion:
                return f"Did you mean: '{suggestion[0]}'? -> {translation_dict[suggestion[0]]}"
            else:
                return "Translation not found."
    else:
        if text in reverse_dict:
            return reverse_dict[text]
        else:
            suggestion = get_close_matches(text, reverse_dict.keys(), n=1)
            if suggestion:
                return f"Did you mean: '{suggestion[0]}'? -> {reverse_dict[suggestion[0]]}"
            else:
                return "Translation not found."

# Streamlit UI
st.title("Hausa-English Smart Translator")
st.write("Translate between English and Hausa with AI-assisted suggestions.")

language = st.selectbox("Choose translation direction", ["English to Hausa", "Hausa to English"])
user_input = st.text_input("Enter text to translate")

if st.button("Translate"):
    if user_input:
        result = translate(user_input, language)
        st.success(result)
    else:
        st.warning("Please enter some text.")
