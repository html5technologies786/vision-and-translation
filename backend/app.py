from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from ocr import process_image_with_groq
from translator import translate_to_urdu

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_image():
    """Endpoint to upload an image, extract text, and translate it into Urdu."""
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Process OCR
    extracted_text = process_image_with_groq(filepath)
    print("Extracted Text:", extracted_text)  # Debugging step

    if not extracted_text:
        return jsonify({"error": "Failed to process the image for text extraction"}), 500

    # Translate to Urdu
    urdu_translation = translate_to_urdu(extracted_text)
    print("Urdu Translation:", urdu_translation)  # Debugging step

    if not urdu_translation:
        return jsonify({"error": "Failed to translate the extracted text"}), 500

    # Return both extracted text and Urdu translation
    return jsonify({
        "extracted_text": extracted_text,
        "urdu_translation": urdu_translation
    }), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
