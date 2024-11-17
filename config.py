from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configuration constants
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
CLIENT_SECRET_FILE = os.getenv("CLIENT_SECRET_FILE", "client_secret.json")
CALLS_PER_MINUTE = int(os.getenv("CALLS_PER_MINUTE", 30))
SEARCH_CALLS_PER_MINUTE = int(os.getenv("SEARCH_CALLS_PER_MINUTE", 50))
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
# Validate required variables
required_env_vars = ["GROQ_API_KEY", "SERPER_API_KEY", "CLIENT_SECRET_FILE"]
for var in required_env_vars:
    if not os.getenv(var):
        raise ValueError(f"Missing required environment variable: {var}")
