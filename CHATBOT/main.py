# Define responses
responses = {
    "hi": "Hello! How can I help you?",
    "how are you": "I'm good, thank you for asking.",
    "bye": "Goodbye! Have a great day."
}

# Chatbot function
def chatbot():
    print("Welcome! How can I assist you?")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = responses.get(user_input, "I'm not sure how to respond to that.")
        print("Chatbot:", response)

# Main code
chatbot()
