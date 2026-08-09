from __future__ import annotations
from pathlib import Path 
from typing import Optional

import yaml
from pydantic import BaseModel, Field

class ModelConfig(BaseModel):
    name: str = Field(default="gemini-2.0-flash")
    temperature: float = Field(default=0.4, ge=0.0, le=1.0)
    top_p: float = Field(default=0.9, ge=0.0, le=1.0)
    max_output_token: int = Field(default=2048, ge=1)

class DebuggingAppConfig(BaseModel):
    explanation_language: str = "en"
    max_code_chars: int = 4000

class AppConfig(BaseModel):
    model: ModelConfig
    debugging_app: DebuggingAppConfig = DebuggingAppConfig()


def load_config(path: Optional[str | Path] = None) -> AppConfig:
    if path is None:
        root_dir = Path(__file__).resolve().parent.parent
        path = root_dir/"config"/"config.yaml"

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found at: {path}")
    
    with path.open("r", encoding="utf-8") as f:
        raw_cfg = yaml.safe_load(f) or {}

    return AppConfig(**raw_cfg)