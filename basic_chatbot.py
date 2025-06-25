# chatbot

import random  #Used to select random responses

#Define the chatbot function
def chatbot():
    #Lists of possible responses for different types of user input
    greetings = ["Hi! 😊", "Hello! 👋", "Hey! 😄", "Hii! 🙌", "Howdy! 🤠"]
    how_are_you_responses = ["I'm good, thanks! 😎", "Doing well! 👍", "Feeling great! 😃", "All good here! ✅"]
    fine_responses = ["Nice! 😁", "Glad to hear that! 😊", "Awesome! 🎉", "Great! 🙌"]
    unknown_responses = ["Sorry, I didn't get that. 🤔", "Can you rephrase? 🧐", "Hmm, not sure I understand. 😅"]
    #Initial greeting when the chatbot starts
    print("Bot: Hi! I'm ChatBot. Type 'bye' to end the chat.")

    #Start an infinite loop to keep chatting until user types 'bye'
    while True:
        user_input = input("You: ").lower().strip()
        #Get user input, convert to lowercase and strip spaces

        #If user input contains any greeting word
        if any(greet in user_input for greet in ["hello", "hi", "hii", "hey"]):
            print("Bot:", random.choice(greetings))  #Reply with a random greeting

        #If user asks "how are you"
        elif "how are you" in user_input:
            print("Bot:", random.choice(how_are_you_responses))
            #Reply with a random "I'm fine" type message

        #If user says they are fine
        elif user_input in ["fine", "good", "great", "i'm fine", "doing good"]:
            print("Bot:", random.choice(fine_responses))  #Reply positively

        #If user asks or mentions a name
        elif "name" in user_input:
            print("Bot: I'm just a simple chatbot. What's your name?")

        #If user says "my name is ..."
        elif user_input.startswith("my name is"):
            name = user_input.replace("my name is", "").strip()  #Extract the name
            print(f"Bot: Nice to meet you, {name}!")  #Personalize the reply

        #If user types "bye", end the chat
        elif user_input == "bye":
            print("Bot: Bye! Have a great day 👋")
            break  #Exit the loop

        #Default case for unknown input
        else:
            print("Bot:", random.choice(unknown_responses))  #Generic response when input is not understood

#Call the chatbot function to start the conversation
chatbot()

