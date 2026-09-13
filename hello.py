from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()
msg = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=300,
    messages=[{"role": "user", "content": "In one sentence, what is an AI agent?"}],
)
print(msg.content[0].text)