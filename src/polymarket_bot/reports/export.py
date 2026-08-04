import json
from pathlib import Path


def export_json(report: dict, path: str = "results/metrics.json"):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2))
    return target
