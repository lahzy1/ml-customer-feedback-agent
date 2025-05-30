def analyze_sentiment(text: str) -> str:
    """
    Analyze sentiment of a text and return 'positive', 'negative', or 'neutral'.
    This is a simple rule-based approach. In production, you would use a more sophisticated model.
    """
    # List of positive and negative words
    positive_words = ["good", "great", "excellent", "love", "like", "happy", "satisfied", "amazing", "awesome", "fantastic"]
    negative_words = ["bad", "poor", "terrible", "hate", "dislike", "unhappy", "disappointed", "awful", "horrible", "terrible"]

    # Convert to lowercase for case-insensitive matching
    text_lower = text.lower()

    # Count positive and negative words
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)

    # Determine sentiment
    if positive_count > negative_count:
        return "positive"
    elif negative_count > positive_count:
        return "negative"
    else:
        return "neutral"


# from typing import Literal, Union
# from autogen import AssistantAgent
# from feedback_agent.config import LLM_CONFIG
#
# SENTIMENT_VALUES = {"positive", "negative", "neutral"}
#
# def analyze_sentiment(text: str) -> Union[Literal["positive"], Literal["negative"], Literal["neutral"]]:
#     agent = AssistantAgent(
#         name="Sentiment Analysis Agent",
#         system_message="You are a helpful AI assistant. "
#                       "You can analyze the sentiment of a customer feedback. "
#                       "Given a customer feedback, you can use the sentiment_analysis tool to analyze the sentiment. "
#                       "You will provide sentiment analysis result in the following format: '[sentiment]'. "
#                       "Example result: 'positive'. "
#                       "Example of invalid result: 'sentiment is positive'."
#                       "Sentiment can be 'positive', 'negative', or 'neutral'. "
#                       "Don't include any other text in your response."
#                       "Return 'TERMINATE' when the task is done.",
#         llm_config=LLM_CONFIG,
#     )
#     reply = agent.generate_reply(
#         messages=[
#             {"role": "user", "content": f'analyze the sentiment of the following feedback: {text}'}
#         ],
#     )
#
#     if not reply:
#         raise ValueError("No reply found")
#
#     reply_value = ""
#     if isinstance(reply, dict):
#         reply_content = reply["content"]
#         if reply_content:
#             reply_value = reply_content
#         else:
#             raise ValueError("No content found in the reply")
#     else:
#         reply_value = reply
#
#     reply_values = reply_value.splitlines()
#     if len(reply_values) != 1:
#         filtered_lines = list(filter(lambda x: SENTIMENT_VALUES.intersection(set(x.lower().split())), reply_values))
#         reply_value = filtered_lines[0] if filtered_lines else ""
#
#     reply_value = reply_value.replace("[", "").replace("]", "").replace(" ", "").strip()
#
#     if reply_value not in SENTIMENT_VALUES:
#         raise ValueError(f"Invalid sentiment value: {reply_value}")
#
#     return reply_value
