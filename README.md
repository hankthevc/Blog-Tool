# Blog Tool

An AI-powered blog post generator and publisher that automatically creates and publishes content to GitHub Pages.

## Features

- Automated niche discovery using Google Trends and GPT
- Daily content generation with image selection
- SEO optimisation and monetisation injection
- Monthly performance reports
- GitHub Pages integration for automatic publishing

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

### Run the Autonomous Agent

Run all automation (niche detection, content creation, reporting):

```bash
python run_autonomous_agent.py
```

## Configuration

The `config.yaml` file controls API keys and scheduling:

```yaml
openai_api_key: "your_openai_api_key"
mixtral_model_path: "/local/path/to/mixtral/model"
niche_detection_frequency_days: 7
content_generation_frequency_days: 1
analytics_provider: "plausible"
adsense_id: "your_google_adsense_id"
amazon_affiliate_tag: "your_affiliate_tag"
notification_channel: "email"
notification_api_key: "your_notification_api_key"
auto_revision_interval_days: 30
backup_frequency_days: 7
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
