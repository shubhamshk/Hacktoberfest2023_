from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English language data
trainer.train('chatterbot.corpus.english')

# Chat with the bot
print("Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    response = chatbot.get_response(user_input)
    print("Bot:", response)
