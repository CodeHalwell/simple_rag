# LangChain 1.0 Alpha Upgrade Guide

## Overview

This document describes the upgrade to LangChain 1.0.0 alpha release (1.0.0a10).

## Package Versions

The following packages have been updated:

| Package | Previous Version | New Version |
|---------|-----------------|-------------|
| langchain | 0.3.27 | 1.0.0a10 |
| langchain-core | 0.3.74 | 0.3.76+ |
| langchain-openai | 0.3.30 | 0.3.33+ |
| langchain-community | 0.3.27 | 0.3.30+ |
| langchain-text-splitters | 0.3.9 | 0.3.11+ |
| langchain-chroma | 0.2.5 | 0.2.6+ |

## What's New in LangChain 1.0

LangChain 1.0 is the first major release focused on:

- **Stability**: Production-ready APIs with long-term support
- **Performance**: Optimized implementations and reduced overhead
- **Type Safety**: Improved type hints and validation
- **Documentation**: Comprehensive guides and examples
- **Backward Compatibility**: Minimal breaking changes from 0.3.x

## Installation

### Using pip

```bash
pip install -r requirements.txt
```

Note: The `requirements.txt` file specifies `langchain==1.0.0a10` to install the alpha release.

### Using UV

```bash
uv sync
```

The `pyproject.toml` file includes the same version specifications.

### Pre-release Installation Note

Since LangChain 1.0 is in alpha, you may need to use the `--pre` flag with pip:

```bash
pip install --pre langchain==1.0.0a10
```

## Compatibility

### Code Changes

No code changes are required from the LangChain 0.3.x version. The following imports remain compatible:

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
```

### API Compatibility

The following APIs used in this project remain unchanged:

- `PyPDFLoader(pdf_path)`
- `RecursiveCharacterTextSplitter(chunk_size, chunk_overlap)`
- `OpenAIEmbeddings(api_key)`
- `Chroma.from_documents(docs, embedding_function)`
- `PromptTemplate.from_template(template)`

## Testing

### Verification Steps

1. **Install the packages**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the validation script**:
   ```bash
   python validate_setup.py
   ```

3. **Check the installed version**:
   ```bash
   python -c "import langchain; print(f'LangChain version: {langchain.__version__}')"
   ```
   
   Expected output: `LangChain version: 1.0.0a10`

4. **Test the application**:
   ```bash
   streamlit run rag_chat.py
   ```

### Known Issues

- **Alpha Release Warning**: LangChain 1.0 is currently in alpha. While it's stable for testing, use caution in production environments.
- **Network Issues**: Some users may experience timeouts when installing from PyPI. If this occurs, try:
  ```bash
  pip install --default-timeout=300 -r requirements.txt
  ```

## Rollback Instructions

If you need to roll back to LangChain 0.3.x:

1. **Edit requirements.txt**:
   Change `langchain==1.0.0a10` to `langchain>=0.3.27`

2. **Edit pyproject.toml**:
   Change `langchain==1.0.0a10` to `langchain>=0.3.27`

3. **Reinstall**:
   ```bash
   pip install -r requirements.txt --force-reinstall
   ```

## References

- [LangChain GitHub Repository](https://github.com/langchain-ai/langchain)
- [LangChain Release Notes](https://github.com/langchain-ai/langchain/releases)
- [LangChain Documentation](https://python.langchain.com/)

## Support

For issues or questions related to this upgrade:

1. Check the [project README](README.md) for general setup instructions
2. Run `python validate_setup.py` to diagnose issues
3. Review the [LangChain 1.0 release notes](https://github.com/langchain-ai/langchain/releases?q=tag%3A%22langchain%3D%3D0%22&expanded=true)
4. Open an issue on the [project repository](https://github.com/CodeHalwell/simple_rag/issues)
