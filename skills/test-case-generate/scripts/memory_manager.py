#!/usr/bin/env python3
import argparse
import json
from datetime import datetime
from pathlib import Path

MEMORY_DIR = ".test-case-memory"
DEFAULTS = {
    "project-context.json": {},
    "terminology.json": {"domain_terms": {}, "module_abbreviations": {}},
    "generation-history.json": {"generations": []},
    "user-preferences.json": {"language": "zh-CN", "platform": "APP"},
    "ambiguity-decisions.json": {"decisions": []},
}


def initialize(project):
    root = Path(project).resolve()
    memory = root / MEMORY_DIR
    memory.mkdir(parents=True, exist_ok=True)
    for name, default in DEFAULTS.items():
        path = memory / name
        if not path.exists():
            value = dict(default)
            if name == "project-context.json":
                value = {"project_name": root.name, "initialized_at": datetime.now().isoformat()}
            path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    return memory


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", default=".")
    parser.add_argument("--action", choices=["init", "read", "add-record"], required=True)
    parser.add_argument("--type")
    parser.add_argument("--data")
    args = parser.parse_args()
    memory = initialize(args.project)
    mapping = {
        "context": "project-context.json", "terminology": "terminology.json",
        "history": "generation-history.json", "preferences": "user-preferences.json",
        "ambiguities": "ambiguity-decisions.json"
    }
    if args.action == "init":
        print(memory)
    elif args.action == "read":
        name = mapping.get(args.type or "")
        if not name:
            raise SystemExit("read 需要有效的 --type")
        print((memory / name).read_text(encoding="utf-8"))
    else:
        record = json.loads(args.data or "{}")
        path = memory / "generation-history.json"
        history = json.loads(path.read_text(encoding="utf-8"))
        record["date"] = datetime.now().isoformat()
        history["generations"].append(record)
        path.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")
        print(path)


if __name__ == "__main__":
    main()
