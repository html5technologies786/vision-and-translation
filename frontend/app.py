import streamlit as st
import requests
from streamlit_extras.add_vertical_space import add_vertical_space

# Backend API URL
BACKEND_API_URL = "http://127.0.0.1:5000/upload"

# Set the page configuration
st.set_page_config(page_title="Picture Text to Urdu: AI-Powered Translator", page_icon="🌐", layout="wide")

# Define the navigation state in session_state
if "page" not in st.session_state:
    st.session_state.page = "greeting"  # Default to the greeting page

# Function to navigate between pages
def navigate_to(page_name):
    st.session_state.page = page_name

# Greeting Page
if st.session_state.page == "greeting":
    st.markdown(
        """
        <div style="background-color: #f0f8ff; color: #333333; padding: 15px; border-radius: 10px; text-align: center;">
            <h2>Hi! I'm your AI-Powered Translator Bot 🤖</h2>
            <p>Upload an image, and I'll extract the text and translate it into Urdu for you!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Let's Get Started!"):
        navigate_to("functionality")

# Functionality Page
if st.session_state.page == "functionality":
    # Sidebar
    with st.sidebar:
        st.title("📜 Picture Text to Urdu: AI-Powered Translator")
        st.write("Upload an image, extract English text from it, and get its Urdu translation.")
        st.write("### Features:")
        st.write("- Extracts text from images using **LLAMA Vision Model**.")
        st.write("- Translates the extracted text into **Urdu** accurately.")
        st.write("### Why LLAMA Vision Model?")
        st.write(
            """
            The LLAMA Vision Model is a state-of-the-art machine learning model that excels in processing 
            and understanding visual data. It is specifically designed to:
            - Extract text from complex images with high precision.
            - Handle diverse fonts, languages, and layouts effectively.
            """
        )
        add_vertical_space(2)
        st.write("Developed by **Muavia Shakeel**.")

    # Main App
    st.title("🌐 Picture Text to Urdu: AI-Powered Translator")
    st.write("Upload an image below, and we'll extract the English text and translate it to Urdu.")

    # File Upload
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], help="Accepted formats: PNG, JPG, JPEG")

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        st.success("File uploaded successfully! Click the 'Process Image' button below.")

        # Process the image when the user clicks the button
        if st.button("Process Image"):
            with st.spinner("Processing the image..."):
                # Send the image to the backend
                response = requests.post(BACKEND_API_URL, files={"image": uploaded_file})

                # Check the response from the backend
                if response.status_code == 200:
                    result = response.json()
                    extracted_text = result.get("extracted_text", "No text extracted")
                    urdu_translation = result.get("urdu_translation", "No translation available")

                    # Display results in styled containers
                    st.write("---")
                    st.subheader("Extracted Text:")
                    st.markdown(
                        f"""
                        <div style="background-color: #ffffff; color: #000000; padding: 10px; border-radius: 5px; border: 1px solid #cccccc;">
                            {extracted_text}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    st.subheader("Urdu Translation:")
                    st.markdown(
                        f"""
                        <div style="background-color: #f0f8ff; color: #000000; padding: 10px; border-radius: 5px; border: 1px solid #cccccc;">
                            {urdu_translation}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                else:
                    st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    else:
        st.info("Please upload an image to get started.")
