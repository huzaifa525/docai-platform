import os
from werkzeug.utils import secure_filename
from app.utils.vector_store import VectorStore
from app.utils.llm_client import LLMClient
from app.utils.web_search import WebSearchTool
from app.utils.document_processor import DocumentProcessor

class DocumentService:
    def __init__(self):
        self.vector_store = VectorStore()
        self.doc_processor = DocumentProcessor()
        self.upload_folder = 'uploads'
        os.makedirs(self.upload_folder, exist_ok=True)

    def process_document(self, file):
        try:
            filename = secure_filename(file.filename)
            filepath = os.path.join(self.upload_folder, filename)
            file.save(filepath)

            text = self.doc_processor.extract_text(filepath)
            if not text:
                return False, "Failed to extract text from document"

            success = self.vector_store.add_document(text)
            return success, "Document processed successfully"

        except Exception as e:
            return False, str(e)
        finally:
            if os.path.exists(filepath):
                os.remove(filepath)

class QAService:
    def __init__(self):
        self.vector_store = VectorStore()
        self.llm_client = LLMClient()
        self.web_search = WebSearchTool()

    def process_query(self, question):
        try:
            context = self.vector_store.search(question)
            if not context:
                context = self.web_search.search(question)

            prompt = self._create_prompt(question, context)
            response = self.llm_client.generate_response(prompt)
            return response, len(response.split())

        except Exception as e:
            return f"Error: {str(e)}", 0

    def _create_prompt(self, question, context):
        return f"""Based on the following context, answer the question.

Context: {context}

Question: {question}

Answer:"""