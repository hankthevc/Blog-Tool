import os
from git import Repo
import yaml
import shutil
from datetime import datetime

class GitHubPagesPublisher:
    def __init__(self):
        with open("config.yaml") as f:
            self.config = yaml.safe_load(f)
        
        self.repo = Repo(os.getcwd())
        self.deploy_branch = self.config['blog']['deploy_branch']

    def _ensure_deploy_branch(self):
        """Ensure the deployment branch exists"""
        if self.deploy_branch not in [ref.name for ref in self.repo.refs]:
            current = self.repo.active_branch
            new_branch = self.repo.create_head(self.deploy_branch)
            new_branch.checkout()
            # Create empty gh-pages branch
            self.repo.index.commit("Initialize gh-pages branch")
            current.checkout()

    def publish(self):
        """Publish blog posts to GitHub Pages"""
        current_branch = self.repo.active_branch
        
        try:
            # Ensure deploy branch exists
            self._ensure_deploy_branch()
            
            # Switch to deploy branch
            self.repo.git.checkout(self.deploy_branch)
            
            # Clean existing files except .git
            for item in os.listdir():
                if item != '.git':
                    if os.path.isfile(item):
                        os.remove(item)
                    elif os.path.isdir(item):
                        shutil.rmtree(item)
            
            # Copy posts directory
            posts_dir = self.config['blog']['output_dir']
            if os.path.exists(posts_dir):
                shutil.copytree(posts_dir, f"./{posts_dir}", dirs_exist_ok=True)
            
            # Add and commit changes
            self.repo.git.add(all=True)
            self.repo.index.commit(f"Update blog posts - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Push to remote
            self.repo.git.push('origin', self.deploy_branch, force=True)
            
            print(f"✅ Successfully published to GitHub Pages")
            
        finally:
            # Switch back to original branch
            current_branch.checkout()

if __name__ == "__main__":
    publisher = GitHubPagesPublisher()
    publisher.publish() 