"""SEO optimisation utilities."""
from __future__ import annotations
from pathlib import Path
import frontmatter

from llm.openai_client import generate_blog_post


def optimise_post(file_path: Path, config: dict) -> None:
    """Add basic SEO metadata to the post."""
    post = frontmatter.load(file_path)
    prompt = (
        f"Create a one sentence meta description and a comma separated list of keywords for the article titled '{post['title']}'."
    )
    try:
        resp = generate_blog_post(prompt, "")
        lines = [l.strip() for l in resp.splitlines() if l.strip()]
        description = lines[0]
        keywords = lines[-1]
        post["description"] = description
        post["keywords"] = keywords
        frontmatter.dump(post, file_path.open("w"))
    except Exception:
        # Fallback: keep original post
        pass
