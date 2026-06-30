import json

from chatbot.preprocess import preprocess_text
from chatbot.similarity import SimilarityMatcher

class FAQChatbot:
    def init(self, faq_file):
        with open(faq_file, "r") as file:
            self.faqs=json.load(file)
        self.questions=[
            preprocess_text(
                faq["question"]
            )
            for faq in self.faqs
        ]
        self.matcher=SimilarityMatcher(self.questions)
    def get_response(self, user_query):
        processed_query= preprocess_text(user_query)
        index, score= self.matcher.find_best_match(processed_query)
        if score < 0.20:
            return("Sorry, I could not find a relevant answer.")
        return self.faqs[index]["answer"]    