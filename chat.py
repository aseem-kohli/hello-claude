
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

MODEL = "claude-sonnet-5"
SYSTEM = "You are a concise, friendly assistant. Keep answers short and direct."


def main():
    messages = []
    print('Welcome to claude chat. Ask a question and continue conversation. Send exit to quit')
    while True:
        user_input = input("You: ")
        if user_input == 'exit':
            break
        messages.append({"role": "user", "content": user_input})

        print("Claude: ", end="", flush=True)
        with client.messages.stream(
            model=MODEL,
            max_tokens=1000,
            system=SYSTEM,
            messages=messages,
        ) as stream:
            for chunk in stream.text_stream:
                print(chunk, end="", flush=True)
            response = stream.get_final_message()
        print()

        assistant_text = next((block.text for block in response.content if block.type == "text"), "")
        messages.append({"role": "assistant", "content": assistant_text})


if __name__ == "__main__":
    main()
