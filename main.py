import os
from datetime import date
import yaml
import jinja2
from llm.openai_client import generate_blog_post

def generate_and_save_post(topic, keywords):
    """Generate and save a blog post"""
    # Load config
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    # Generate content
    content = generate_blog_post(topic, keywords)

    # Render markdown
    env = jinja2.Environment()
    template = env.from_string(open("templates/blog_post_template.md").read())
    md_output = template.render(
        title=topic,
        date=str(date.today()),
        author=config['blog']['author'],
        content=content
    )

    # Save to file
    os.makedirs(config['blog']['output_dir'], exist_ok=True)
    output_path = os.path.join(
        config['blog']['output_dir'],
        f"{date.today()}-{topic.replace(' ', '-').lower()}.md"
    )
    with open(output_path, "w") as f:
        f.write(md_output)

    print(f"✅ Blog post saved to {output_path}")
    return output_path

if __name__ == "__main__":
    # Default topic and keywords for direct script execution
    topic = "Best Indoor Plants for Small Apartments"
    keywords = "indoor plants, small space, apartment gardening"
    generate_and_save_post(topic, keywords) 