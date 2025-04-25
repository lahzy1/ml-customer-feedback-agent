from autogen import AssistantAgent
from dotenv import load_dotenv

from feedback_agent.config import LLM_CONFIG

load_dotenv()

# Reflection function
def evaluate_response(agent, response: str) -> str:
    reflection_prompt = f"""
You are reviewing your previous recommendation as a product analyst.

Evaluate this output:
{response}

Was it logically sound? Did it meet all criteria? Was it clear and complete?

If there are flaws, explain them.
If it's satisfactory, state that.
"""
    return agent.generate_reply(messages=[{"role": "user", "content": reflection_prompt}])

# AssistantV2 with self-evaluation capability
assistant_v2 = AssistantAgent(
    name="AssistantV2",
    llm_config=LLM_CONFIG,
    system_message="""
You are an intelligent assistant that provides thoughtful product recommendations.
After giving your recommendation, reflect critically on your response—was it logically sound,
aligned with all criteria, and clearly explained? Suggest improvements if necessary.
"""
)

# Step 1: Initial Recommendation
initial_response = assistant_v2.generate_reply(
    messages=[{"role": "user", "content": """
Recommend a smartphone suitable for university students focusing on productivity, note-taking, battery life, affordability, and build quality. Clearly justify your choice.
"""}]
)

print("Initial Response:\n", initial_response)

# Step 2: Reflection
reflection = evaluate_response(assistant_v2, initial_response)
print("\nSelf-Evaluation:\n", reflection)

# Step 3: Reasoning about improvements
improvement_reasoning = assistant_v2.generate_reply(
    messages=[{"role": "user", "content": """
Based on the self-evaluation, refine the recommendation.
"""}]
)

print("\nRefined Recommendation:\n", improvement_reasoning)
