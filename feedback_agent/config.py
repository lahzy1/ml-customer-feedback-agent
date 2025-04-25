LLM_CONFIG = {
    "model": "llama3.1:latest", # Same as llama3.1:8b?
    "client_host": "127.0.0.1:11434",
    "api_type": "ollama",
    "repeat_penalty": 1.1,
    "stream": False,
    "seed": 42,
    "native_tool_calls": False,
    "cache_seed": None,
    #"num_predict": -1, # Will not work with llama3.1:latest (8b?)
    # "temperature": 1, # Will not work with llama3.1:latest (8b?)
    # "top_k": 50, # Will not work with llama3.1:latest (8b?)
    # "top_p": 0.8, # Will not work with llama3.1:latest (8b?)
}