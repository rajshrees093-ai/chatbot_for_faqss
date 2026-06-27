FAQ Chatbot
NLP-Powered Frequently Asked Questions Assistant
Task 2 — AIML Project    JavaScript + TF-IDF + Cosine Similarity


📋 Project Overview
This project implements an intelligent FAQ chatbot using Natural Language Processing (NLP) techniques. The chatbot matches user questions against a curated knowledge base of 20 FAQs across 5 topic categories, returning the most semantically relevant answer using TF-IDF vectorization and cosine similarity scoring.

✨ Features
•	NLP pipeline: tokenization → stop-word removal → stemming → TF-IDF → cosine similarity
•	20 FAQs across 5 categories: Shipping, Returns, Accounts, Payments, Products
•	Match confidence score displayed as a color-coded progress bar (green / amber / red)
•	Related question suggestions (2nd and 3rd best matches shown as clickable chips)
•	Topic shortcut chips for quick category browsing
•	Real-time chat UI with typing indicator and timestamped messages
•	Graceful fallback response for low-confidence or unrecognized queries
•	Fully client-side — no server, no external ML libraries required

🛠️ Technology Stack
Component	Technology	Purpose
Frontend	HTML5 / CSS3 / Vanilla JS	Chat UI, event handling
NLP Engine	Custom JavaScript	TF-IDF + cosine similarity
Text Processing	JS (no libraries)	Tokenize, stop-word, stem
Similarity	Cosine Similarity	Vector-space matching
Weighting	TF-IDF	Rare term boosting
Icons	Tabler Icons (CDN)	UI iconography

🔬 NLP Pipeline
The matching engine runs the following stages for every user query:

Stage 1 — Tokenization
Raw text is lowercased, punctuation is stripped, and the result is split on whitespace into individual word tokens.
"How long does FREE shipping take?"
→ ["how", "long", "does", "free", "shipping", "take"]

Stage 2 — Stop-word Removal
A set of ~40 high-frequency English words (the, a, is, do, how, what, etc.) are filtered out. These carry no discriminative semantic weight.
→ ["long", "free", "shipping", "take"]

Stage 3 — Suffix Stemming
A lightweight rule-based stemmer strips common suffixes (-ing, -ed, -s, -ly) to normalize word forms so that "shipped", "shipping", and "ships" all map to the same root token.
→ ["long", "free", "ship", "take"]

Stage 4 — TF-IDF Vectorization
Each document (FAQ question + answer) and the user query are converted into sparse numeric vectors using Term Frequency–Inverse Document Frequency weighting:
•	TF (Term Frequency): how often a term appears in this document
•	IDF (Inverse Document Frequency): log((N+1)/(df+1)) + 1, where N = total docs, df = docs containing term
•	Words appearing in many FAQs (common) receive low IDF weight; rare/specific words receive high weight

Stage 5 — Cosine Similarity
The angle between the query vector and each FAQ vector is computed. A score of 1.0 means identical direction (perfect match); 0.0 means orthogonal (no overlap). An overlap bonus (+0.1 per shared token) is added to the raw query–question match to boost direct question paraphrases.
similarity = (q · d) / (‖q‖ × ‖d‖)

Stage 6 — Ranking & Response
All FAQs are ranked by their similarity score. The top result's answer is displayed. The 2nd and 3rd results are offered as "Did you also mean?" suggestion chips. Queries scoring below 0.05 trigger a fallback message.

Confidence Score Display
The match confidence is shown as: min(100, score × 150)%. This maps typical cosine similarity ranges (0.2–0.7) to a more intuitive 30–100% display range. Color coding: green (>60%), amber (35–60%), red (<35%).

📚 FAQ Knowledge Base
20 FAQs are pre-loaded across 5 topic categories (4 per category):

Category	Sample Question	Count
Shipping & Delivery	How long does shipping take?	5 FAQs
Returns & Refunds	What is your return policy?	5 FAQs
Account & Orders	How do I create an account?	5 FAQs
Payments	What payment methods do you accept?	5 FAQs
Products	Are your products eco-friendly?	5 FAQs

💬 Chat UI Features
•	Bot avatar with animated typing indicator (3-dot bounce animation)
•	Message timestamps shown under each bubble
•	User messages: right-aligned with accent-blue background
•	Bot messages: left-aligned with border card, confidence bar, and suggestion chips
•	Topic chips in header: clicking sends a sample question from that category
•	Auto-resizing textarea (up to 3 lines) with Enter-to-send (Shift+Enter for newline)
•	Send button disabled when input is empty
•	Smooth scroll to latest message on each reply

📁 Project Structure
faq-chatbot/
├── index.html          # Single-file application (UI + NLP + data)
├── README.md           # This document
└── assets/             # (optional) icons, screenshots

The entire application is self-contained in a single HTML file. The NLP engine, FAQ data, and chat UI are all implemented in vanilla JavaScript — no build step, no package manager, no external ML dependencies.

🚀 How to Run
Option A — Open directly in browser
1.	Download or copy the HTML artifact code
2.	Save as index.html
3.	Open in any modern browser (Chrome, Firefox, Edge, Safari)
4.	No internet connection needed (except for Tabler Icons CDN)

Option B — Serve locally (recommended)
# Python
python -m http.server 8080

# Node.js
npx serve .

# Then visit: http://localhost:8080

🧪 Example Queries to Try
These queries demonstrate paraphrase handling via stemming and TF-IDF:
The chatbot should match all of these even though the phrasing differs from the stored FAQ questions.

User Query	Matches FAQ About
"how fast is delivery?"	Shipping time (stemming: deliver ≈ ship)
"forgot my password"	Password reset (direct token match)
"can I send stuff back?"	Return policy
"do you take PayPal?"	Payment methods
"is there a rewards program?"	Loyalty program
"damaged product received"	Damaged item policy

⚠️ Limitations & Future Improvements
Current Limitations
•	Stemming is rule-based (suffix stripping) — not linguistically accurate for all words
•	No semantic understanding (synonyms like "fast" ≠ "quick" unless both appear in FAQs)
•	Fixed knowledge base — FAQs must be manually added to the JS array
•	No conversation memory — each query is matched independently

Potential Improvements
•	Replace rule-based stemming with WordNet lemmatization (via NLTK in Python)
•	Use pre-trained word embeddings (Word2Vec, GloVe) for semantic similarity
•	Add a Python/Flask backend for server-side NLP with spaCy
•	Implement BM25 ranking (state-of-the-art lexical retrieval)
•	Connect to a real product database for dynamic FAQ generation
•	Add multi-turn conversation context tracking

🐍 Python/NLTK Equivalent
The same pipeline can be implemented in Python with NLTK and scikit-learn:

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess(text):
    tokens = word_tokenize(text.lower())
    stop = set(stopwords.words('english'))
    ps = PorterStemmer()
    return ' '.join(ps.stem(t) for t in tokens if t.isalpha() and t not in stop)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([preprocess(q) for q in faq_questions])

def get_answer(user_query):
    q_vec = vectorizer.transform([preprocess(user_query)])
    scores = cosine_similarity(q_vec, tfidf_matrix).flatten()
    best_idx = scores.argmax()
    return faq_answers[best_idx], scores[best_idx]

Task 2 — FAQ Chatbot   |   AIML Project   |   NLP: TF-IDF + Cosine Similarity
