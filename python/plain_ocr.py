import sys
import easyocr
import json
import logging
import numpy as np

# Disable easyocr logging messages
logging.getLogger("easyocr.easyocr").setLevel(logging.ERROR)

def read_image(image_path):
    try:
        # Initialize reader with English and Indonesian languages
        reader = easyocr.Reader(['en', 'id'], verbose=False, download_enabled=False)

        # Read text from image
        result = reader.readtext(image_path)

        # Extract text with confidence and positions
        texts = [item[1] for item in result]
        plain_text = ' '.join(texts)

        # Print as JSON string for proper parsing in Node.js
        print(json.dumps({
            "success": True,
            "data": plain_text
        }, ensure_ascii=False))

    except Exception as e:
        print(json.dumps({
            "success": False,
            "error": str(e)
        }, ensure_ascii=False))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        read_image(image_path)
    else:
        print(json.dumps({
            "success": False,
            "error": "No image path provided"
        }, ensure_ascii=False))
