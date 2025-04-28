import os
from dotenv import load_dotenv
import sys

load_dotenv()

PYTHONPATH = os.getenv("PYTHONPATH")

if PYTHONPATH not in sys.path:
    sys.path.append(PYTHONPATH)

from llm.mistral_wrapper import call_llama3 
from termcolor import colored 


def run_chat():
    print("🤖 Sunbird AI Assistant (Type 'exit' to quit)\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ['exit', 'quit']:
                print("👋 Goodbye!")
                break

            # Call the LLM (Llama3) model
            response = call_llama3(user_input)  
            print("\n" + colored("Assistant:", "cyan"), colored(response, "green") + "\n")


        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"[Error]: {e}\n")


if __name__ == "__main__":
    run_chat()
