#!/usr/bin/env python3
"""
Shark Activities Update Script for GitHub Profile
Updates the SharkBLN GitHub profile README with recent activities and daily shark facts.
"""

import os
import re
import random
import datetime
from github import Github
from github.GithubException import GithubException

# Shark facts to randomly select from
SHARK_FACTS = [
    "Unlike most GitHub users, SharkBLN doesn't need coffee to code - the thrill of the hunt sustains it.",
    "When SharkBLN commits code, it's permanently immutable - no shark has ever needed to revert a commit.",
    "SharkBLN can detect vulnerabilities from miles away, sensing the digital equivalent of a single drop of blood in the ocean.",
    "While other developers debug, SharkBLN simply eliminates the weak code in a process known as 'natural selection'.",
    "The SharkBLN pipeline never sleeps - much like its creator, who continuously patrols the digital depths.",
    "SharkBLN's code standards are so high that pull requests evolve just to meet them.",
    "Some say SharkBLN doesn't push to repositories - the repositories pull from SharkBLN out of respect.",
    "SharkBLN's keyboard has no backspace key - mistakes are for lesser predators.",
    "When SharkBLN tests code, failing tests don't just fail - they become extinct.",
    "It's rumored that SharkBLN doesn't use version control - the code is simply too afraid to change without permission."
]

def get_github_client():
    """Initialize and return GitHub client using token from environment variables."""
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise ValueError("No GitHub token found in environment variables")
    return Github(token)

def get_recent_activity(github_client, username="SharkBLN", max_events=3):
    """Get recent GitHub activity for the specified user."""
    try:
        user = github_client.get_user(username)
        events = user.get_events()
        
        activities = []
        count = 0
        
        for event in events:
            if count >= max_events:
                break
                
            if event.type == "PushEvent":
                repo_name = event.repo.name
                created_at = event.created_at
                time_ago = get_time_ago(created_at)
                activities.append({
                    "text": f"🦈 Pushed some shark code to {repo_name}",
                    "link": f"https://github.com/{repo_name}",
                    "time": time_ago
                })
                count += 1
            
            elif event.type == "CreateEvent":
                repo_name = event.repo.name
                created_at = event.created_at
                time_ago = get_time_ago(created_at)
                activities.append({
                    "text": f"🦈 Created a new hunting ground at {repo_name}",
                    "link": f"https://github.com/{repo_name}",
                    "time": time_ago
                })
                count += 1
                
            elif event.type == "IssueCommentEvent" or event.type == "IssuesEvent":
                repo_name = event.repo.name
                created_at = event.created_at
                time_ago = get_time_ago(created_at)
                activities.append({
                    "text": f"🦈 Found prey (issues) in {repo_name}",
                    "link": f"https://github.com/{repo_name}",
                    "time": time_ago
                })
                count += 1
        
        # If no real activities found, create placeholder ones
        if not activities:
            activities = [
                {
                    "text": "🦈 Spotted hunting dragons at abuse_pipeline",
                    "link": "https://github.com/sharkBLN/abuse_pipeline",
                    "time": "2 hours ago"
                },
                {
                    "text": "🦈 The shark has been busy refactoring its lair",
                    "link": "https://github.com/sharkBLN",
                    "time": "yesterday"
                },
                {
                    "text": "🦈 A successful hunt yielded 3 fixed bugs",
                    "link": "https://github.com/sharkBLN",
                    "time": "3 days ago"
                }
            ]
            
        return activities
    
    except GithubException as e:
        print(f"Error fetching GitHub activities: {e}")
        return []

def get_time_ago(timestamp):
    """Convert timestamp to relative time string (e.g., '2 hours ago')."""
    now = datetime.datetime.now(datetime.timezone.utc)
    diff = now - timestamp
    
    seconds = diff.total_seconds()
    
    if seconds < 60:
        return "just now"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif seconds < 604800:
        days = int(seconds / 86400)
        return f"{days} day{'s' if days > 1 else ''} ago"
    elif seconds < 2592000:
        weeks = int(seconds / 604800)
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"
    else:
        months = int(seconds / 2592000)
        return f"{months} month{'s' if months > 1 else ''} ago"

def get_random_shark_fact():
    """Return a random shark fact from the list of facts."""
    return random.choice(SHARK_FACTS)

def update_readme(github_client, username="SharkBLN", repo_name="SharkBLN"):
    """Update the README.md file with new shark activities and a daily fact."""
    try:
        # Get repository
        repo = github_client.get_user(username).get_repo(repo_name)
        
        # Get README content
        readme_file = repo.get_contents("README.md")
        readme_content = readme_file.decoded_content.decode("utf-8")
        
        # Get activities and shark fact
        activities = get_recent_activity(github_client, username)
        shark_fact = get_random_shark_fact()
        
        # Prepare new activities HTML
        activities_html = ""
        for activity in activities:
            activities_html += f"""    <tr>
      <td>
        <a href="{activity['link']}">
          {activity['text']} - <i>{activity['time']}</i>
        </a>
      </td>
    </tr>
"""
        
        # Update activities section
        activity_pattern = r'<table>.*?<tr>.*?<td><b>🌊 Recent Shark Sightings 🌊</b></td>.*?</tr>(.*?)</table>'
        new_activities_section = f"""<table>
    <tr>
      <td><b>🌊 Recent Shark Sightings 🌊</b></td>
    </tr>
{activities_html}  </table>"""
        
        updated_readme = re.sub(activity_pattern, new_activities_section, readme_content, flags=re.DOTALL)
        
        # Update shark fact
        fact_pattern = r'<b>🦈 Daily Shark Fact 🦈</b><br>\s*<i>"(.*?)"</i>'
        new_fact = f'<b>🦈 Daily Shark Fact 🦈</b><br>\n  <i>"{shark_fact}"</i>'
        
        updated_readme = re.sub(fact_pattern, new_fact, updated_readme)
        
        # Update README file
        repo.update_file(
            path=readme_file.path,
            message="🦈 Daily shark activities update",
            content=updated_readme,
            sha=readme_file.sha
        )
        
        print("Successfully updated README with new shark activities and fact!")
        
    except GithubException as e:
        print(f"Error updating README: {e}")

if __name__ == "__main__":
    github_client = get_github_client()
    update_readme(github_client)
