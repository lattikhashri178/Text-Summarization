
import streamlit as st
from transformers import pipeline

# Page configuration
st.set_page_config(
    page_title="Text Summarization App",
    page_icon="📝",
    layout="centered"
)

# App title
st.title("📝 Text Summarization Using Hugging Face")
st.write(
    "Enter a long paragraph or article to generate "
    "a short summary using AI."
)

# Load the pretrained model once
@st.cache_resource
def load_summarizer():
    return pipeline(
        task="summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )

# User input
input_text = st.text_area(
    "Enter your text:",
    height=250,
    placeholder="Paste your article or paragraph here..."
)

# Summary length selection
summary_length = st.selectbox(
    "Choose summary length:",
    ["Short", "Medium", "Long"],
    index=1
)

# Set summary length
length_options = {
    "Short": {"min_length": 20, "max_length": 60},
    "Medium": {"min_length": 40, "max_length": 100},
    "Long": {"min_length": 60, "max_length": 130}
}

# Generate summary
if st.button("Generate Summary", type="primary"):

    if not input_text.strip():
        st.warning("Please enter some text.")

    elif len(input_text.split()) < 30:
        st.warning(
            "Please enter at least 30 words "
            "to generate a meaningful summary."
        )

    else:
        try:
            with st.spinner(
                "Loading the model and generating summary..."
            ):
                summarizer = load_summarizer()

                settings = length_options[summary_length]

                result = summarizer(
                    input_text,
                    min_length=settings["min_length"],
                    max_length=settings["max_length"],
                    do_sample=False,
                    truncation=True
                )

                summary = result[0]["summary_text"]

            # Display summary
            st.subheader("📌 Generated Summary")
            st.success(summary)

            # Display statistics
            original_words = len(input_text.split())
            summary_words = len(summary.split())

            st.write(f"Original words: {original_words}")
            st.write(f"Summary words: {summary_words}")

            # Download summary
            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

        except Exception as error:
            st.error(f"An error occurred: {error}")
            st.info(
                "Check your internet connection and installed "
                "library versions. The model downloads on first use."
            )
