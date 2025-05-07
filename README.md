# 🧠 Sunbird Ed AI Assistant (MCP Protocol Integration)

This project is a prototype AI assistant integrated with the **Sunbird Ed** learning platform using **Model Context Protocol (MCP)** concepts. The goal is to enable contextual, conversational support for learners and admins, powered by **LLaMA 3** (via Ollama) and Sunbird APIs.

> ✅ Successfully demonstrates API tooling, agent reasoning, and installation-level context using mocked data.

for architecture workflow please refer to: [architecture.md](architecture.md)

## 🚀 Project Overview

Sunbird Ed is a modular Digital Public Good (DPG) that supports personalized learning and skilling at scale. This project introduces an **AI assistant** that can:

- Answer user queries about course metadata, enrollments, and progress.
- Simulate Sunbird Ed behavior using mock API responses.
- Provide intelligent responses using an LLM (LLaMA 3) with tool-calling logic.
- Lay the foundation for personalized learning support using MCP.

## 🛠 Tech Stack

- **Language**: Python  
- **Model**: [LLaMA 3 (via Groq API)](https://console.groq.com/) 
- **MCP SDK**: Conceptually implemented with tool schemas (No official Python MCP Agent SDK used yet)  
- **API Simulation**: Local mock APIs (Mockoon)  
- **Env Management**: `dotenv`  
- **CLI Interface**: Command-line interface  
- **Pycharm**

## ⚙️ Setup Instructions

1. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**

   Create a `.env` file in the root directory:

   ```env
   PYTHONPATH=/path/to/sunbird-ai-assistant   # Replace with your actual path
   MCP_MODEL=llama3-8b-8192             # Replace with any other model
   MCP_API_BASE=https://api.groq.com/openai/v1
   MCP_API_KEY=your_groq_api_key_here    # Paste your API key here

   ```

## 🧪 Testing Instructions (LLaMA 3 Required)

To run the project using LLaMA 3:

1. Start the Assistant:
   To run the assistant using Groq's hosted LLaMA 3 or other model:

   Sign up and get an API key from [Groq Console](https://console.groq.com/)
   Add the API key to your `.env` file as shown above
   Start the assistant:

   ```bash
   python cli/main.py
   ```

Note: `PYTHONPATH` is automatically appended to `sys.path` during runtime.

## ✅ Current Features

- Fetch course listings via `course/v1/search` (mocked)
- Retrieve user enrollment data via `user/enrollment/list` (mocked)
- Display user profile and progress via `user/v1/profile` (mocked)
- Run contextual CLI chat using LLaMA 3 with tool calling logic

## 🌟 Future Improvements

- 🔄 Replace mocked endpoints with real Sunbird API integration
- 🎯 Add user-level personalization and intelligent guidance
- 🧠 Incorporate official Python MCP Agent SDK (once available)
- 🌐 Launch a web-based interface (Phase 2)

## 🔐 Requesting API Access

Currently using mock APIs. Access to official Sunbird APIs (`course/v1/search`, `user/v1/profile`, `user/enrollment/list`) is requested to enable real-world deployment and validation.

## 📄 License

This project is part of **Code4GovTech** and is open-sourced under the **MIT License**.

## 👥 Contributors

- **Ganasekhar Kalla** – Developer & MCP Agent Integration  
- **Sunbird Community** – API & Documentation Support
