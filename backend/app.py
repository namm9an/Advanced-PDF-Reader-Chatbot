from flask import Flask, request, jsonify
import PyPDF2
import os
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain import RetrievalQA, LLMChain
from langchain.chat_models import ChatOpenAI

app = Flask(__name__)

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Create retriever with FAISS
def create_retriever(text):
    loader = TextLoader.from_text(text)
    documents = loader.load()
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

# Advanced RAG integration
def create_rag_system(retriever):
    chat_model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, max_tokens=2600)
    qa_system = RetrievalQA(llm=chat_model, retriever=retriever)
    return qa_system

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    pdf_path = os.path.join("uploaded_pdfs", file.filename)
    file.save(pdf_path)

    text = extract_text_from_pdf(pdf_path)
    retriever = create_retriever(text)

    # Save the retriever globally for future use
    global qa_system
    qa_system = create_rag_system(retriever)

    return jsonify({'message': 'PDF uploaded and processed successfully'})

@app.route('/ask_question', methods=['POST'])
def ask_question():
    if 'qa_system' not in globals():
        return jsonify({'error': 'Upload a PDF first'}), 400

    data = request.get_json()
    query = data.get('query')

    # Use RAG model to answer the query
    response = qa_system.run(query)

    return jsonify({'answer': response})

if __name__ == '__main__':
    if not os.path.exists('uploaded_pdfs'):
        os.makedirs('uploaded_pdfs')
    app.run(debug=True)
