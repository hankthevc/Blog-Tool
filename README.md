# Blog Tool

An AI-powered blog post generator and publisher that automatically creates and publishes content to GitHub Pages.

## Features

- Automated blog post generation using OpenAI GPT-4
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
