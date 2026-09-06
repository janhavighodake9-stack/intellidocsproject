import os
import pymupdf
from werkzeug.utils import secure_filename
from docx import Document


ALLOWED_EXTENSIONS = {"pdf", "docx", "txt"}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


def save_document(file):
    if file is None or file.filename == "":
        return False, "No file selected."

    if not allowed_file(file.filename):
        return False, "Only PDF, DOCX and TXT files are allowed."

    upload_folder = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "uploads"
    )

    os.makedirs(upload_folder, exist_ok=True)

    filename = secure_filename(file.filename)
    file_path = os.path.join(upload_folder, filename)

    file.save(file_path)

    return True, f"File '{filename}' uploaded successfully."


def extract_text(file_path):
    extension = file_path.rsplit(".", 1)[1].lower()

    # TXT extraction
    if extension == "txt":
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()

        except Exception as e:
            return f"Unable to read this TXT file: {str(e)}"

    # PDF extraction
    elif extension == "pdf":
        try:
            pdf = pymupdf.open(file_path)

            text = ""

            for page in pdf:
                text += page.get_text() + "\n"

            pdf.close()

            if text.strip():
                return text

            return "No readable text found in this PDF."

        except Exception as e:
            return f"Unable to read this PDF: {str(e)}"

    # DOCX extraction
    elif extension == "docx":
        try:
            document = Document(file_path)

            text = ""

            for paragraph in document.paragraphs:
                text += paragraph.text + "\n"

            if text.strip():
                return text

            return "No readable text found in this DOCX file."

        except Exception as e:
            return f"Unable to read this DOCX file: {str(e)}"

    return "Unsupported file type."