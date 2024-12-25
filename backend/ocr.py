import os
from mimetypes import guess_type
import base64
from groq import Groq

# loading API key securely from environment variables
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("API Key not found. Please set the GROQ_API_KEY environment variable.")


# Initializing Groq client
try:
    client = Groq(api_key=API_KEY)
    print("Groq client initialized successfully")
except Exception as e:
    raise RuntimeError(f"Failed to initialized Groq client: {e}")


from mimetypes import guess_type

def encode_image(image_path):
    """
    Encode an image file to Base64 format.
    
    Args:
        image_path (str): The file path to the image.
    
    Returns:
        str: Base64-encoded string of the image.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file '{image_path}' does not exist.")
    
    # Validate file format
    mime_type, _ = guess_type(image_path)
    if mime_type not in ["image/png", "image/jpeg"]:
        raise ValueError(f"Invalid file format. Expected a PNG or JPEG image, but got {mime_type}.")
    
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except Exception as e:
        raise ValueError(f"Failed to encode the image: {e}")

    
def extract_text_from_response(completion):
    """
    Extract and validate text from the Groq API response.

    Args:
        completion (object): The response object returned by the Groq API.

    Returns:
        str: Extracted text or a message indicating no text was found.
    """
    try:
        # Extract the content of the response
        extracted_text = completion.choices[0].message.content.strip()
        # Validate the content
        if not extracted_text or "No text present" in extracted_text:
            return "No text present in the image"
        return extracted_text
    except (IndexError, AttributeError) as e:
        # Handle unexpected response structure
        print(f"Response Error: {e}")
        return "Error: Invalid response from the API."
    

    
def process_image_with_groq(image_path):
    """
    Extract text content from an image using Groq's LLM vision API

    Args:
        image_path (str): The file path to the image

    Returns:
        str: Extracted text or a message indicating no text found
    """
    try:
        # Encoding the image to Base64
        base64_image = encode_image(image_path)

        # Sending API request for the text extraction to LLAMA vision model
        completion = client.chat.completions.create(
            model="llama-3.2-11b-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text", "text":
                            "Extract **only the text** that is present in the image."
                            "Do not describe the image or object in the image. "
                            "If no text is found, respond with 'No text present in the image.'"
                        },
                        {"type": "image_url",
                         "image_url": {"url": f"data:image/png;base64,{base64_image}"}
                        }
                    ]
                }
            ],
            temperature=0,
            max_tokens=1024,
            top_p=1
        )

        # Automatically handle response extraction and validation
        return extract_text_from_response(completion)

    except FileNotFoundError as fe:
        print(f"File Error: {fe}")
        return "Error: File not found or invalid file path."
    except ValueError as ve:
        print(f"Value Error: {ve}")
        return "Error: Invalid file format or unsupported operation."
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return "Error processing the image."
    

# Example useage with local image file
if __name__ == "__main__":
    image_path = "G:/Projects/Image-To-Urdu-Translator/backend/background.png"
    try:
        result = process_image_with_groq(image_path)
        print("Extracted Text:", result)
    except Exception as e:
        print(f"Processing Failed: {e}")
