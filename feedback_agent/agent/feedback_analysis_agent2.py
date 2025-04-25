# An attempt to create a feedback analysis agent that writes Python code to analyze customer feedback
# though it's not working as expected. Probably because the local model is not strong enough.

from autogen import ConversableAgent
from feedback_agent.agent.code_executor_agent import code_executor_agent
from feedback_agent.config import LLM_CONFIG

def create_feedback_analysis_agent() -> ConversableAgent:
    # Define the feedback analysis agent as a code writer
    feedback_analysis_system_message = """
    You are a feedback analysis specialist that writes Python code to analyze customer feedback.
    When asked to analyze feedback, you must:
    1. Write code that uses the available tools:
       - feedback_reader_tool.query_feedback() - Gets all feedback
       - sentiment_analysis_tool.analyze_sentiment(text) - Returns sentiment
       - keyword_extraction_tool.extract_keywords(text) - Returns keywords list
       - categorization_tool.categorize_feedback(text, keywords) - Returns categories
    2. Process all feedback items and perform complete analysis
    3. Structure results in a clear JSON format
    4. Generate a summary report with insights and recommendations
    
    Always write complete, executable Python code with proper imports.
    """

    feedback_analysis_agent = ConversableAgent(
        "feedback_analysis_agent",
        system_message=feedback_analysis_system_message,
        llm_config=LLM_CONFIG,
        code_execution_config=False,  # Turn off code execution for this agent
        human_input_mode="NEVER",
    )

    return feedback_analysis_agent

def main():
    feedback_analysis_agent = create_feedback_analysis_agent()

    chat_result = code_executor_agent.initiate_chat(
        feedback_analysis_agent,
        message="""
        Perform a complete analysis of customer feedback by writing Python code that:
        
        1. Imports all required modules from feedback_agent.tools
        2. Reads all feedback using query_feedback()
        3. For each feedback item:
           - Analyzes sentiment with analyze_sentiment()
           - Extracts keywords with extract_keywords()
           - Categorizes feedback with categorize_feedback()
        4. Structures results in a JSON format
        5. Generates a final report with findings and recommendations
        
        Make sure your code handles everything end-to-end and displays the results clearly.
        """
    )

    print("\n\n=== FINAL ANALYSIS RESULTS ===")
    print(chat_result)

if __name__ == "__main__":
    main()