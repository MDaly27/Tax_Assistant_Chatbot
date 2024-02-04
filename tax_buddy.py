import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'
file_path = "tax_regulations.txt"

def read_documents(file_path):
    with open(file_path, 'r') as file:
        documents = file.read()
    return documents

def ask_openai(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    return response['choices'][0]['message']['content'].strip()

def main():
    documents = read_documents(file_path)

    # Initial message with document information
    document_messages = [
        {"role": "system", "content": "You are an accountant reviewing tax regulations."},
        {"role": "system", "content": documents}
    ]

    # Initialize conversation history
    conversation_history = document_messages.copy()

    while True:
        user_input = input("User: ")

        if user_input.lower() == 'exit':
            break

        # Add user message to the conversation
        user_message = {"role": "user", "content": user_input}
        conversation_history.append(user_message)

        # Get the AI's response
        ai_response = ask_openai(conversation_history)
        print(f"AI: {ai_response}\n")

        # Add AI's response to the conversation
        ai_message = {"role": "assistant", "content": ai_response}
        conversation_history.append(ai_message)

if __name__ == "__main__":
    main()
