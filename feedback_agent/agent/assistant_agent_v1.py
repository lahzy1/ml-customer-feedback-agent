from autogen import AssistantAgent, UserProxyAgent

from feedback_agent.config import LLM_CONFIG

# Create AssistantV1 with reasoning
assistant_v1 = AssistantAgent(
    name="AssistantV1",
    llm_config=LLM_CONFIG,
    system_message="""
You are an intelligent assistant capable of understanding complex user needs.
When responding, think through the problem step-by-step, consider trade-offs,
and provide a recommendation that best fits the criteria provided.
Justify your reasoning clearly.
"""
)

# User proxy
user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
    code_execution_config=False
)

# Run the agent
assistant_v1.initiate_chat(user_proxy, max_turns=2, message="Recommend a smartphone suitable for university students focusing on productivity, note-taking, battery life, affordability, and build quality. Clearly justify your choice.")

# Send a single message and get the response using generate_reply
# response = assistant_v1.generate_reply(
#     messages=[{"role": "user", "content": """Recommend a smartphone suitable for university students focusing on productivity, note-taking, battery life, affordability, and build quality. Clearly justify your choice."""}]
# )

# print(response)
