#!/usr/bin/env python3
"""
Validation script to test the UV package manager setup and environment configuration.

This script helps verify that:
1. All required dependencies are properly installed
2. Environment variables are correctly loaded from .env file
3. The setup is ready for running the RAG chat bot

Usage:
    python validate_setup.py

Or with UV:
    uv run python validate_setup.py
"""

import os
import sys
from pathlib import Path

def test_imports():
    """Test that all required packages can be imported."""
    print("🔍 Testing package imports...")
    
    required_packages = [
        ('dotenv', 'python-dotenv'),
        ('streamlit', 'streamlit'),
        ('openai', 'openai'),
        ('langchain', 'langchain'),
        ('langchain_openai', 'langchain-openai'),
        ('langchain_chroma', 'langchain-chroma'),
        ('langchain_core', 'langchain-core'),
        ('langchain_community', 'langchain-community'),
        ('langchain_text_splitters', 'langchain-text-splitters'),
    ]
    
    missing_packages = []
    
    for package, pip_name in required_packages:
        try:
            mod = __import__(package)
            version = getattr(mod, '__version__', 'unknown')
            print(f"  ✓ {package} ({version})")
        except ImportError:
            print(f"  ✗ {package} (install with: pip install {pip_name})")
            missing_packages.append(pip_name)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Run: pip install " + " ".join(missing_packages))
        return False
    else:
        print("✅ All required packages are available!")
        
        # Check if LangChain 1.0 alpha is installed
        try:
            import langchain
            if langchain.__version__.startswith('1.0.0a'):
                print(f"✅ LangChain 1.0 alpha detected: {langchain.__version__}")
            elif langchain.__version__.startswith('0.3'):
                print(f"ℹ️  LangChain 0.3.x detected: {langchain.__version__}")
                print("   Consider upgrading to 1.0.0a10 for latest features")
        except:
            pass
        
        return True

def test_env_file():
    """Test that .env file exists and contains required variables."""
    print("\n🔍 Testing environment configuration...")
    
    env_file = Path('.env')
    env_example = Path('.env.example')
    
    if not env_file.exists():
        if env_example.exists():
            print("  ⚠️  .env file not found, but .env.example exists")
            print("  📝 Copy .env.example to .env and add your OpenAI API key")
            print("  Command: cp .env.example .env")
        else:
            print("  ✗ Neither .env nor .env.example found")
        return False
    
    print("  ✓ .env file found")
    return True

def test_env_loading():
    """Test that environment variables can be loaded."""
    print("\n🔍 Testing environment variable loading...")
    
    try:
        from dotenv import load_dotenv
        
        # Try to load environment variables
        dotenv_path = Path(__file__).parent / '.env'
        loaded = load_dotenv(dotenv_path=dotenv_path)
        
        if not loaded:
            print("  ⚠️  .env file found but couldn't be loaded")
            return False
        
        # Check for required variables
        openai_key = os.getenv('OPENAI_API_KEY')
        pdf_path = os.getenv('PDF_PATH', 'pdfs/YOUR_PDF_FILE.pdf')
        
        if not openai_key:
            print("  ⚠️  OPENAI_API_KEY not found in environment")
            print("  📝 Add OPENAI_API_KEY=your_api_key_here to your .env file")
            return False
        elif openai_key == "your_openai_api_key_here":
            print("  ⚠️  OPENAI_API_KEY still has placeholder value")
            print("  📝 Replace with your actual OpenAI API key in .env file")
            return False
        else:
            print(f"  ✓ OPENAI_API_KEY found (length: {len(openai_key)})")
        
        print(f"  ✓ PDF_PATH: {pdf_path}")
        
        return True
        
    except ImportError:
        print("  ✗ python-dotenv not available")
        return False

def test_pdf_directory():
    """Test that PDF directory exists."""
    print("\n🔍 Testing PDF directory...")
    
    pdf_dir = Path('pdfs')
    if not pdf_dir.exists():
        print("  ⚠️  pdfs/ directory not found")
        print("  📝 Create pdfs/ directory and add your PDF files")
        return False
    
    pdf_files = list(pdf_dir.glob('*.pdf'))
    if not pdf_files:
        print("  ⚠️  No PDF files found in pdfs/ directory")
        print("  📝 Add PDF files to pdfs/ directory")
        return False
    
    print(f"  ✓ Found {len(pdf_files)} PDF file(s)")
    for pdf_file in pdf_files:
        print(f"    - {pdf_file.name}")
    
    return True

def main():
    """Run all validation tests."""
    print("🚀 Simple RAG Setup Validation")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_env_file,
        test_env_loading,
        test_pdf_directory,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"  ❌ Test failed with error: {e}")
            results.append(False)
    
    print("\n" + "=" * 40)
    
    if all(results):
        print("🎉 All tests passed! Your setup is ready.")
        print("\nYou can now run the chat bot with:")
        print("  streamlit run rag_chat.py")
        print("\nOr with UV:")
        print("  uv run streamlit run rag_chat.py")
        return 0
    else:
        print("⚠️  Some tests failed. Please address the issues above.")
        print("\nFor help, check the README.md file or the project documentation.")
        return 1

if __name__ == "__main__":
    sys.exit(main())