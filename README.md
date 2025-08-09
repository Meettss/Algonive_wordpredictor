# Word Predictor
A Python-based predictive text generator built during my internship at **Algonive**. It uses basic NLP techniques like n-grams to suggest the next word in a sentence, similar to autocomplete in messaging apps.

## Features

- **Word Prediction**: Suggests the next word based on user input.
- **Context Awareness**: Uses previously typed words to improve prediction accuracy.
- **Customizable Dictionary**: Users can add frequently used words to improve relevance.
- **Basic Machine Learning**: Uses an n-gram model (or Markov Chain) for text prediction.

## Tools & Libraries

- **Python 3.x** – Core programming language
- **NLTK (Natural Language Toolkit)** – Used for generating n-grams and text processing
- **Collections Module** – Used for efficient data structures like `defaultdict` and `Counter`
- **VS Code** – Code editor
- **Git & GitHub** – Version control and project hosting

## Project Structure
```
Algonive/
├── Word_predictor.py # Main script with the predictive text generator
├── .gitignore # Specifies files/folders to ignore in Git
├── README.md # Project overview and documentation
```

**Clone the repository**
   ```bash
   git clone https://github.com/Meettss/Algonive.git
   cd Algonive