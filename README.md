# RAG-AGENT

A sophisticated multi-turn Retrieval-Augmented Generation (RAG) agent that combines intelligent document retrieval, web search capabilities, and an intuitive interface for seamless data ingestion and interaction.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Components](#components)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)

## 🎯 Overview

RAG-AGENT is an advanced AI-powered system designed to provide accurate, context-aware responses by combining:

- **Retrieval-Augmented Generation**: Leverages a knowledge base to ground responses in actual documents
- **Web Search Integration**: Extends knowledge beyond stored documents using Bing Search API
- **Multi-turn Conversations**: Maintains context across multiple interactions for coherent dialogue
- **Document Management**: Intelligent indexing and retrieval using Azure AI Search

This system is ideal for customer support, knowledge base querying, research assistance, and intelligent information retrieval tasks.

## ✨ Features

### Core Capabilities

- **Multi-turn Conversation Support**
  - Maintains conversation history and context
  - Understands follow-up questions with proper context awareness
  - Supports back-and-forth dialogue sessions

- **Dual Search Tools**
  - **Document Search**: Query indexed documents via Azure AI Search
  - **Web Search**: Real-time web search powered by Bing Search API
  - Intelligent tool selection based on query type

- **Document Management System**
  - Upload and ingest documents (PDF, TXT, DOCX, etc.)
  - Real-time document preview before indexing
  - Automatic chunking and embedding generation
  - Vector-based semantic search

- **Intuitive Web Interface**
  - Clean, responsive UI for querying
  - Document upload and management dashboard
  - Data preview functionality
  - Conversation history tracking
  - Search result visualization

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    User Interface                            │
│            (Web Interface + Document Ingestion)              │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                  RAG Agent Engine                            │
│          (Multi-turn Conversation Manager)                   │
└────────┬───────────────────────┬───────────────────────┬────┘
         │                       │                       │
    ┌────▼─────┐         ┌──────▼──────┐        ┌──────▼──────┐
    │ Document │         │ Bing Search │        │   Context   │
    │  Search  │         │    Tool     │        │   Manager   │
    │(Azure AI │         │             │        │             │
    │ Search)  │         └─────────────┘        └─────────────┘
    └────┬─────┘
         │
┌────────▼────────────────────────────────────────────────────┐
│            Knowledge Base & Vector Store                     │
│           (Azure AI Search + Embeddings)                     │
└──────────────────────────────────────────────────────────────┘
```

## 🛠️ Tech Stack

### Backend
- **Language**: Python / Node.js
- **LLM**: OpenAI GPT-4 / Azure OpenAI
- **Vector Database**: Azure AI Search
- **Web Search**: Bing Search API
- **Framework**: FastAPI / Express.js

### Frontend
- **Framework**: React / Vue.js
- **UI Components**: Tailwind CSS / Material UI
- **State Management**: Redux / Pinia
- **Real-time Updates**: WebSockets

### Cloud Infrastructure
- **Azure AI Search**: Document indexing and semantic search
- **Azure OpenAI**: Language model and embeddings
- **Azure App Service**: Backend deployment
- **Azure Static Web Apps**: Frontend hosting

## 📦 Components

### 1. **RAG Agent Engine**
The core intelligence system that orchestrates:
- Query interpretation and routing
- Tool selection and execution
- Response generation with source attribution
- Conversation state management

### 2. **Document Ingestion Pipeline**
Handles the document upload and processing workflow:
- File upload and validation
- Document parsing and chunking
- Embedding generation
- Index creation in Azure AI Search
- Preview generation

### 3. **Search Tools**

#### Document Search
- Queries indexed documents in Azure AI Search
- Performs semantic and keyword search
- Returns ranked results with relevance scores
- Provides source attribution

#### Web Search
- Integrates Bing Search API
- Retrieves real-time information
- Supplements document knowledge
- Tracks search sources

### 4. **Web Interface**
User-facing application providing:
- **Query Interface**: Multi-turn conversation view
- **Document Management**: Upload, preview, and delete documents
- **Settings Panel**: Configuration and preferences
- **Results Display**: Formatted responses with sources

### 5. **Context Manager**
Maintains conversation state:
- Conversation history
- Token management
- Context window optimization
- Session persistence

## 🚀 Getting Started

### Prerequisites

- Python 3.9+ / Node.js 18+
- Azure subscription
- Azure OpenAI deployed instance
- Bing Search API key
- Azure AI Search service

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/RAG-AGENT.git
   cd RAG-AGENT
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   ```

4. **Configuration**
   - Create `.env` file with required credentials:
   ```
   AZURE_OPENAI_ENDPOINT=your_endpoint
   AZURE_OPENAI_KEY=your_key
   AZURE_SEARCH_ENDPOINT=your_search_endpoint
   AZURE_SEARCH_KEY=your_search_key
   BING_SEARCH_KEY=your_bing_key
   ```

5. **Start the Application**
   ```bash
   # Terminal 1: Backend
   cd backend && python main.py
   
   # Terminal 2: Frontend
   cd frontend && npm start
   ```

## 💬 Usage

### Query the RAG Agent

1. **Open the Web Interface**
   - Navigate to `http://localhost:3000`

2. **Ask a Question**
   - Type your query in the chat interface
   - The agent automatically selects appropriate tools
   - Review the response and source documents

3. **Multi-turn Conversation**
   - Follow up with related questions
   - Agent maintains conversation context
   - Reference previous interactions

### Ingest Documents

1. **Access Document Management**
   - Click "Upload Documents" in the interface

2. **Preview Documents**
   - View document preview before ingestion
   - Verify content and formatting

3. **Complete Ingestion**
   - Confirm upload
   - Monitor ingestion progress
   - Documents indexed and searchable

## ⚙️ Configuration

### Model Settings
- Temperature, top_p, max_tokens
- System prompts and instructions
- Response formatting

### Search Settings
- Document search confidence threshold
- Web search result count
- Result ranking preferences

### Tool Settings
- Enable/disable Bing search
- Document search only mode
- Hybrid search configuration

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions, please open an issue on GitHub or contact the development team.