from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI()

# Define the prompt
messages = [
    {
        "role": "developer",
        "content": "You are a helpful assistant that answers questions clearly and concisely."
    },
    {
        "role": "user",
        "content": "Explain the importance of context management in text generation."
    }
]

# Generate a response
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages
)

# Extract and print the generated response
print(response.choices[0].message["content"])


import requests

# Define the AnkiConnect API endpoint
ANKI_CONNECT_URL = "http://localhost:8765"

def create_flashcard(deck_name, front, back):
    payload = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deck_name,
                "modelName": "Basic",
                "fields": {
                    "Front": front,
                    "Back": back,
                },
                "tags": [],
                "options": {
                    "allowDuplicate": False
                }
            }
        }
    }

    response = requests.post(ANKI_CONNECT_URL, json=payload)
    if response.status_code == 200:
        result = response.json()
        if result.get("error") is None:
            print(f"Card added successfully: {result}")
        else:
            print(f"Error: {result['error']}")
    else:
        print(f"Failed to connect to Anki. Status code: {response.status_code}")

# Example usage
deck_name = "My Python Deck"  # Replace with your deck name
front = "What is the capital of France?"
back = "Paris"

create_flashcard(deck_name, front, back)

# List of flashcards (front, back pairs)
flashcards = [
    ("What is the capital of France?", "Paris"),
    ("What is the capital of Germany?", "Berlin"),
    ("What is the capital of Japan?", "Tokyo")
]

for front, back in flashcards:
    create_flashcard("My Python Deck", front, back)
