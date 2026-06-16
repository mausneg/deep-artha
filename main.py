from deepagents import create_deep_agent
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

class DeepArtha:
    def __init__(self):
        self._model = ChatOllama(
            model="gemma4:31b-cloud",
            base_url="https:ollama.com"
        )
        self._agent = create_deep_agent(
            model=self._model,
            system_prompt="you are a helpful assistant."
        )

    def invoke(self, question: str, conversation_id: str):
        pass
    
def main():
    print("Hello from deep-artha!")


if __name__ == "__main__":
    main()
