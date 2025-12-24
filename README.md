[readme.md](https://github.com/user-attachments/files/24323032/readme.md)
# 🚔 Law Enforcement Report Intelligence System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

An AI-powered system that revolutionizes law enforcement report generation and analysis through natural language processing, automated penal code identification, and intelligent document processing.

## 🎥 System Demo

[![Demo Video](https://img.shields.io/badge/🎥_Demo-View_on_Loom-blueviolet)](https://www.loom.com/share/bbc0e7b67a174710baa3851ca7e0f8a4?sid=94e1263b-727f-489c-9099-6aed13ac35cf)

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies](#technologies)
- [Notebooks Overview](#notebooks-overview)
- [Contributing](#contributing)
- [Legal Disclaimer](#legal-disclaimer)
- [License](#license)

## 🎯 Overview

The Law Enforcement Report Intelligence System is a comprehensive solution designed to assist law enforcement professionals in creating accurate, legally compliant reports. By leveraging state-of-the-art natural language processing and machine learning models, the system automates time-consuming tasks such as penal code identification, statement generation, and entity extraction from incident reports.

### Problem Statement

Law enforcement officers spend significant time on administrative tasks, particularly in:

- Identifying relevant penal codes for incidents
- Drafting detailed incident reports and statements
- Ensuring legal compliance with CALCRIM standards
- Cross-referencing entities across multiple reports
- Maintaining consistency in documentation

### Our Solution

This system provides an intelligent assistant that:

- **Analyzes** incident descriptions to automatically suggest relevant California penal codes
- **Generates** professional officer statements based on incident details
- **Processes** PDF documents to extract key information using transformer models
- **Matches** entities across different reports for case correlation
- **Provides** an interactive chatbot interface for report queries

## ✨ Key Features

### 🔍 Automated Penal Code Identification

- Intelligent analysis of incident narratives
- Automatic mapping to California Penal Codes
- CALCRIM 2023 Edition compliance
- Context-aware code recommendations

### 📝 Statement Generation

- AI-powered officer statement drafting
- Professional formatting and legal terminology
- Customizable templates
- Incident-specific detail integration

### 📄 PDF Document Processing

- DistilBERT-powered text extraction
- Structured information retrieval
- Multi-document analysis
- Entity recognition and classification

### 🤖 Interactive Chatbot

- Natural language queries about reports
- Real-time information retrieval
- Context-aware responses
- Case history search

### 🔗 Entity Matching

- Cross-report entity linking
- Suspect/witness identification
- Location correlation
- Timeline reconstruction

### 🖥️ Web Interface

- Streamlit-based user interface
- Intuitive report submission
- Real-time processing feedback
- Export capabilities

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface Layer                      │
│              (Streamlit Web Application)                     │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                  Processing Layer                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Penal Code │  │  Statement   │  │   Entity     │      │
│  │   Generator  │  │  Generator   │  │   Matcher    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                    AI/ML Layer                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  DistilBERT  │  │     NLP      │  │  Document    │      │
│  │   Embeddings │  │   Pipeline   │  │  Processing  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                    Data Layer                                │
│       CALCRIM Database • Reports • Case Files                │
└──────────────────────────────────────────────────────────────┘
```

## High-Level Architecture

```
            ┌─────────────────────┐
            │  Incident Report /  │
            │   Legal PDF Input   │
            └─────────┬───────────┘
                      │
                      ▼
            ┌─────────────────────┐
            │  PDF Text Extraction│
            │  & Preprocessing    │
            └─────────┬───────────┘
                      │
                      ▼
            ┌─────────────────────┐
            │  NLP Pipeline       │
            │  (DistilBERT, NLP) │
            └─────────┬───────────┘
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
┌───────────────────┐   ┌────────────────────┐
│ Entity Extraction │   │ Semantic Similarity │
│ & Normalization   │   │ & Matching          │
└─────────┬─────────┘   └─────────┬──────────┘
          │                       │
          └───────────┬───────────┘
                      ▼
            ┌─────────────────────┐
            │ Penal Code Reasoning│
            │ & Mapping Engine   │
            └─────────┬───────────┘
                      │
                      ▼
            ┌─────────────────────┐
            │ Statement & Report  │
            │ Generation Module  │
            └─────────┬───────────┘
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
┌───────────────────┐   ┌────────────────────┐
│ Chatbot Interface │   │ Streamlit Web App  │
└───────────────────┘   └────────────────────┘
```

## Processing Flow (End-to-End)

```
Raw Text / PDF
      ↓
Cleaning & Segmentation
      ↓
Embedding & Semantic Encoding
      ↓
Entity Detection & Matching
      ↓
Legal Context Inference
      ↓
Penal Code Suggestions
      ↓
Formal Narrative Generation
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- 4GB+ RAM recommended
- CUDA-compatible GPU (optional, for faster processing)

### Setup

1. **Clone the repository**

```bash
git clone https://github.com/AsmaEman/Report-Project.git
cd Report-Project
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Install additional NLP models**

```bash
python -m spacy download en_core_web_sm
```

5. **Set up environment variables**

```bash
cp .env.example .env
# Edit .env with your configuration
```

## 💻 Usage

### Running the Streamlit Application

```bash
cd streamlit_app
streamlit run app.py
```

The application will be available at `http://localhost:8501`

### Using Individual Notebooks

#### Penal Code Generation

```python
# Open PenalCodeGeneratorImprovedCode.ipynb
# Input incident description
# Get relevant penal codes with confidence scores
```

#### Statement Generation

```python
# Open ReportingOfficer'sStatement.ipynb
# Provide incident details
# Generate professional officer statement
```

#### Document Processing

```python
# Open DistilBERTPDFProcessing.ipynb
# Upload PDF reports
# Extract and analyze content
```

### Example Workflow

```python
from report_system import PenalCodeGenerator, StatementGenerator

# Initialize generators
penal_gen = PenalCodeGenerator()
statement_gen = StatementGenerator()

# Incident description
incident = """
On 12/24/2025 at approximately 14:30 hours,
officers responded to a residential burglary at
123 Main Street...
"""

# Generate penal codes
codes = penal_gen.generate(incident)
print(f"Relevant Codes: {codes}")

# Generate officer statement
statement = statement_gen.create_statement(incident, codes)
print(statement)
```

## 📁 Project Structure

```
Report-Project/
│
├── streamlit_app/              # Web application
│   ├── app.py                  # Main Streamlit app
│   ├── pages/                  # Multi-page app structure
│   └── utils/                  # Helper functions
│
├── notebooks/                  # Jupyter notebooks
│   ├── PenalCodeGenerator.ipynb
│   ├── PenalCodeGeneratorImprovedCode.ipynb
│   ├── ReportingOfficer'sStatement.ipynb
│   ├── PenalCode&StatementGenerator.ipynb
│   ├── PenalCode&StatementGenerator2.ipynb
│   ├── DistilBERTPDFProcessing.ipynb
│   ├── EntityMatching.ipynb
│   ├── Report_ChatBot.ipynb
│   └── StatementPrompt.ipynb
│
├── Sample Reports/             # Example reports and test data
│   └── ...
│
├── data/                       # Data files
│   ├── calcrim_2023_edition.pdf
│   ├── Incident_Report.pdf
│   └── 242_231119_070754.pdf
│
├── models/                     # Trained models (not included)
│   └── .gitkeep
│
├── Report.docx                 # Template document
├── requirements.txt            # Python dependencies
├── .gitignore
└── README.md
```

## 🛠️ Technologies

### Core Technologies

- **Python 3.8+**: Primary programming language
- **Jupyter Notebook**: Interactive development environment
- **Streamlit**: Web application framework

### Machine Learning & NLP

- **Transformers (Hugging Face)**: DistilBERT model implementation
- **PyTorch**: Deep learning framework
- **spaCy**: Industrial-strength NLP
- **NLTK**: Natural language toolkit
- **scikit-learn**: Machine learning utilities

### Document Processing

- **PyPDF2**: PDF manipulation
- **python-docx**: Word document generation
- **pdfplumber**: Advanced PDF text extraction

### Data Handling

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **regex**: Advanced pattern matching

## 📓 Notebooks Overview

### `PenalCodeGenerator.ipynb`

Initial implementation of penal code identification system using keyword matching and rule-based approaches.

### `PenalCodeGeneratorImprovedCode.ipynb`

Enhanced version with machine learning models, improved accuracy, and confidence scoring.

### `ReportingOfficer'sStatement.ipynb`

Generates professional officer statements from incident data with proper formatting and legal terminology.

### `PenalCode&StatementGenerator.ipynb` & `PenalCode&StatementGenerator2.ipynb`

Integrated systems combining both penal code identification and statement generation with various iterations.

### `DistilBERTPDFProcessing.ipynb`

Utilizes DistilBERT transformer model for intelligent PDF document processing and information extraction.

### `EntityMatching.ipynb`

Advanced entity recognition and matching across multiple documents for case correlation.

### `Report_ChatBot.ipynb`

Interactive conversational interface for querying reports and retrieving information.

### `StatementPrompt.ipynb`

Template and prompt engineering for optimized statement generation.

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guidelines
- Write clear commit messages
- Add unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

## ⚖️ Legal Disclaimer

**IMPORTANT**: This system is designed as an assistive tool for law enforcement professionals. It does not replace professional judgment, legal expertise, or official procedures.

- All generated content should be reviewed by qualified personnel
- The system provides suggestions, not legal advice
- Users are responsible for verifying accuracy and compliance
- CALCRIM references are for informational purposes only
- Always consult with legal counsel for case-specific guidance

This software is provided "as is" without warranty of any kind. The developers assume no liability for any use of this system.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Hugging Face for transformer models
- The open-source community for various libraries and tools
- Law enforcement professionals who provided domain expertise

---
