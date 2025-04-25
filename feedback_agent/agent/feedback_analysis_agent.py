# feedback_agent/agent/feedback_analysis_agent.py
from autogen import ConversableAgent
from feedback_agent.tools.feedback_reader_tool import query_feedback
from feedback_agent.tools.sentiment_analysis_tool import analyze_sentiment
from feedback_agent.tools.categorization_tool import categorize_feedback
from feedback_agent.tools.keyword_extraction_tool import extract_keywords
# from feedback_agent.tools.insights_tool import generate_insights
# from feedback_agent.tools.action_tool import generate_actions
from feedback_agent.config import LLM_CONFIG


def create_feedback_analysis_agent() -> ConversableAgent:
    # define the agent
    agent = ConversableAgent(
        name="Feedback Analysis Agent",
        system_message="You are a helpful AI assistant specialized in customer feedback analysis. "
                      "Follow these steps IN ORDER: "
                      "1. Read feedback with feedback_reader tool. "
                      "2. Analyze each item (sentiment, keywords, categories). "
                      "3. Create a list of structured feedback data in JSON format. "
                      "4. Present a final report with all findings and recommended actions. "
                      # "4. MUST call generate_insights with the structured data. "
                      # "5. MUST call generate_actions with the insights output. "
                      # "6. Present a final report with all findings and recommended actions. "
                      "Return 'TERMINATE' when the task is complete.",
        llm_config=LLM_CONFIG,
    )

    # Register tools
    agent.register_for_llm(name="feedback_reader", description="Read customer feedback")(query_feedback)
    agent.register_for_llm(name="sentiment_analysis", description="Analyze sentiment (positive, negative, neutral)")(analyze_sentiment)
    agent.register_for_llm(name="keyword_extraction", description="Extract keywords from text")(extract_keywords)
    agent.register_for_llm(name="categorization", description="Categorize into themes")(categorize_feedback)
    # agent.register_for_llm(name="generate_insights", description="Generate insights from analyzed feedback")(generate_insights)
    # agent.register_for_llm(name="generate_actions", description="Generate recommended actions based on insights")(generate_actions)

    return agent


def create_user_proxy():
    user_proxy = ConversableAgent(
        name="User",
        llm_config=False,
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
        human_input_mode="NEVER",
    )
    user_proxy.register_for_execution(name="feedback_reader")(query_feedback)
    user_proxy.register_for_execution(name="sentiment_analysis")(analyze_sentiment)
    user_proxy.register_for_execution(name="keyword_extraction")(extract_keywords)
    user_proxy.register_for_execution(name="categorization")(categorize_feedback)
    # user_proxy.register_for_execution(name="generate_insights")(generate_insights)
    # user_proxy.register_for_execution(name="generate_actions")(generate_actions)
    return user_proxy


def main():
    user_proxy = create_user_proxy()
    feedback_analysis_agent = create_feedback_analysis_agent()
    user_proxy.initiate_chat(
        feedback_analysis_agent,
        message="""
                Perform a complete analysis of customer feedback following these steps:
                
                1. Read all customer feedback using the feedback_reader tool.
                2. For each feedback item:
                   - Analyze sentiment using sentiment_analysis tool
                   - Extract keywords using keyword_extraction tool
                   - Categorize using categorization tool and show which category it belongs to
                3. Combine all analysis into a structured format for each feedback item
                4. Present a final report with all findings and recommendations
                """
                # 4. Generate overall insights using generate_insights tool
                # 5. Recommend actions using generate_actions tool
                # 6. Present a final report with all findings and recommendations
    )


if __name__ == "__main__":
    main()


# from autogen import ConversableAgent
# from feedback_agent.tools.feedback_reader_tool import query_feedback
# from feedback_agent.tools.sentiment_analysis_tool import analyze_sentiment
# from feedback_agent.tools.categorization_tool import categorize_feedback
# from feedback_agent.tools.keyword_extraction_tool import extract_keywords
# from feedback_agent.config import LLM_CONFIG
#
# def create_feedback_analysis_agent() -> ConversableAgent:
#     # define the agent
#     agent = ConversableAgent(
#         name="Feedback Analysis Agent",
#         system_message="You are a helpful AI assistant. "
#                       "You can perform sentiment analysis on customer feedback. "
#                       "You can read customer feedback using the feedback_reader tool. It will return a list of feedback, that consists of id, text, and source. "
#                       "Given a customer feedback, you can use the sentiment_analysis tool to analyze the sentiment. "
#                       # "You can also categorize the feedback into themes using the categorization tool. "
#                       # "You can also extract keywords from the feedback using the keyword_extraction tool. "
#                       "Don't include any other text in your response. "
#                       "Return 'TERMINATE' when the task is done.",
#         llm_config=LLM_CONFIG,
#     )
#
#     # add the tools to the agent
#     agent.register_for_llm(name="feedback_reader", description="Read customer feedback")(query_feedback)
#     agent.register_for_llm(name="sentiment_analysis", description="Analyze the sentiment of a customer feedback")(analyze_sentiment)
#     # agent.register_for_llm(name="categorization", description="Categorize feedback into themes")(categorize_feedback)
#     # agent.register_for_llm(name="keyword_extraction", description="Extract keywords from a customer feedback")(extract_keywords)
#
#     return agent
#
# def create_user_proxy():
#     user_proxy = ConversableAgent(
#         name="User",
#         llm_config=False,
#         is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
#         human_input_mode="NEVER",
#     )
#     user_proxy.register_for_execution(name="feedback_reader")(query_feedback)
#     user_proxy.register_for_execution(name="sentiment_analysis")(analyze_sentiment)
#     # user_proxy.register_for_execution(name="categorization")(categorize_feedback)
#     # user_proxy.register_for_execution(name="keyword_extraction")(extract_keywords)
#     return user_proxy
#
#
# def main():
#     user_proxy = create_user_proxy()
#     feedback_analysis_agent = create_feedback_analysis_agent()
#     user_proxy.initiate_chat(
#         feedback_analysis_agent,
#         message="""
#                 1. Read feedback from the feedback store, using the feedback_reader tool.
#                 2. For each feedback item, analyze the sentiment using the sentiment_analysis tool.
#                 3. Create a JSON object that contains the feedback id and the analyzed sentiment.
#                 Example:
#                 [
#                     {"id": "1", "sentiment": "positive"},
#                     {"id": "2", "sentiment": "negative"},
#                     {"id": "3", "sentiment": "neutral"}
#                 ]
#                 4. Return the JSON object.
#                 """
#     )
#
# if __name__ == "__main__":
#     main()
