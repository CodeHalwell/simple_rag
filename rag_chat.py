from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from openai import OpenAI
import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# Set up logging for debugging and monitoring.
import logging
log_level = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(level=getattr(logging, log_level.upper()))

st.set_page_config(page_title="Simple RAG Chat Bot", page_icon=":robot:", layout="wide")

# Get API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    st.error("OPENAI_API_KEY not found. Please check your .env file or environment variables.")
    st.stop()

# Use the OpenAI client for the API
client = OpenAI(api_key=openai_api_key)

# Create the vector database
def create_vector_db(pdf_path, chunk_size=1000, chunk_overlap=100):
    embedding_function = OpenAIEmbeddings(api_key=openai_api_key)
    docs = PyPDFLoader(pdf_path)
    docs = docs.load_and_split(text_splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap))
    db = Chroma.from_documents(docs, embedding_function)
    return db


# Create a Prompt Template instance
prompt_template = PromptTemplate.from_template(
    "You are a document assistant. Help me understand the following content: {content}. Please provide me with page numbers for further reading"
)

st.title("Simple RAG Chat Bot")

st.subheader("Ask questions about the document and get answers from the RAG model.")

# Example usage
pdf_path = os.getenv('PDF_PATH', 'pdfs/YOUR_PDF_FILE.pdf')
db = create_vector_db(pdf_path=pdf_path)  # Always recreate the db for this example

if prompt := st.chat_input("What is up?"):
    docs = db.similarity_search_with_relevance_scores(prompt, k=5)
    concatenated_texts = ' '.join([dict(doc[0])['page_content'] for doc in docs])
    formatted_prompt = prompt_template.format(content=concatenated_texts)

    messages = [{
        "role": "system",
        "content": "You are a document assistant."
    }, {
        "role": "user",
        "content": formatted_prompt
    }]

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Initiate streaming session
        try:
            stream = client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=messages,
                stream=True
            )

            # Write the response to the stream
            response = st.write_stream(stream)

            # Append the response to the messages
            messages.append({"role": "assistant", "content": response})

        except Exception as e:
            print(f"An error occurred: {e}")