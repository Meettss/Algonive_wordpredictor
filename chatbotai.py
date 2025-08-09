import time
import random
from rapidfuzz import fuzz

# ✅ Expanded FAQ responses (multiple variations for naturalness)
faq_responses = {
    # About Chatbot
    "what is an ai customer support chatbot": 
    ["An AI chatbot simulates human conversation to help customers in real time.",
        "It's a virtual assistant that talks with you and answers questions instantly.",
        "Think of it as a smart helper that understands your queries and replies instantly."],
    "what industries use customer support chatbots": 
    ["They’re common in e-commerce, banking, healthcare, telecom, and travel.",
    "Industries like retail, finance, healthcare, and travel use them heavily.",
    "From online shops to airlines, many industries rely on them for quick help."],

    # Customer Support
    "do you have a refund policy":
     [ "Yes, we offer refunds within 7–30 days depending on the product.",
    "Refunds are available for most purchases within 30 days.",
    "You can request a refund through our support portal within the policy period."],
    "how can i raise a complaint":
    ["You can file a complaint through our support form.",
    "We take complaints seriously; let me know the details so we can resolve them."],
    "what are your services": 
    ["We help with orders, payments, appointments, and general inquiries.",
    "Our services include customer support, tracking orders, and handling complaints.",
    "We assist with product info, order issues, and technical questions."],
    "can you reset my password":
    ["I can’t do that directly, but you can reset it on the login page via 'Forgot Password'.",
    "Please click 'Forgot Password' on the login page to reset it securely.",
    "For your safety, password resets happen only through our secure portal."],
    "can you track my order": [
    "I can’t track it directly, but you can check your order status in the 'My Orders' section of our website.",
    "Sorry, I can’t access tracking info, but you can find it by logging into your account and opening 'Order History'.",
    "I can’t track orders myself, but you can check the status on our app under 'Orders'."],

    # Small Talk
    "how are you": [
        "I'm just a bot, but I’m doing great! How can I help you? 😊",
        "Feeling powered up and ready to assist! ⚡",
        "Always happy to chat! What’s on your mind?" ],
    "who made you": [
        "I was developed to improve customer service using AI! 🤖",
        "I’m a creation of tech enthusiasts who love helping people.",
        "I’m a product of coding, coffee, and a little magic ✨." ],
    "tell me a joke": [
        "Why don’t skeletons fight each other? They don’t have the guts. 💀",
        "What do you call fake spaghetti? An *impasta*! 🍝",
        "Why was the math book sad? It had too many problems. 📚" ],
    "what's your name": [
        "I’m your friendly support bot. No name yet, but you can give me one! 🤖",
        "I’m just called Support Bot for now, but I’m open to suggestions.",
        "People call me Support Buddy — nice to meet you!" ],

    # Politeness 
    "thank you": [
        "You're very welcome! 🙌",
        "No problem at all! 😊",
        "Always happy to help! 🚀" ],
    "thanks": [
        "Anytime! 🙌",
        "Glad I could help! 😊",
        "You’re welcome! 🚀" ],
    "bye": [
        "Goodbye! 👋 Have an amazing day!",
        "See you later! Take care. 🌟",
        "Bye! Come back if you need anything. 🙏" ],
}

# Fuzzy matching
def match_query(user_input, faq_responses, threshold=70):
    best_match = None
    highest_score = 0
    for question in faq_responses.keys():
        score = fuzz.partial_ratio(user_input.lower(), question.lower())
        if score > highest_score:
            highest_score = score
            best_match = question
    return best_match if highest_score >= threshold else None

# Chatbot Function
def chatbot():
    print(" Welcome to the AI 🤖 Customer Support Chatbot")
    print("Type 'exit' to end the chat.")
    print("-" * 50)

    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
    greeting_responses = [
        "Hello! 👋 How can I assist you today?",
        "Hi there! 😊 What can I help you with?",
        "Hey! 🚀 Ready to help you!",
        "Good to see you! How can I support you today?"
    ]

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Bot: Thanks for chatting with me! 👋")
            break

        # Greeting detection
        if any(user_input.lower().startswith(greet) for greet in greetings):
            print("Bot:", random.choice(greeting_responses))
            continue

        # Match FAQs with fuzzy matching
        matched_question = match_query(user_input, faq_responses)
        if matched_question:
            responses = faq_responses[matched_question]
            if isinstance(responses, list):
                print("Bot:", random.choice(responses))
            else:
                print("Bot:", responses)
            continue

        # Fallback for unmatched queries
        print("Bot: 🤔 Hmm… I’m not sure I understand that. Could you rephrase?")

# ✅ Run chatbot
if __name__ == "__main__":
    chatbot() 