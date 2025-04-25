from typing import Dict, List, Any, Union
import json

def generate_actions(insights: Union[Dict[str, Any], str]) -> List[Dict[str, str]]:
    """Generate recommended actions based on feedback insights."""
    # Parse string input if necessary
    if isinstance(insights, str):
        insights = json.loads(insights)

    actions = []

    # Check for negative sentiment
    sentiment_dist = insights.get("sentiment_distribution", {})
    if sentiment_dist.get("negative", 0) > sentiment_dist.get("positive", 0):
        actions.append({
            "action_type": "alert",
            "target": "management",
            "priority": "high",
            "message": "Critical: Negative feedback exceeds positive feedback"
        })

    # Generate category-specific actions
    for category in insights.get("category_sentiment", {}):
        cat_sentiments = insights["category_sentiment"][category]

        # If negative sentiment is high for a category
        if cat_sentiments.get("negative", 0) > cat_sentiments.get("positive", 0):
            actions.append({
                "action_type": "improvement",
                "target": "product_team",
                "area": category,
                "message": f"Improvement needed in {category} based on customer feedback"
            })

        # If positive sentiment is high for a category
        if cat_sentiments.get("positive", 0) > cat_sentiments.get("negative", 0) * 2:
            actions.append({
                "action_type": "highlight",
                "target": "marketing",
                "area": category,
                "message": f"Leverage positive feedback about {category} in marketing"
            })

    return actions
