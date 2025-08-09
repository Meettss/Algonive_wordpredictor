# Algonive Projects

This repository contains multiple Python projects developed during my internship at Algonive, demonstrating skills in natural language processing, machine learning, and chatbot development.

---
## 1 Word Predictor
A Python-based predictive text generator built during my internship at **Algonive**. It uses basic NLP techniques like n-grams to suggest the next word in a sentence, similar to autocomplete in messaging apps.

### Features

- **Word Prediction**: Suggests the next word based on user input.
- **Context Awareness**: Uses previously typed words to improve prediction accuracy.
- **Customizable Dictionary**: Users can add frequently used words to improve relevance.
- **Basic Machine Learning**: Uses an n-gram model (or Markov Chain) for text prediction.

### Tools & Libraries

- **Python 3.x** – Core programming language
- **NLTK (Natural Language Toolkit)** – Used for generating n-grams and text processing
- **Collections Module** – Used for efficient data structures like `defaultdict` and `Counter`
- **VS Code** – Code editor
- **Git & GitHub** – Version control and project hosting

### Project Structure
```
Algonive/
├── Word_predictor.py # Main script with the predictive text generator
├── .gitignore # Specifies files/folders to ignore in Git
├── README.md # Project overview and documentation
```

**Clone the repository**
   ``` bash
   git clone https://github.com/Meettss/Algonive.git
   cd Algonive

## 2. AI Customer Support Chatbot

A Python chatbot that uses fuzzy string matching to understand user queries and provide relevant answers from a predefined FAQ. It also handles greetings, small talk, and polite responses for a natural conversational experience.

### Features

- FAQ matching with `rapidfuzz` fuzzy matching
- Multiple answer variations for natural responses
- Greeting and small talk support
- Easy to extend FAQ database
- Simple command-line interface with exit option

### Tools & Libraries

- Python 3.x
- rapidfuzz (for fuzzy string matching)
- VS Code
- Git & GitHub

---

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/Meettss/Algonive.git
cd Algonive
