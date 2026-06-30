from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarilty

class SimilarityMatcher:
    def init(self, questions):
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(
            questions
        )
    def find_best_match(self, query):
        query_vector= self.vectorizer.transform([query])
        similarities= cosine_similarilty(
            query_vector,
            self.question_vectors
        )
        best_index = similarities.argmax()
        best_score= similarities[0][best_index]
        return best_index, best_score