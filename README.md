# vision-and-translation

---

# **Picture Text to Urdu: AI-Powered Translator**

An AI-powered application to extract text from images using the **LLAMA Vision Model** and translate the extracted text into Urdu. The project uses a combination of **Flask** for the backend and **Streamlit** for the frontend to deliver a seamless user experience.

---

## **Features**
- **OCR (Optical Character Recognition):**
  - Extract text from images, including complex layouts, diverse fonts, and different languages.
  - Powered by the advanced **LLAMA Vision Model** for high precision and accuracy.

- **Text Translation:**
  - Translate the extracted English text into Urdu with high accuracy.

- **User-Friendly Interface:**
  - Simple and interactive web application built using **Streamlit**.
  - Drag-and-drop functionality for uploading images.

- **Lightweight and Fast:**
  - Combines Flask and Streamlit for efficient backend and frontend communication.

---

## **Tech Stack**
### **Frontend**
- **Streamlit**: A lightweight framework for building interactive web apps in Python.
- **HTML/CSS**: For additional customization of the Streamlit app.

### **Backend**
- **Flask**: A Python-based lightweight backend framework.
- **LLAMA Vision Model**: A state-of-the-art machine learning model for extracting text from images.
- **Google Translate API** (or equivalent): For Urdu translation.

### **Programming Language**
- Python

---

## **Project Structure**
```
vision-and-translation/
├── backend/
│   ├── backend.py            # Main Flask app
│   ├── ocr.py                # OCR functions using LLAMA Vision Model
│   ├── translator.py         # Text translation logic
│   ├── requirements.txt      # Backend dependencies
├── frontend/
│   ├── app.py                # Streamlit app
│   ├── requirements.txt      # Frontend dependencies
├── README.md                 # Project documentation
```

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/html5technologies786/vision-and-translation.git
cd vision-and-translation
```

### **2. Backend Setup**
1. Navigate to the backend folder:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # For Linux/Mac
   venv\Scripts\activate       # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python backend.py
   ```

### **3. Frontend Setup**
1. Open a new terminal and navigate to the frontend folder:
   ```bash
   cd frontend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # For Linux/Mac
   venv\Scripts\activate       # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## **Usage**
1. Open the frontend Streamlit app in your browser (e.g., `http://localhost:8501`).
2. Upload an image containing text.
3. Click the "Process Image" button to:
   - Extract text from the image.
   - Get its Urdu translation displayed in real-time.

---

## **Why Use LLAMA Vision Model?**
The **LLAMA Vision Model** is a cutting-edge machine learning model designed for processing and understanding visual data. It provides:
- High accuracy in extracting text from complex images.
- Robust performance on diverse fonts, languages, and layouts.

---

## **Contributing**
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Credits**
Developed by **Muavia Shakeel**.


