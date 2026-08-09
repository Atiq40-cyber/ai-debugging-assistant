from __future__ import annotations
import os
from typing import Optional
import google.generativeai as genai
from dotenv import load_dotenv
from config.model_config import load_config
load_dotenv()

class GeminiClient:
    def __init__(self, api_key: Optional[str] = None, config_path: Optional[str] = None):
        self.app_config = load_config(config_path)
        self.model_cfg = self.app_config.model

        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found.")
        
        # Configure client
        genai.configure(api_key=self.api_key)

        # Initialize model
        self.model = genai.GenerativeModel(self.model_cfg.name)

    def ask(self, prompt: str) -> str:
        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": self.model_cfg.temperature,
                "top_p": self.model_cfg.top_p,
                "max_output_tokens": self.model_cfg.max_output_token
            }
        )

        if not response or not hasattr(response, "text"):
            return "No response generated. Please try again."
        
        return response.text