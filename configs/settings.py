import os
from dotenv import load_dotenv

BASE_URL = "http://localhost:3010"

load_dotenv()

MCP_API_BASE = os.getenv("MCP_API_BASE")
MCP_MODEL = os.getenv("MCP_MODEL")
MCP_API_KEY = os.getenv("MCP_API_KEY")
