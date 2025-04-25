from typing import List

# Define categories and associated keywords
CATEGORIES = {
    "Product Quality": ["product", "quality", "great", "good", "bad", "love", "hate", "broke", "defective"],
    "Customer Service": ["service", "support", "help", "staff", "representative", "agent", "response"],
    "User Experience": ["experience", "interface", "easy", "difficult", "intuitive", "confusing", "simple"],
    "Price": ["price", "cost", "expensive", "cheap", "worth", "value", "money"],
    "Delivery": ["delivery", "shipping", "arrived", "late", "package", "time"]
}

def categorize_feedback(feedback_text: str, keywords: List[str] = None) -> List[str]:
    """Categorize feedback based on keywords or text content."""
    text = feedback_text.lower()

    # If keywords are not provided, use the entire text
    words_to_check = keywords if keywords else text.split()

    categories = []
    for category, category_keywords in CATEGORIES.items():
        # Check if any category keyword is in the feedback text or extracted keywords
        if any(keyword in text for keyword in category_keywords) or \
           any(word in category_keywords for word in words_to_check):
            categories.append(category)

    # If no categories found, mark as "General"
    if not categories:
        categories = ["General"]

    return categories
