from pathlib import Path

import yaml


def load_config(path: str = "config/default.yaml") -> dict:
    file = Path(path)
    if not file.exists():
        return {}
    with file.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}
