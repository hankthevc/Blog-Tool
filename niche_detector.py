"""Automated niche detection using Google Trends and OpenAI."""
from __future__ import annotations
import yaml
from datetime import date
from pathlib import Path
from typing import Any

try:
    from pytrends.request import TrendReq
except Exception:  # pragma: no cover - library may not be installed
    TrendReq = None

from llm.openai_client import generate_blog_post  # reusing client for API access


NICHE_FILE = Path("niche_data.yaml")


def detect_niches(config: dict) -> list[str]:
    """Detect profitable niches and store them in ``niche_data.yaml``."""
    topics: list[str] = []

    if TrendReq:
        try:
            pytrends = TrendReq()
            df = pytrends.trending_searches(pn="global")
            topics = df[0].head(10).tolist()
        except Exception:
            topics = []

    if not topics:
        prompt = (
            "List ten profitable blog niches for the coming week. "
            "Return them as a comma separated list."
        )
        completion = generate_blog_post(prompt, "")
        topics = [t.strip() for t in completion.split(",") if t.strip()]

    data: dict[str, Any] = {"last_updated": str(date.today()), "topics": topics}
    NICHE_FILE.write_text(yaml.safe_dump(data))
    return topics


if __name__ == "__main__":
    with open("config.yaml") as f:
        cfg = yaml.safe_load(f)
    detect_niches(cfg)
