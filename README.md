# Advanced PDF Reader Chatbot with RAG and LLM

This project implements an advanced **PDF reader chatbot** using **Retrieval-Augmented Generation (RAG)** and **Large Language Models (LLM)**. The chatbot can read, analyze, and answer questions about PDF documents while supporting large context windows of up to **2600 tokens** for handling extensive document data.

## Key Features

- **PDF Document Upload**: Upload PDF files and extract text for contextual processing.
- **Intelligent Q&A**: Ask questions based on the PDF content, and the chatbot generates AI-based answers using RAG and LLM.
- **RAG Implementation**: Uses document retrieval techniques to enhance the LLM's ability to provide accurate responses based on the uploaded PDF.
- **Large Context Windows**: Optimized to handle up to 2600 tokens in a single context window.
- **Scalable Architecture**: Modular backend (Flask) and frontend (React) architecture, supporting future scalability.

## Project Structure

```plaintext
AdvancedPDFReaderChatbot/
│
├── backend/
│   ├── uploaded_pdfs/         # Uploaded PDFs for processing
│   ├── venv/                  # Virtual environment for Flask
│   ├── app.py                 # Backend server code (Flask)
│   └── requirements.txt       # Python dependencies
│
├── frontend/
│   ├── public/                # Static files for the frontend
│   ├── src/
│   │   ├── components/        # React components
│   │   │   └── ChatBot.js     # Chatbot component
│   │   └── index.js           # Entry point for React app
│   └── package.json           # Node dependencies
│
└── initialize_project.ps1      # PowerShell script to set up the project
```

## Prerequisites

- **Python 3.8+**
- **Node.js 14+**
- **npm (Node Package Manager)**
- **PowerShell (for running the setup script)**
- **Flask**
- **React**

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/AdvancedPDFReaderChatbot.git
cd AdvancedPDFReaderChatbot
```

Here is the README in markdown:

markdown
Copy code
# Advanced PDF Reader Chatbot with RAG and LLM

This project is an advanced **PDF reader chatbot** leveraging **Retrieval-Augmented Generation (RAG)** and **Large Language Models (LLM)** to process and analyze PDF documents. It provides an intuitive interface for uploading PDFs, asking context-related questions, and receiving accurate AI-generated answers. The chatbot is optimized for handling large context windows, up to **2600 tokens**, ensuring a comprehensive understanding of the document.

## Features

- **PDF Document Upload**: Users can upload any PDF document, and the system will extract the text for context analysis.
- **Advanced Question Answering**: Ask questions based on the uploaded PDF, and the system provides context-aware, detailed answers.
- **RAG (Retrieval-Augmented Generation)**: Combines document retrieval with OpenAI’s LLM for highly accurate, relevant answers.
- **Large Context Windows**: Supports context windows of up to 2600 tokens, making it suitable for lengthy or complex documents.
- **Scalable Architecture**: Uses Flask for the backend and React for the frontend, allowing for scalable and modular development.

## Prerequisites

- **Python 3.8+**
- **Node.js 14+**
- **npm (Node Package Manager)**
- **PowerShell (for running the setup script)**
- **Flask**
- **React**

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AdvancedPDFReaderChatbot.git
cd AdvancedPDFReaderChatbot
```
### 2. Run the Initialization Script
Open PowerShell as Administrator and run the setup script to create the project structure and install dependencies:

```bash
Set-ExecutionPolicy RemoteSigned
./initialize_project.ps1
```
### 3. Backend Setup (Flask)
- Navigate to the backend folder:
  
  ```bash
  cd backend
  ```
- Activate the virtual environment:
  
  ```bash
  # For Windows:
  .\venv\Scripts\Activate
  
  # For macOS/Linux:
  source venv/bin/activate
  ```
- Install the required Python dependencies:
  
  ```bash
  pip install -r requirements.txt
  ```
- Start the Flask server:
  
  ```bash
  python app.py
  ```
### 4. Frontend Setup (React)
- Navigate to the frontend folder:
  
  ```bash
  cd ../frontend
  ```
- Install the required Node modules:
  
  ```bash
  npm install
  ```
- Start the React development server:
  
  ```bash
  npm start
  ```
### 5. Access the Application
- Open your web browser and navigate to http://localhost:3000 to access the chatbot interface.
- Upload a PDF, ask questions based on its content, and receive answers from the chatbot.
### How It Works
- **Upload PDF**: The user uploads a PDF document via the frontend interface. The file is sent to the Flask backend, which extracts the text from the PDF.
- **Text Processing**: The extracted text is processed by the RAG system using FAISS for document retrieval and OpenAI's LLM for generating answers.
- **Ask Questions**: The user can submit a query related to the content of the uploaded PDF. The RAG system retrieves the most relevant parts of the text and generates a context-aware answer using the LLM.
### Technologies Used
- **Backend**: Flask, Python, PyPDF2, LangChain, FAISS, OpenAI API
- **Frontend**: React, JavaScript, Axios
- **RAG**: Retrieval-Augmented Generation for document analysis and LLM integration
- **LLM**: OpenAI's GPT-3.5-turbo with context windows up to 2600 tokens
