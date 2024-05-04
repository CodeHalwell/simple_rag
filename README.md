# Simple RAG Chat Bot

This is a simple implementation of a RAG (Retrieval-Augmented Generation) chat bot using the OpenAI API, Langchain, and Streamlit. The bot is designed to answer questions about a specific document.

## Requirements

This project requires Python 3.6 or later. The required Python libraries are listed in the `requirements.txt` file and can be installed using pip:

```bash
pip install -r requirements.txt
```

## Usage

To run the chat bot, execute the `rag_chat.py` script:

```bash
streamlit run rag_chat.py
```

This will start a Streamlit server and open a new tab in your default web browser with the chat bot interface.

## How it works

The chat bot works by creating a vector database from a given PDF document. It splits the document into chunks and computes embeddings for each chunk using the OpenAI API. These embeddings are stored in a Chroma database, which allows for efficient similarity search.

When a user asks a question, the bot performs a similarity search in the database to find the most relevant chunks of text. It then sends a prompt to the OpenAI API, which generates a response.

The bot also uses a prompt template to format the prompts sent to the OpenAI API. The template can be customized to change the role of the bot and the type of responses it generates.

## Configuration

The OpenAI API key is loaded from a file named `open_ai_key` in the same directory as the script. You need to create this file and write your OpenAI API key in it.

The path to the PDF document is specified in the `create_vector_db` function. You need to replace `'pdfs/YOUR_PDF_FILE.pdf'` with the path to your document.

The chunk size and overlap for splitting the document into chunks can be adjusted by changing the `chunk_size` and `chunk_overlap` parameters in the `create_vector_db` function.

The number of most relevant chunks to consider when answering a question can be adjusted by changing the `k` parameter in the `similarity_search_with_relevance_scores` method.

## Error handling

If an error occurs while generating a response, the bot prints the error message and continues running. You can see the error messages in the terminal where you started the script.

