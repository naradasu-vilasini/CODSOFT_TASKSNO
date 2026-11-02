from datetime import datetime


def has_word(words, options):
    # checks if any word from options is in the user's words
    return any(w in words for w in options)


def get_response(user_input):
    text = user_input.lower().strip()
    words = text.split()

    if text in ["bye", "exit", "quit", "goodbye"]:
        return "Goodbye! Have a nice day."

    elif has_word(words, ["hi", "hello", "hey", "hii"]):
        return "Hello! How can I help you today?"

    elif "how are you" in text or "how r u" in text or "how ru" in text or "how are u" in text:
        return "I am fine, thank you! How are you?"

    elif has_word(words, ["fine", "good", "great", "ok", "okay", "nice", "happy"]):
        return "That is great to hear! 😊 What would you like to talk about?"

    elif has_word(words, ["sad", "bad", "tired", "angry"]):
        return "I am sorry to hear that. I hope your day gets better soon."

    elif "your name" in text or "who are you" in text:
        return "I am a simple chatbot made with Python."

    elif "who made you" in text or "who created you" in text:
        return "I was created by Vilasini as part of the CodSoft AI internship."

    elif "what can you do" in text or "help" in text:
        return "I can chat with you. Try: hi, how are you, your name, time, date, joke, thank you, bye."

    elif "time" in text:
        return "The time now is " + datetime.now().strftime("%I:%M %p")

    elif "date" in text or "today" in text:
        return "Today's date is " + datetime.now().strftime("%d %B %Y")

    elif "joke" in text:
        return "Why did the computer go to the doctor? Because it had a virus!"

    elif "thank" in text:
        return "You are welcome!"

    else:
        return "Sorry, I did not understand. Type 'help' to see what I can do."


print("Chatbot: Hello! I am your chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ")
    reply = get_response(user)
    print("Chatbot:", reply)
    if user.lower().strip() in ["bye", "exit", "quit", "goodbye"]:
        break