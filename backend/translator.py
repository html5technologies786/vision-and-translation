from groq import Groq

# Directly initialize the client with the API key
client = Groq(api_key="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")

def translate_to_urdu(text):
    """Translate English text to Urdu using GroqCloud LLM."""
    try:
        completion = client.chat.completions.create(
            model="llama-3.2-11b-vision-preview",
            messages=[
                {"role": "user", "content": f"Translate the following text into Urdu:\n\n{text}"}
            ],
            temperature=0,  # Ensures precise translation
            max_tokens=1024,
            top_p=1,
            stream=False,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    test_text = "AI/ML ENGINEER specializes in developing high-performance machine learning models."
    urdu_translation = translate_to_urdu(test_text)
    print("English Text:", test_text)
    print("Urdu Translation:", urdu_translation)
