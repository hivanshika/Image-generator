import streamlit as st

from huggingface_hub import InferenceClient

from dotenv import load_dotenv
import os

load_dotenv()

hf_token = os.getenv("HF_TOKEN")

client = InferenceClient(
    provider="hf-inference",
    api_key=hf_token,
)

st.set_page_config(
    page_title="Ridvig AI Image Generator",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 AI Prompt to Image Generator")

st.write("Welcome! This app converts a simple idea into a professional prompt and generates an image.")
user_prompt = st.text_area(
    "Enter your idea:",
    placeholder="Example: A poster for my juice shop's monsoon offer"
)
generate_button = st.button("Generate Professional Prompt")

if generate_button:

    if user_prompt.strip() == "":
        st.warning("⚠️ Please enter an idea before generating a prompt.")

    else:
        st.success("Generating your image...")
        prompt = f"""
        Create a professional image generation prompt for:
        {user_prompt}
        Include:
        - highly detailed
        - realistic
        - cinematic lighting
        - vibrant colors
        - high quality
        - 4k
        """
        image = client.text_to_image(
            prompt,
            model="black-forest-labs/FLUX.1-schnell"
            )
        st.subheader("🖼 Generated Image")
        st.image(image, use_container_width=True)