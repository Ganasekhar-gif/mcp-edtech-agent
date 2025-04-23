# 🧠 Sunbird Ed AI Assistant (MCP Protocol Integration)                                                                             

This project is a prototype AI assistant integrated with the **Sunbird Ed** learning platform using **Model Context Protocol (MCP)** concepts. The goal is to enable contextual, conversational support for learners and admins, powered by **LLaMA 3** (via Ollama) and mock Sunbird APIs.                                                                         

> ✅ Successfully demonstrates API tooling, agent reasoning, and installation-level context using mocked data.                                                                 

---

## 🚀 Project Overview                                                                       

Sunbird Ed is a modular Digital Public Good (DPG) that supports personalized learning and skilling at scale. This project introduces an **AI assistant** that can:                     

- Answer user queries about course metadata, enrollments, and progress.                                                 
- Simulate Sunbird Ed behavior using mock API responses.                                                                                          
- Provide intelligent responses using an LLM (LLaMA 3) + tool calling logic.                                                                                 
- Lay the foundation for personalized learning support using MCP.                                                                                                     

---

## 🛠 Tech Stack                                                                                                                      

- **Language**: Python                                                                                                                                                     
- **Model**: [LLaMA 3 (via Ollama)](https://ollama.com/library/llama3)                                                                                                                                      
- **MCP SDK**: *Conceptually implemented* with tool schemas (No official Python MCP Agent SDK used yet)                                                                                                    
- **API Simulation**: Local mock APIs (FastAPI or static mocks)                                                                                                                                           
- **Env Management**: `dotenv`                                                                                                                                                                
- **CLI Interface**: Simple command-line agent interface                                                                                                                                        

---

## 📁 Project Structure                                                                                        

sunbird-ai-assistant/                                                                                                                          
│
├── llm/                                                                                                                                            
│   ├── __init__.py                                                                                                                                         
│   └── mistral_wrapper.py         # custom LLM wrapper (simulates MCP agent)                                                                                                 
│
├── tools/                                                                                                                              
│   ├── __init__.py                                                                                                                                               
│   └── course_metadata.py         # Tool: fetch course info from mock API                                                                                                            
│   └── user_enrollment.py         # Tool: user enrollment status                                                                                                                          
│   └── progress_tracker.py        # Tool: learning progress data                                                                                                                          
│
├── context/                                                                                                                                                                             
│   └── installation_context.py    # Handles loading installation-level context                                                                                                                  
│                                                                                                                                                                                                     
├── cli/                                                                                                                                                                                            
│   └── main.py                    # Chatbot CLI interface                                                                                                                                      
│                                                                                                                                                                                
├── configs/                                                                                                                                                                                 
│   └── tool_schemas.json          # Tool schema definitions                                                                                                                                    
│   └── settings.py                # Configuration file (base URL, ports, etc.)                                                                                                                           
│
├── requirements.txt               # Python dependencies                                                                                                                                        
└── README.md                      # Project README                                                                                                                                                           


---

## ⚙️ Setup Instructions                                                                                                                                                            
                                                                                                                                                                                             
1. **Install Requirements**                                                                                                                                                               
   ```bash                                                                                                                                                                                      
   pip install -r requirements.txt                                                                                                                                                                        

2. Set Environment Variables Create a .env file:                                                                                                                                 
   
PYTHONPATH=D:/sunbird-ai-assistant  # working directory change accordingly                                                                                                                              
MCP_MODEL=llama3                                                                                                                                                                               
MCP_API_BASE=http://localhost:11434/v1                                                                                                                                                             
MCP_API_KEY=null 

## 🧪 Testing Instructions (LLaMA 3 Required)                                                                                                                                      

To run this project with LLaMA 3:                                                                                                                                                        

1. Download and install [Ollama](https://ollama.com/download)
2. Open your terminal and run:                                                                                                                                                          
   ```bash                                                                                                                                                                      
   ollama pull llama3
   ollama run llama3                                                                                                                                                                                     
   ollama serve                                                                                                                                                                                               


3. Run the Assistant                                                                                                                                                                                                                                                            
python cli/main.py                                                                                                                                                                                       

Note: PYTHONPATH is automatically loaded and appended to sys.path during runtime.                                                                                                                     

 Current Features                                                                                                                                                         
 Course listing via course/v1/search (mocked)                                                                                                                                            
 Enrollment data via user/enrollment/list (mocked)                                                                                                                                               
 User profile and progress via user/v1/profile (mocked)                                                                                                                                  
 CLI test loop for simulating contextual queries                                                                                                                                                    
 Model reasoning using LLaMA 3 with tool calling                                                                                                                                                     

  Future Improvements                                                                                                                                                                               
🔄 Replace mocks with real Sunbird API integration                                                                                                                                                           
🎯 Extend support to user-level personalization                                                                                                                                                             
🧠 Use official Python MCP Agent SDK (if needed)                                                                                                                                                        
🌐 Add web-based interface (Phase 2)                                                                                                                                                                   

Requesting API Access                                                                                                                                                                                    
We are currently using mock APIs. Access to real APIs (e.g., course/v1/search, user/v1/profile, user/enrollment/list) is requested for full integration and validation with Sunbird Ed.              

License                                                                                                                                                                                                   
This project is developed as part of Code4GovTech and is open-source under the MIT License.                                                                                                               

Contributors                                                                                                                                                                                          
Ganasekhar Kalla - Developer & MCP Agent Integration                                                                                                                                                               
Sunbird Community (API & Docs)                                                                                                                                                                                    
