# Blog Tool

An AI-powered blog post generator and publisher that automatically creates and publishes content to GitHub Pages.

## Features

- Automated blog post generation using OpenAI GPT-4
- GitHub Pages integration for automatic publishing
- Scheduled post generation (daily by default)
- SEO-optimized content with keyword targeting
- Markdown-based content with frontmatter

## Setup

1. Clone the repository:
```bash
git clone https://github.com/hankthevc/Blog-Tool.git
cd Blog-Tool
```

2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

5. (Optional) Configure the blog settings in `config.yaml`:
- Change the blog title
- Update the author name
- Modify the output directory
- Update the GitHub repository URL

## Usage

### Generate a Single Post

```bash
python main.py
```

### Run the Automated Scheduler

```bash
python scheduler.py
```

By default, this will generate a new post every day at 9:00 AM.

### Manual Publishing

To manually publish posts to GitHub Pages:

```bash
python publisher/github_pages.py
```

## Configuration

The `config.yaml` file contains all the necessary settings:

```yaml
openai_api_key: ${OPENAI_API_KEY}
blog:
  title: "AutoBlog Chronicles"
  author: "AI Ghostwriter"
  output_dir: "posts"
  deploy_branch: "gh-pages"
  repo_url: "https://github.com/hankthevc/Blog-Tool"
```

## Adding Custom Topics

Edit `scheduler.py` to add your own topics and keywords to the `BlogScheduler` class.

## License

MIT
