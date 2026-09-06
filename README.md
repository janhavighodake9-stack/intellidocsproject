# 📄 IntelliDocs

## Intelligent Document Processing and Question Answering System

IntelliDocs is a web-based document processing application developed using Python and Flask.

The system allows users to upload documents in PDF, DOCX, and TXT formats. After uploading a document, IntelliDocs extracts the text and allows users to ask questions related to the uploaded document.

## Features

- Upload PDF documents
- Upload DOCX documents
- Upload TXT documents
- File type validation
- Document storage
- PDF text extraction
- DOCX text extraction
- TXT text extraction
- Document-based question answering
- Simple and user-friendly web interface
- Modular Flask architecture


##  Technologies Used

- Python
- Flask
- PyMuPDF
- Python-docx
- HTML
- CSS
- Werkzeug

##  Project Structure

```text
Intellidocs/
│
├── app.py
│
├── routes/
│   ├── __init__.py
│   └── main_routes.py
│
├── controllers/
│   ├── __init__.py
│   └── home_controller.py
│
├── services/
│   ├── __init__.py
│   ├── document_service.py
│   └── qa_service.py
│
├── models/
│   └── __init__.py
│
├── utils/
│   └── __init__.py
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── .gitignore
└── README.md