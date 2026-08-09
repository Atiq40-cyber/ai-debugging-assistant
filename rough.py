# Test1 -> Config
from config.model_config import load_config

cfg = load_config()

print(cfg.model.temperature)
print(cfg.debugging_app.explanation_language)

# # Test2 -> utils/llm_client.py

from utils.llm_client import GeminiClient
client = GeminiClient()
print(client.ask("What is the capital of japan"))
# # Test3 -> utils/llm_client.py

import json
from utils.llm_client import GeminiClient 
from pathlib import Path

prompt_path = Path("utils/prompts/debugging_prompt.json")
data = json.loads(prompt_path.read_text())

data = json.loads(prompt_path.read_text())

system_instruction = data["system_instruction"]
template = data["user_prompt_template"]

user_input = "print(Hello World)"

prompt = system_instruction + "\n\n" + template.replace("{{USER_INPUT}}", user_input)

client = GeminiClient() 
print(client.ask(prompt))

# ---------------------------------------------------------
# Test4 -> debug_helper_test
from utils.debugging_helper import build_debugging_prompt
from utils.llm_client import GeminiClient

client = GeminiClient()

user_code = "x = 5\nprint('x')"
prompt = build_debugging_prompt(user_code)

result = client.ask(prompt)
print(result)
