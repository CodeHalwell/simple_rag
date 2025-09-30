# Simple RAG Chat Bot

This is a simple implementation of a RAG (Retrieval-Augmented Generation) chat bot using the OpenAI API, Langchain, and Streamlit. The bot is designed to answer questions about a specific document.

## Prerequisites

- Python 3.8 or later
- [UV package manager](https://github.com/astral-sh/uv) (recommended) or pip

## Installation

### Using UV (Recommended)

UV provides streamlined package management, simplified project setup, and consistency across development environments.

1. **Install UV** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/CodeHalwell/simple_rag.git
   cd simple_rag
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file and add your OpenAI API key and PDF path.

5. **Validate your setup**:
   ```bash
   uv run python validate_setup.py
   ```

### Using pip (Alternative)

If you prefer to use pip, you can install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

You can also validate your setup with:
```bash
python validate_setup.py
```

## Configuration

Create a `.env` file in the project root with the following variables:

```env
# Required: Your OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here

# Optional: Path to your PDF document (default: pdfs/YOUR_PDF_FILE.pdf)
PDF_PATH=pdfs/your_document.pdf

# Optional: Logging level (default: INFO)
LOG_LEVEL=INFO
```

You can use the provided `.env.example` as a template.

## Usage

### With UV

```bash
uv run streamlit run rag_chat.py
```

### With pip

```bash
streamlit run rag_chat.py
```

This will start a Streamlit server and open a new tab in your default web browser with the chat bot interface.

## How it works

The chat bot works by creating a vector database from a given PDF document. It splits the document into chunks and computes embeddings for each chunk using the OpenAI API. These embeddings are stored in a Chroma database, which allows for efficient similarity search.

When a user asks a question, the bot performs a similarity search in the database to find the most relevant chunks of text. It then sends a prompt to the OpenAI API, which generates a response.

The bot also uses a prompt template to format the prompts sent to the OpenAI API. The template can be customized to change the role of the bot and the type of responses it generates.

## Advanced Configuration

The chunk size and overlap for splitting the document into chunks can be adjusted by changing the `chunk_size` and `chunk_overlap` parameters in the `create_vector_db` function.

The number of most relevant chunks to consider when answering a question can be adjusted by changing the `k` parameter in the `similarity_search_with_relevance_scores` method.

## Development

### Using UV for Development

For development work, you can install additional development dependencies:

```bash
uv sync --dev
```

This includes tools like pytest, black, and flake8 for testing and code formatting.

## Error handling

If an error occurs while generating a response, the bot prints the error message and continues running. You can see the error messages in the terminal where you started the script.

## Recent Updates

### LangChain 1.0 Alpha Upgrade (December 2024)

The project has been updated to use LangChain 1.0 alpha release:

- **LangChain**: Updated to 1.0.0a10 (alpha release)
- **LangChain Core**: Updated to 0.3.76+
- **LangChain OpenAI**: Updated to 0.3.33+
- **LangChain Community**: Updated to 0.3.30+
- **LangChain Chroma**: Updated to 0.2.6+
- **LangChain Text Splitters**: Updated to 0.3.11+
- **OpenAI**: Updated to 1.99.0+

**What's in LangChain 1.0 Alpha:**
- LangChain 1.0 marks the first major version with a focus on stability and production readiness
- Improved API consistency across all LangChain packages
- Enhanced type safety and error handling
- Better integration patterns with external APIs and services

**Breaking Changes Addressed:**
- Import statements updated for LangChain 1.0 compatibility
- Document loaders now use `langchain_community`
- Text splitters now use `langchain_text_splitters`
- Prompt template usage simplified

**OpenAI API Integration:**
- Embeddings: Configured via `OpenAIEmbeddings` with API key
- Chat: Configured via `OpenAI` client with streaming support
- Model: Uses `gpt-3.5-turbo` for chat completions

**Note:** LangChain 1.0 is currently in alpha release. The stable 1.0 release is expected soon. Use with caution in production environments.

## Migration from Previous Setup

If you were previously using the `open_ai_key` file approach:

1. Copy your API key from the `open_ai_key` file
2. Create a `.env` file and add: `OPENAI_API_KEY=your_key_here`
3. The application will now use environment variables instead of the file-based approach

