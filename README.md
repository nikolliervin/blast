# Blast OCR API

Blast OCR is a Python API that provides a simple endpoint for optical character recognition (OCR) using Tesseract. The API takes an image as input, processes it using Tesseract, and returns the extracted text from the image.

## Getting Started

Follow the steps below to set up and run the Blast OCR API on your local machine.

### Prerequisites

Make sure you have the following prerequisites installed:

- Python 3.10
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nikolliervin/blast-ocr-api.git

### Usage

1. Run the API (First Instance)
   ```bash
   uvicorn main:app --reload
2. Make a HTTP POST Request to:
   ```bash 
   /recognize
  
3. Curl example:
   ```bash
   curl --location 'http://127.0.0.1:8000/recognize' \ --form 'image=@"C:\\Users\\...\\Desktop\\fastapi.png"'
4. API Response
   ```bash
   {"text": "FastAPI."}
