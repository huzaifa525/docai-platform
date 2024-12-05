import fitz
import pytesseract
from PIL import Image

class DocumentProcessor:
    def __init__(self):
        self.needs_ocr = False

    def extract_text(self, filepath):
        try:
            doc = fitz.open(filepath)
            text = ""
            
            for page in doc:
                page_text = page.get_text()
                if not page_text.strip():
                    self.needs_ocr = True
                    pix = page.get_pixmap()
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    page_text = pytesseract.image_to_string(img)
                text += page_text + '\n'
            
            return text.strip()
        except Exception as e:
            raise Exception(f"Failed to process document: {str(e)}")