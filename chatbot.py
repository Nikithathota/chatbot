import nltk
from nltk.chat.util import Chat, reflections

def greet():
    return "Hey there! I'm your helpful chat companion. What can I do for you today? Feel free to share, and let's have a friendly chat!"

def farewell():
    return "See you later! If you ever have more questions or just want to chat, feel free to drop by. I'm here to help and have a friendly conversation whenever you need!"

def handle_basic_questions(user_input):

    if "your name" in user_input:
        return "I'm just a chatbot, so I don't have a personal name."
    elif "your purpose" in user_input or "why are you here" in user_input:
        return "I'm here to assist and chat with you. Ask me anything!"

    elif "capabilities" in user_input or "what can you do" in user_input:
        return "I can assist and make your life easier. Ask me anything you need help with, such as arithmetic calculations or any general basic questions about me!Try me!"

    elif "how can you help" in user_input:
        return "I can help you with tasks such as arithmetic calculations and answering general questions."
    elif "your purpose" in user_input or "why were you created" in user_input:
        return "My purpose is to assist and make your life easier. Ask me anything you need help with, such as arithmetic calculations or any general basic questions about me!"
    elif "who created you" in user_input:
        return "I was created by a developer who wanted to build a helpful virtual assistant for arithmetic calculations."
    elif "are you human" in user_input:
        return "No, I'm not human. I'm a computer program here to assist you with arithmetic calculations."

    # Check for matches with predefined patterns
    patterns = [
        (r'hello|hi|hey', ['Hi there!', 'Hello!', 'Hey!']),
        (r'how are you', ['I am good, thank you!', 'Doing well, thanks. How about you?', 'I am just a computer program, but thanks for asking!']),
        #(r'bye|goodbye', ['Goodbye!', 'See you later.', 'Bye!']),
        (r'favorite|what is your favorite|what do you like|like', ['I do not have personal preferences, but I am here to help you!']),
        (r'general questions', ['I am your go-to source for answering any general questions you might have, whether it is about the purpose or capabilities behind my development. Additionally, if you need a hand with arithmetic calculations, count on me to make those numbers dance! Let us chat and explore together. 🚀🔢']),
        # Add more patterns and responses as needed
    ]

    for pattern, responses in patterns:
        if nltk.re.search(pattern, user_input):
            return responses[0]  # Return the first response in the list

    

def is_math_expression(user_input):
    # Check if the input contains mathematical operators
    return any(op in user_input for op in ['+', '-', '*', '/', '%'])

def handle_calculator(user_input):
    try:
        # Evaluate the mathematical expression
        result = eval(user_input)
        return f"The result is: {result}"

    except Exception as e:
        return f"Oops! There was an error. Please enter a valid mathematical expression. Example: x+y, remove the special characters(=,?)."





def chat():
    print(greet())
    
    # Initialize the chatbot with predefined patterns and responses
    patterns = []
    chatbot = Chat(patterns, reflections)
    
    while True:
        user_input = input("You: ").lower()

        # Check if the user wants to end the conversation
        if user_input == 'bye':
            print(farewell())
            break

        # Check for basic questions
        basic_question_response = handle_basic_questions(user_input)
        if basic_question_response:
            print("Bot:", basic_question_response)
            continue

        # Check for calculator input
        if is_math_expression(user_input):
            calculator_response = handle_calculator(user_input)
            print("Bot:", calculator_response)
            continue

        # Fallback response if no specific response is triggered
        print("Bot: Having a bit of trouble with that question! How about we switch gears and dive into some fun arithmetic calculations? Ask me anything, and let's make math more enjoyable! 🧮😊")



if __name__ == "__main__":
    chat()




























