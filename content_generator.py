"""Generate SEO-optimised content for detected niches."""
from __future__ import annotations
import os
from datetime import date
from pathlib import Path
import yaml
import jinja2

from llm.openai_client import generate_blog_post
from niche_detector import detect_niches
from seo_agent import optimise_post
from monetization_agent import monetise_post


POST_TEMPLATE = Path("templates/blog_post_template.md")


def _image_for_topic(topic: str) -> str:
    """Return a royalty-free image URL for the topic."""
    return f"https://source.unsplash.com/featured/?{topic.replace(' ', '%20')}"


def _render_markdown(title: str, author: str, content: str, image_url: str) -> str:
    template = jinja2.Environment().from_string(POST_TEMPLATE.read_text())
    return template.render(
        title=title,
        date=str(date.today()),
        author=author,
        content=content,
        image_url=image_url,
    )


def generate_content(config: dict) -> None:
    """Generate a new article for the first topic in ``niche_data.yaml``."""
    if not Path("niche_data.yaml").exists():
        detect_niches(config)

    with open("niche_data.yaml") as f:
        niches = yaml.safe_load(f)

    topics = niches.get("topics", [])
    if not topics:
        return

    topic = topics.pop(0)
    niches["topics"] = topics
    Path("niche_data.yaml").write_text(yaml.safe_dump(niches))

    content = generate_blog_post(topic, "")
    author = config["blog"]["author"]
    image_url = _image_for_topic(topic)
    markdown = _render_markdown(topic, author, content, image_url)

    output_dir = Path(config["blog"]["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    file_path = output_dir / f"{date.today()}-{topic.replace(' ', '-').lower()}.md"
    file_path.write_text(markdown)

    optimise_post(file_path, config)
    monetise_post(file_path, config)

    print(f"Generated post for topic: {topic}")


if __name__ == "__main__":
    with open("config.yaml") as f:
        cfg = yaml.safe_load(f)
    generate_content(cfg)
