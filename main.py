#!/usr/bin/env python3
"""Simple utility script."""
import os
import sys
import json
from pathlib import Path

def get_config(path="config.json"):
    """Load configuration from JSON file."""
    config_path = Path(path)
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    return {"debug": False, "version": "0.1.0"}

def main():
    config = get_config()
    print(f"Running with config: {config}")

if __name__ == "__main__":
    main()
