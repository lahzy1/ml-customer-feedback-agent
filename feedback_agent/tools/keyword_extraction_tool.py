from typing import List
from collections import Counter
import string

def extract_keywords(feedback_text: str) -> List[str]:
    """Extract important keywords from feedback text using a simple frequency-based approach."""
    # Convert to lowercase and remove punctuation
    text = feedback_text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split into words
    words = text.split()

    # Remove common stopwords
    stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you",
                 "your", "yours", "yourself", "yourselves", "he", "him", "his",
                 "himself", "she", "her", "hers", "herself", "it", "its", "itself",
                 "they", "them", "their", "theirs", "themselves", "what", "which",
                 "who", "whom", "this", "that", "these", "those", "am", "is", "are",
                 "was", "were", "be", "been", "being", "have", "has", "had", "having",
                 "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if",
                 "or", "because", "as", "until", "while", "of", "at", "by", "for",
                 "with", "about", "against", "between", "into", "through", "during",
                 "before", "after", "above", "below", "to", "from", "up", "down",
                 "in", "out", "on", "off", "over", "under", "again", "further",
                 "then", "once", "here", "there", "when", "where", "why", "how",
                 "all", "any", "both", "each", "few", "more", "most", "other",
                 "some", "such", "no", "nor", "not", "only", "own", "same", "so",
                 "than", "too", "very", "s", "t", "can", "will", "just", "don",
                 "should", "now", "had"]

    filtered_words = [word for word in words if word not in stopwords and len(word) > 2]

    # Get most common words
    word_counts = Counter(filtered_words)

    # Return top keywords (up to 5)
    keywords = [word for word, count in word_counts.most_common(5)]
    return keywords or ["no keywords found"]
