FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get -qq -y install tesseract-ocr && \
    apt-get -qq -y install libtesseract-dev

WORKDIR /ocr

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
