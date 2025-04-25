from autogen import AssistantAgent, UserProxyAgent

from feedback_agent.config import LLM_CONFIG

assistant_v0 = AssistantAgent(
    name="AssistantV0",
    llm_config=LLM_CONFIG,
    system_message="You are a helpful assistant that answers questions clearly."
)

# Create a code execution configuration that disables Docker
code_execution_config = {
    "use_docker": False,
}

user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
    code_execution_config=code_execution_config
)

# Run the simple agent
assistant_v0.initiate_chat(user_proxy, max_turns=2, message="""
Recommend a smartphone suitable for university students focusing on productivity, note-taking, battery life, affordability, and build quality. Clearly justify your choice.
""")