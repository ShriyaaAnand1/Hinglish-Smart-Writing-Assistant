
import streamlit as st

from modules.transliteration import transliterate
from modules.improvement import improve_sentence
from modules.translation import translate_to_english

st.set_page_config(
    page_title="Hinglish Smart Writing Assistant",
    page_icon="✍️",
    layout="centered"
)

LANGUAGES = {
    "Hindi": {
        "xlit": "hi",
        "indictrans": "hin_Deva"
    },
    "Kannada": {
        "xlit": "kn",
        "indictrans": "kan_Knda"
    },
    "Tamil": {
        "xlit": "ta",
        "indictrans": "tam_Taml"
    }
}

st.title("Hinglish Smart Writing Assistant")

st.write(
    "Convert Hinglish text written using English letters "
    "into Indian-language scripts."
)

language_name = st.selectbox(
    "Choose output language",
    list(LANGUAGES.keys())
)

input_text = st.text_area(
    "Enter Hinglish text",
    placeholder="Example: Mujhe kal college jaana hai",
    height=120
)

col1, col2 = st.columns(2)

with col1:
    use_improvement = st.checkbox(
        "Improve sentence (Param1)"
    )

with col2:
    use_translation = st.checkbox(
        "Translate to English (IndicTrans2)"
    )

if st.button("Convert Text", type="primary",
             use_container_width=True):

    if not input_text.strip():
        st.warning("Please enter some text.")

    else:
        language_codes = LANGUAGES[language_name]

        try:
            with st.spinner("Converting text..."):

                converted_text = transliterate(
                    input_text.strip(),
                    language_codes["xlit"]
                )

            st.subheader("Transliterated Output")
            st.success(converted_text)

            final_text = converted_text

            if use_improvement:

                try:
                    with st.spinner("Improving sentence..."):

                        final_text = improve_sentence(
                            converted_text,
                            language_name
                        )

                    st.subheader("Improved Sentence")
                    st.info(final_text)

                except Exception as e:
                    st.error(
                        f"Sentence improvement failed: {e}"
                    )

            if use_translation:

                try:
                    with st.spinner("Translating..."):

                        english_text = translate_to_english(
                            final_text,
                            language_codes["indictrans"]
                        )

                    st.subheader("English Translation")
                    st.success(english_text)

                except Exception as e:
                    st.error(
                        f"Translation failed: {e}"
                    )

        except Exception as e:
            st.error(f"Transliteration failed: {e}")

st.divider()

st.caption(
    "AI-powered Indian language writing assistant."
)
