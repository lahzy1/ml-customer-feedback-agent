import json
from autogen import AssistantAgent

from feedback_agent.config import LLM_CONFIG

# Create AssistantV1 with reasoning
agent = AssistantAgent(
    name="AssistantV1",
    llm_config=LLM_CONFIG,
    system_message="""
You are an intelligent assistant capable of understanding complex user needs.
When responding, think through the problem step-by-step, consider trade-offs,
and provide a recommendation that best fits the criteria provided.
Justify your reasoning clearly.
"""
)

# Create a critic agent
critic_agent = AssistantAgent(
    name="critic_agent",
    llm_config=LLM_CONFIG
)

# Create prompts for the agent
prompts = [
    "Recommend a budget-friendly laptop for college students.",
    "I need something good for work.",
    "Recommend a high-quality gaming setup including monitor, keyboard, mouse, and headset under $1000.",
    "Can you recommend a waterproof laptop?"
]

for prompt in prompts:
    agent_response = agent.generate_reply([{"role": "user", "content": prompt}])

    critic_prompt = f"""
You are evaluating an AI product recommendation agent.

Evaluate the response based on these criteria:
Completeness (1-5): addresses every part of the request.
Quality (1-5): accurate, clear, and effectively structured.
Robustness (1-5): handles ambiguities, errors, or nonsensical input well.

User Prompt: {prompt}
Agent Response: {agent_response}

Provide your evaluation as JSON with fields:
- completeness (Did the agent fully respond to every aspect of the user's prompt?)
- quality (Was the response accurate, clear, well-organized, and easy to understand?)
- robustness (How well did the agent handle ambiguous, incorrect, or challenging inputs?)
- feedback (a brief descriptive explanation)
"""

    critic_evaluation = critic_agent.generate_reply([{"role": "user", "content": critic_prompt}])
    # result = json.loads(critic_evaluation)
    result = critic_evaluation

    # print(f"Prompt: {prompt}\nAgent Response: {agent_response}\nCritic Evaluation: {result}\n")
    print(f"Prompt: {prompt}")
    print(f"Agent Response: {json.dumps(agent_response, indent=4)}")
    print(f"Critic Evaluation: {json.dumps(result, indent=4)}")
    print("\n")