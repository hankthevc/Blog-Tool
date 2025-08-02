"""Monetisation helpers for blog posts."""
from __future__ import annotations
from pathlib import Path
import frontmatter


def monetise_post(file_path: Path, config: dict) -> None:
    post = frontmatter.load(file_path)
    adsense = config.get("adsense_id")
    affiliate = config.get("amazon_affiliate_tag")
    footer = (
        f"<script data-ad-client='{adsense}' async src='https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'></script>"
    )
    affiliate_link = f"https://www.amazon.com?tag={affiliate}" if affiliate else None
    if affiliate_link:
        post.content += f"\n\n[Recommended product]({affiliate_link})"
    post.content += f"\n\n{footer}"
    frontmatter.dump(post, file_path.open("w"))
