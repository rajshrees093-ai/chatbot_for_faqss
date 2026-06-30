# FAQ Chatbot using NLP and Flask

## Project Overview

This project is an intelligent FAQ Chatbot developed using Python, Flask, NLTK, and Scikit-learn. The chatbot automatically matches user questions with the most relevant Frequently Asked Question (FAQ) using Natural Language Processing (NLP) techniques and Cosine Similarity.

Instead of relying on exact keyword matches, the chatbot understands the meaning of user queries through text preprocessing and vectorization, providing accurate and efficient responses.

---

## Features

* Interactive chatbot interface
* FAQ dataset management using JSON
* Text preprocessing with NLTK
* Tokenization and stopword removal
* TF-IDF Vectorization
* Cosine Similarity-based question matching
* Confidence score thresholding
* Flask backend API
* Responsive web-based chat UI
* Easy to customize and extend

---

## Tech Stack

### Backend

* Python
* Flask

### NLP & Machine Learning

* NLTK
* Scikit-learn
* NumPy

### Frontend

* HTML
* CSS
* JavaScript

### Data Storage

* JSON

---

## Project Structure

```text
faq-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── faqs.json
│
├── chatbot/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── similarity.py
│   └── chatbot_engine.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── images/
│
├── screenshots/
│
└── .gitignore
```

---

## Working Principle

### Step 1: User Query

The user enters a question through the chatbot interface.

Example:

```
How do I get a refund?
```

### Step 2: Text Preprocessing

The query is cleaned using NLP techniques:

* Convert text to lowercase
* Tokenization
* Remove punctuation
* Remove stopwords

Example:

```
How do I get a refund?
```

becomes

```
refund
```

### Step 3: TF-IDF Vectorization

The processed query and FAQ questions are transformed into numerical vectors using TF-IDF (Term Frequency–Inverse Document Frequency).

### Step 4: Similarity Matching

Cosine Similarity is calculated between the user query vector and all FAQ vectors.

The FAQ with the highest similarity score is selected.

### Step 5: Response Generation

The answer corresponding to the most similar FAQ is returned to the user.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/faq-chatbot.git

cd faq-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Sample FAQs

```json
[
  {
    "question": "What is your return policy?",
    "answer": "You can return products within 30 days."
  },
  {
    "question": "How can I track my order?",
    "answer": "Use the tracking number sent to your email."
  }
]
```

---

## Future Enhancements

* Intent Classification using Machine Learning
* Transformer-based NLP models
* Speech-to-Text support
* Database integration (MongoDB/MySQL)
* Multi-language support
* User authentication
* Chat history storage
* Integration with OpenAI APIs

---

## Learning Outcomes

Through this project, the following concepts were explored:

* Natural Language Processing (NLP)
* Tokenization
* Stopword Removal
* Text Vectorization
* TF-IDF
* Cosine Similarity
* Flask Web Development
* API Development
* Frontend-Backend Integration

---

## Conclusion

The FAQ Chatbot demonstrates how Natural Language Processing can be used to automate responses to frequently asked questions. By leveraging TF-IDF Vectorization and Cosine Similarity, the chatbot efficiently identifies the most relevant FAQ and delivers accurate responses through an intuitive web interface.
