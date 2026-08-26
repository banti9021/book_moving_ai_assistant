import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)

project_name = "moving-ai-agent"

list_of_files = [

    # Backend
    "backend/main.py",
    "backend/database.py",
    "backend/chatbot.py",
    "backend/quote.py",
    "backend/email.py",

    # Frontend
    "frontend/index.html",
    "frontend/style.css",
    "frontend/script.js",

    # Data
    "data/pricing.txt",
    "data/faq.txt",

    # Root files
    "requirements.txt",
    ".env",
    "README.md"
]

for filepath in list_of_files:

    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

        logging.info(
            f"Creating directory: {filedir} for the file: {filename}"
        )

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        with open(filepath, "w") as f:
            pass

        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")