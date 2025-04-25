from typing import List, Dict, Any, Union
import json

def generate_insights(analyzed_feedback: Union[List[Dict[str, Any]], str]) -> Dict[str, Any]:
    """
    Generate insights from analyzed feedback.
    Input can be a list of dictionaries or a JSON string.
    """
    # Parse string input if necessary
    if isinstance(analyzed_feedback, str):
        analyzed_feedback = json.loads(analyzed_feedback)

    # Count sentiments
    sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}
    category_counts = {}
    category_sentiments = {}

    # Process each feedback item
    for item in analyzed_feedback:
        # Count sentiment
        sentiment = item.get("sentiment", "neutral").lower()
        sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1

        # Count categories
        category = item.get("category", "General")

        # Update category count
        category_counts[category] = category_counts.get(category, 0) + 1

        # Update category sentiment
        if category not in category_sentiments:
            category_sentiments[category] = {"positive": 0, "negative": 0, "neutral": 0}
        category_sentiments[category][sentiment] += 1

    # Calculate top categories
    sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
    top_categories = [{"name": cat, "count": count} for cat, count in sorted_categories[:3]]

    # Generate insights dict
    insights = {
        "total_feedback": len(analyzed_feedback),
        "sentiment_distribution": sentiment_counts,
        "top_categories": top_categories,
        "category_sentiment": category_sentiments,
        "summary": f"Analyzed {len(analyzed_feedback)} feedback items. Most were {max(sentiment_counts, key=sentiment_counts.get)}."
    }

    return insights
