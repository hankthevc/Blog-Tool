"""Main orchestrator for the autonomous blogging system."""
from __future__ import annotations
import json
import os
from datetime import datetime, timedelta
import yaml

from niche_detector import detect_niches
from content_generator import generate_content
from performance_monitor import generate_report

STATE_FILE = "agent_state.json"


def load_state() -> dict:
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}


def save_state(state: dict) -> None:
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def should_run(task: str, interval_days: int, state: dict) -> bool:
    last_run = state.get(task)
    if not last_run:
        return True
    last_dt = datetime.fromisoformat(last_run)
    return datetime.utcnow() - last_dt >= timedelta(days=interval_days)


def main() -> None:
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    state = load_state()

    if should_run("niche_detection", config["niche_detection_frequency_days"], state):
        detect_niches(config)
        state["niche_detection"] = datetime.utcnow().isoformat()

    if should_run(
        "content_generation", config["content_generation_frequency_days"], state
    ):
        generate_content(config)
        state["content_generation"] = datetime.utcnow().isoformat()

    # Always attempt monthly report; function internally checks interval
    generate_report(config, state)

    save_state(state)


if __name__ == "__main__":
    main()
