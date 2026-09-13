
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

MODEL = "claude-opus-5"


def main():
    messages = []
    print('Welcome to claude chat. Ask a question and continue conversation. Send exit to quit')
    while True:
        user_input = input()
        if user_input == 'exit':
            break
        messages.append({"role": "user", "content": user_input})
        response = client.messages.create(
            model=MODEL,
            max_tokens=16000,
            messages=messages,
        )

        assistant_text = next(block.text for block in response.content if block.type == "text")
        print(assistant_text)
        messages.append({"role": "assistant", "content": assistant_text})


if __name__ == "__main__":
    main()
