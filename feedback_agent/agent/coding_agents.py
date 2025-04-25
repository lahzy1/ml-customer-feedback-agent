import pprint

from feedback_agent.agent.code_executor_agent import code_executor_agent
from feedback_agent.agent.code_writer_agent import code_writer_agent

chat_result = code_executor_agent.initiate_chat(
    code_writer_agent, message="Write Python code to calculate and list the first 10 numbers that are both a prime and a Fibonacci number."
)

pprint.pprint(chat_result)
