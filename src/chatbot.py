import requests
import json

class ChatBot:
    def __init__(self):
        self.api_key = "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"
        self.base_url = "https://openrouter.ai/api/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "https://github.com/OpenRouterTeam/openrouter-python",
            "X-Title": "Console Chat with LLM"
        }

    def chat(self, user_input):
        """Process user input and return the model's response"""
        try:
            response = requests.post(
                url=f"{self.base_url}/chat/completions",
                headers=self.headers,
                json={
                    "model": "google/gemini-pro",
                    "messages": [
                        {
                            "role": "user",
                            "content": user_input
                        }
                    ]
                }
            )
            
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    print("Welcome to the ChatBot! Type 'exit' to quit.")
    print("Initializing chatbot...")
    try:
        chatbot = ChatBot()
        print("Chatbot initialized successfully!")
    except Exception as e:
        print(f"Error initializing chatbot: {str(e)}")
        return

    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input:
                print("Please enter a message.")
                continue
                
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
                
            response = chatbot.chat(user_input)
            print(f"\nBot: {response}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main() 