from flask import Blueprint, request, render_template
from services.document_services import save_document, extract_text
from services.qa_service import answer_question
import os


main_routes = Blueprint("main_routes", __name__)

# Store extracted document text temporarily
document_text = ""


@main_routes.route("/")
def home():
    return render_template("index.html")


@main_routes.route("/upload", methods=["POST"])
def upload():
    global document_text

    file = request.files.get("document")

    success, message = save_document(file)

    if not success:
        return f"""
        <h2>Upload Failed</h2>
        <p>{message}</p>
        <a href="/">Try again</a>
        """

    filename = file.filename

    upload_folder = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "uploads"
    )

    file_path = os.path.join(upload_folder, filename)

    document_text = extract_text(file_path)

    return f"""
    <html>
    <head>
        <title>Document Uploaded - IntelliDocs</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                margin: 0;
                padding: 0;
            }}

            .container {{
                width: 80%;
                max-width: 900px;
                margin: 50px auto;
                background: white;
                padding: 35px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }}

            h1 {{
                color: #222;
            }}

            h2 {{
                color: #2563eb;
            }}

            .success {{
                color: green;
                font-weight: bold;
            }}

            textarea {{
                width: 100%;
                height: 100px;
                padding: 10px;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 6px;
                box-sizing: border-box;
            }}

            button {{
                background: #2563eb;
                color: white;
                border: none;
                padding: 12px 25px;
                border-radius: 6px;
                cursor: pointer;
                font-size: 16px;
                margin-top: 10px;
            }}

            button:hover {{
                background: #1d4ed8;
            }}

            .document-text {{
                background: #f8fafc;
                padding: 20px;
                border-radius: 8px;
                margin-top: 20px;
                max-height: 300px;
                overflow-y: auto;
                white-space: pre-wrap;
            }}

            a {{
                display: inline-block;
                margin-top: 20px;
                color: #2563eb;
                text-decoration: none;
            }}
        </style>
    </head>

    <body>

    <div class="container">

        <h1>📄 IntelliDocs</h1>

        <p class="success">
            ✓ {message}
        </p>

        <h2>Ask a Question</h2>

        <form action="/ask" method="POST">

            <textarea
                name="question"
                placeholder="Ask something about your document..."
                required
            ></textarea>

            <br>

            <button type="submit">
                Ask Question
            </button>

        </form>

        <h2>Extracted Text</h2>

        <div class="document-text">
            {document_text}
        </div>

        <a href="/">
            ← Upload another document
        </a>

    </div>

    </body>
    </html>
    """


@main_routes.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question")

    answer = answer_question(document_text, question)

    return f"""
    <html>
    <head>
        <title>Answer - IntelliDocs</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                margin: 0;
                padding: 0;
            }}

            .container {{
                width: 80%;
                max-width: 800px;
                margin: 60px auto;
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }}

            h1 {{
                text-align: center;
            }}

            h2 {{
                color: #2563eb;
            }}

            .question {{
                background: #f1f5f9;
                padding: 15px;
                border-radius: 8px;
            }}

            .answer {{
                background: #ecfdf5;
                padding: 20px;
                border-radius: 8px;
                line-height: 1.6;
            }}

            a {{
                display: inline-block;
                margin-top: 20px;
                color: #2563eb;
                text-decoration: none;
            }}
        </style>
    </head>

    <body>

    <div class="container">

        <h1>📄 IntelliDocs</h1>

        <h2>Your Question</h2>

        <div class="question">
            {question}
        </div>

        <h2>Answer</h2>

        <div class="answer">
            {answer}
        </div>

        <a href="/">
            ← Upload another document
        </a>

    </div>

    </body>
    </html>
    """