'''import nltk
from nltk.chat.util import Chat, reflections

def greet():
    return "Hey there! I'm your helpful chat companion. What can I do for you today? Feel free to share, and let's have a friendly chat!"

def farewell():
    return "See you later! If you ever have more questions or just want to chat, feel free to drop by. I'm here to help and have a friendly conversation whenever you need!"

def handle_basic_questions(user_input):

    if "your name" in user_input:
        return "I'm just a chatbot, so I don't have a personal name."
    elif "your purpose" in user_input or "why are you here" in user_input:
        return "I'm here to assist and chat with you. Ask me anything!"

    elif "capabilities" in user_input or "what can you do" in user_input:
        return "I can answer general questions, chat, provide information and do arithmetic calculations. Try me!"

    elif "how can you help" in user_input:
        return "I can help you with tasks such as arithmetic calculations and answering general questions."
    elif "your purpose" in user_input or "why were you created" in user_input:
        return "My purpose is to assist and make your life easier. Ask me anything you need help with, such as arithmetic calculations or any general basic questions about me!"
    elif "who created you" in user_input:
        return "I was created by a developer who wanted to build a helpful virtual assistant for arithmetic calculations."
    elif "are you human" in user_input:
        return "No, I'm not human. I'm a computer program here to assist you with arithmetic calculations."

    # Check for matches with predefined patterns
    patterns = [
        (r'hello|hi|hey', ['Hi there!', 'Hello!', 'Hey!']),
        (r'how are you', ['I am good, thank you!', 'Doing well, thanks. How about you?', 'I am just a computer program, but thanks for asking!']),
        (r'bye|goodbye', ['Goodbye!', 'See you later.', 'Bye!']),
        (r'favorite|what is your favorite|what do you like|like', ['I do not have personal preferences, but I am here to help you!']),
        (r'general questions', ['I am your go-to source for answering any general questions you might have, whether it is about the purpose or capabilities behind my development. Additionally, if you need a hand with arithmetic calculations, count on me to make those numbers dance! Let us chat and explore together. 🚀🔢']),
        # Add more patterns and responses as needed
    ]

    for pattern, responses in patterns:
        if nltk.re.search(pattern, user_input):
            return responses[0]  # Return the first response in the list

    # No match found for predefined patterns
    return ""

def is_math_expression(user_input):
    # Check if the input contains mathematical operators
    return any(op in user_input for op in ['+', '-', '*', '/', '%'])

def handle_calculator(user_input):
    try:
        # Evaluate the mathematical expression
        result = eval(user_input)
        return f"The result is: {result}"

    except Exception as e:
        return f"Oops! There was an error. Please enter a valid mathematical expression. Example: x+y, remove the special characters."

def chat():
    print(greet())
    
    # Initialize the chatbot with predefined patterns and responses
    patterns = [
        # (r'hello|hi|hey', ['Hi there!', 'Hello!', 'Hey!']),
        # (r'how are you', ['I am good, thank you!', 'Doing well, thanks. How about you?', 'I am just a computer program, but thanks for asking!']),
        # (r'bye|goodbye', ['Goodbye!', 'See you later.', 'Bye!']),
        # (r'favorite|what is your favorite|what do you like|like', ['I do not have personal preferences, but I am here to help you!']),
        # (r'general questions', ['I am your go-to source for answering any general questions you might have, whether it is about the purpose or capabilities behind my development. Additionally, if you need a hand with arithmetic calculations, count on me to make those numbers dance! Let us chat and explore together. 🚀🔢']),
        # Add more patterns and responses as needed
    ]
    chatbot = Chat(patterns, reflections)
    
    while True:
        user_input = input("You: ").lower()

        # Check if the user wants to end the conversation
        if user_input == 'bye':
            print(farewell())
            break

        # Check for basic questions
        basic_question_response = handle_basic_questions(user_input)
        if basic_question_response:
            print("Bot:", basic_question_response)
            continue

        # Check for calculator input
        if is_math_expression(user_input):
            calculator_response = handle_calculator(user_input)
            print("Bot:", calculator_response)
            continue

        # Use the predefined chatbot for general responses
        response = chatbot.respond(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chat()





























'''


'''import nltk
from nltk.chat.util import Chat, reflections

def greet():
    return "Hello! I'm your friendly chatbot. How can I assist you today?"

def farewell():
    return "Goodbye! If you have more questions, feel free to ask later."

def handle_basic_questions(user_input):
    if "your name" in user_input:
        return "I'm just a chatbot, so I don't have a personal name."
    elif "your purpose" in user_input or "why are you here" in user_input:
        return "I'm here to assist and chat with you. Ask me anything!"
    


    elif "capabilities" in user_input or "what can you do" in user_input:
        return "I can answer questions, chat, and provide information. Try me!"
   



    elif "what can you do" in user_input or "your capabilities" in user_input:
        return "I can provide information, answer questions, and assist you with arithmetic calculations. Feel free to ask anything!"
    elif "how can you help" in user_input:
        return "I can help you with tasks such as arithmetic calculations and answering general questions."
    elif "your purpose" in user_input or "why were you created" in user_input:
        return "My purpose is to assist and make your life easier. Ask me anything you need help with!"
    elif "who created you" in user_input:
        return "I was created by a developer who wanted to build a helpful virtual assistant."
    elif "are you human" in user_input:
        return "No, I'm not human. I'm a computer program here to assist you."
    else:
        return "" # No match for basic questions

def is_math_expression(user_input):
    # Check if the input contains mathematical operators
    return any(op in user_input for op in ['+', '-', '*', '/', '%'])

def handle_calculator(user_input):
    try:
        # Evaluate the mathematical expression
        result = eval(user_input)
        return f"The result is: {result}"

    except Exception as e:
        return f"Oops! There was an error. Please enter a valid mathematical expression.Example: x+y,remove the special characters."

def chat():
    print(greet())
    
    # Initialize the chatbot with predefined patterns and responses
    patterns = [
        (r'hello|hi|hey', ['Hi there!', 'Hello!', 'Hey!']),
        (r'how are you', ['I am good, thank you!', 'Doing well, thanks. How about you?','I am just a computer program, but thanks for asking!']),
        (r'bye|goodbye', ['Goodbye!', 'See you later.', 'Bye!']),
        (r'favorite|what is your favorite|what do you like|like', ['I don not have personal preferences, but I am here to help you!']),
        (r'general questions',[you can ask me like how i can help you or about me]),
        # Add more patterns and responses as needed
    ]
    chatbot = Chat(patterns, reflections)
    
    while True:
        user_input = input("You: ").lower()

        # Check if the user wants to end the conversation
        if user_input == 'bye':
            print(farewell())
            break

        # Check for basic questions
        basic_question_response = handle_basic_questions(user_input)
        if basic_question_response:
            print("Bot:", basic_question_response)
            continue

        # Check for calculator input
        if is_math_expression(user_input):
            calculator_response = handle_calculator(user_input)
            print("Bot:", calculator_response)
            continue

        # Use the predefined chatbot for general responses
        response = chatbot.respond(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chat()


'''




