import os
import time
from typing import Any

import streamlit as st
from dotenv import find_dotenv, load_dotenv
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from gtts import gTTS

from utils.custom import css_code

# LangChain (updated imports)
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import Ollama

load_dotenv(find_dotenv())

# Preload image captioning model (faster performance)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def progress_bar(amount_of_time: int) -> Any:
    progress_text = "Please wait, Generative models hard at work"
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(amount_of_time):
        time.sleep(0.04)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()


def generate_text_from_image(url: str) -> str:
    image = Image.open(url).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")
    output = model.generate(**inputs)
    generated_text: str = processor.decode(output[0], skip_special_tokens=True)

    print(f"IMAGE INPUT: {url}")
    print(f"GENERATED TEXT OUTPUT: {generated_text}")

    return generated_text


def generate_story_from_text(scenario: str) -> str:
    prompt_template: str = """
    You are a talented storyteller who can create a story from a simple narrative.
    Create a story using the following scenario; the story should be maximum 50 words long.

    CONTEXT: {scenario}
    STORY:
    """

    prompt: PromptTemplate = PromptTemplate(
        template=prompt_template,
        input_variables=["scenario"]
    )

    # LLaMA via Ollama (FREE)
    llm = Ollama(model="phi")

    story_llm: LLMChain = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True
    )

    generated_story: str = story_llm.predict(scenario=scenario)

    print(f"TEXT INPUT: {scenario}")
    print(f"GENERATED STORY OUTPUT: {generated_story}")

    return generated_story


def generate_speech_from_text(message: str) -> Any:
    tts = gTTS(text=message, lang='en')
    tts.save("generated_audio.mp3")


def main() -> None:
    st.set_page_config(page_title="Multimodal AI Image-to-Story Generator with Voice Narration", page_icon="🖼️")

    st.markdown(css_code, unsafe_allow_html=True)

    with st.sidebar:
        st.image("img/img.webp")
        st.write("---")
        st.write("AI App created by @ NUPUR")

    st.header("✨ AI StoryCraft – From Image to Imagination")
    uploaded_file: Any = st.file_uploader("Please choose a file to upload", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        bytes_data: Any = uploaded_file.getvalue()

        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)

        st.image(uploaded_file, caption="Uploaded Image", width="stretch")

        progress_bar(100)

        scenario: str = generate_text_from_image(uploaded_file.name)
        story: str = generate_story_from_text(scenario)
        generate_speech_from_text(story)

        with st.expander("Generated Image scenario"):
            st.write(scenario)

        with st.expander("Generated short story"):
            st.write(story)

        st.audio("generated_audio.mp3")


if __name__ == "__main__":
    main()