import random
from nltk.util import ngrams
from collections import defaultdict, Counter

# Sentences the Bot Learns From
text = """ hello how are you
           hello how is your day
           are you doing well
           how are you today
           what are you doing
           i am doing good
           i hope you are fine
           do you need any help
           what is your name
           my name is 
           where are you from
           i am from 
           what time is it
           can you help me
           i love programming
           you are very smart
           let us go for a walk
           it's a beautiful day
           how can i help you
           are you coming today
           yes i will be there
           no i am busy today
           i have some work
           thank you so much
           you are welcome
           please wait a moment
           how old are you
           i am eighteen years old
           do you like music
           yes i love music
           what are you thinking
           nothing just chilling
           that sounds great
           okay see you later
           bye take care """

# Tokenizing - breaking the full text into smaller tokens
tokens = text.lower().split()
bigrams = list(ngrams(tokens, 2))
trigrams = list(ngrams(tokens, 3))

# Prediction Models - models that will help the program to predict the next word 
bigram_predictor = defaultdict(Counter)
trigram_predictor = defaultdict(Counter)

for first_word, second_word in bigrams:
    bigram_predictor[first_word][second_word] += 1

for word1, word2, word3 in trigrams:
    trigram_predictor[(word1, word2)][word3] += 1

# Prediction Function 
def predict(user):
    words = user.lower().split()

    # Trigram Prediction
    if len(words) >= 2:
        prev_word1, prev_word2 = words[-2], words[-1]
        if (prev_word1, prev_word2) in trigram_predictor:
            return [next_word for next_word, count in trigram_predictor[(prev_word1, prev_word2)].most_common(5)]

    # Bigram Prediction
    if len(words) >= 1:
        last_word = words[-1]
        if last_word in bigram_predictor:
            return [next_word for next_word, count in bigram_predictor[last_word].most_common(5)]

    # No Predictions
    return []

# Interaction with User 
print("Type something (or type 'exit' to quit) : ")
while True:
    user = input("You : ")
    if user.lower() == "exit":
        print("Goodbye!")
        break

    suggestions = predict(user)

    if suggestions:
        print("Predictions : ")
        for i, word in enumerate(suggestions, start=1):
            print(f"{i}. {user} {word}")
    else:
        print("No suggestions found. Try something else!")

        

















        