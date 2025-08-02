# Blog Tool

An AI-powered blog post generator and publisher that automatically creates and publishes content to GitHub Pages.

## Features

- Automated niche discovery using Google Trends and GPT
- Daily content generation with image selection
- SEO optimisation and monetisation injection
- Monthly performance reports
- GitHub Pages integration for automatic publishing
- Scheduled post generation (daily by default)
- SEO-optimized content with keyword targeting
- Markdown-based content with frontmatter
- Google Cloud Run deployment support

## Local Setup

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

## Google Cloud Deployment

1. Install the Google Cloud SDK and initialize it:
```bash
# Follow instructions at https://cloud.google.com/sdk/docs/install
gcloud init
```

2. Enable required APIs:
```bash
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
```

3. Set up environment variables:
```bash
# Replace with your project ID
export PROJECT_ID="your-project-id"
gcloud config set project $PROJECT_ID

# Set your OpenAI API key as a secret
gcloud secrets create openai-api-key --replication-policy="automatic"
echo -n "your-openai-api-key" | gcloud secrets versions add openai-api-key --data-file=-
```

4. Deploy to Cloud Run:
```bash
gcloud builds submit --substitutions=_OPENAI_API_KEY="$(gcloud secrets versions access latest --secret=openai-api-key)"
```

The application will be deployed to Cloud Run and will automatically:
- Generate a new blog post every day at 9:00 AM
- Publish it to GitHub Pages
- Scale automatically based on load

## Local Usage

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
