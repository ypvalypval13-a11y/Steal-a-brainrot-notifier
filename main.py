import time
import mss
from PIL import Image
import pytesseract
import tempfile
import os
import pyttsx3
import json5

# Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"


def speak(text: str) -> None:
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    try:
        engine.stop()
    except Exception:
        pass



# Load keywords
with open("keywords.txt", "r", encoding="utf-8") as f:
    keywords = [line.strip() for line in f if line.strip()]

# Load config
with open("config.json5", "r", encoding="utf-8") as f:
    config = json5.load(f)

screen = config["screen"]
interval = config["interval"]


