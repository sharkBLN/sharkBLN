#!/usr/bin/env python3
"""
SharkBLN Profile Updater

This script updates the SharkBLN GitHub profile with:
- Recent GitHub activities (Shark Sightings)
- Random daily shark facts
- Project status updates
- Contribution metrics
- Tech stack status
- Shark achievements
"""

import os
import re
import random
from datetime import datetime, timedelta, timezone
import github
from github import Github
from collections import Counter
from typing import List, Dict, Any

# Configuration
README_PATH = "README.md"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "sharkBLN/sharkBLN")
GITHUB_ACTOR = os.environ.get("GITHUB_ACTOR", "sharkBLN")

# [Previous SHARK_FACTS and ACTIVITY_EMOJIS remain the same]
# ... [Previous configurations remain the same] ...

def get_github_client():
    """Initialize and return a GitHub client."""
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN environment variable not set.")
        return None
    
    return Github(GITHUB_TOKEN)

def get_activity_emoji(event_type: str, payload: Dict[str, Any] = None) -> str:
    """Get appropriate emoji for the activity type and content."""
    if event_type == "PushEvent" and payload and "commits" in payload:
        commit_msg = payload["commits"][0]["message"].lower()
        if any(keyword in commit_msg for keyword in ["security", "vuln", "cve"]):
            return "🛡️"
        elif any(keyword in commit_msg for keyword in ["feat", "feature"]):
            return "✨"
        elif any(keyword in commit_msg for keyword in ["fix", "bug"]):
            return "🔧"
        elif any(keyword in commit_msg for keyword in ["doc", "readme"]):
            return "📚"
        elif any(keyword in commit_msg for keyword in ["refactor", "clean"]):
            return "♻️"
        elif any(keyword in commit_msg for keyword in ["test", "spec"]):
            return "🧪"
        return "🦈"
    
    elif event_type == "CreateEvent" and payload:
        ref_type = payload.get("ref_type", "")
        if ref_type == "branch":
            return "🌊"
        elif ref_type == "repository":
            return "🏰"
        return "🎯"
    
    elif event_type == "PullRequestEvent" and payload:
        action = payload.get("action", "")
        if action == "opened":
            return "🎣"
        elif action == "closed":
            return "🔱"
        return "🔄"
    
    elif event_type == "IssuesEvent" and payload:
        action = payload.get("action", "")
        if action == "opened":
            return "👁️"
        elif action == "closed":
            return "✅"
        return "🔍"
    
    return "🦈"

def format_activity_message(event_type: str, payload: Dict[str, Any], repo_name: str) -> str:
    """Format activity message with appropriate emoji and context."""
    emoji = get_activity_emoji(event_type, payload)
    repo_short_name = repo_name.split('/')[-1]
    
    if event_type == "PushEvent":
        if payload and "commits" in payload and payload["commits"]:
            message = payload["commits"][0]["message"]
            # Capitalize first letter and truncate if needed
            message = message[0].upper() + message[1:]
            if len(message) > 50:
                message = message[:47] + "..."
            return f"{emoji} {message}"
        return f"{emoji} Hunting in {repo_short_name}"
    
    elif event_type == "CreateEvent":
        ref_type = payload.get("ref_type", "")
        ref = payload.get("ref", "")
        if ref_type == "branch":
            return f"{emoji} Created branch `{ref}` in {repo_short_name}"
        elif ref_type == "repository":
            return f"{emoji} Created new repository {repo_short_name}"
        return f"{emoji} Created {ref_type} in {repo_short_name}"
    
    elif event_type == "PullRequestEvent":
        action = payload.get("action", "")
        title = payload.get("pull_request", {}).get("title", "")
        if len(title) > 50:
            title = title[:47] + "..."
        return f"{emoji} {action.capitalize()} PR: {title}"
    
    elif event_type == "IssuesEvent":
        action = payload.get("action", "")
        title = payload.get("issue", {}).get("title", "")
        if len(title) > 50:
            title = title[:47] + "..."
        return f"{emoji} {action.capitalize()}: {title}"
    
    return f"{emoji} Activity in {repo_short_name}"

def get_recent_activities(gh, username: str, limit: int = 3) -> List[Dict[str, Any]]:
    """Get recent GitHub activities for the specified user."""
    try:
        user = gh.get_user(username)
        events = user.get_events()
        
        activities = []
        count = 0
        
        for event in events:
            if count >= limit:
                break
                
            if event.type in ["PushEvent", "CreateEvent", "PullRequestEvent", "IssuesEvent"]:
                activity = {
                    "type": event.type,
                    "repo": event.repo.name,
                    "created_at": event.created_at,
                    "url": f"https://github.com/{event.repo.name}"
                }
                
                # Format message based on event type
                activity["message"] = format_activity_message(
                    event.type,
                    event.payload,
                    event.repo.name
                )
                
                # Update URL for specific events
                if event.type == "PullRequestEvent" and "pull_request" in event.payload:
                    activity["url"] = event.payload["pull_request"]["html_url"]
                elif event.type == "IssuesEvent" and "issue" in event.payload:
                    activity["url"] = event.payload["issue"]["html_url"]
                elif event.type == "CreateEvent" and event.payload.get("ref_type") == "branch":
                    activity["url"] = f"https://github.com/{event.repo.name}/tree/{event.payload.get('ref')}"
                
                activities.append(activity)
                count += 1
        
        return activities
    
    except Exception as e:
        print(f"Error retrieving activities: {e}")
        return []

def get_time_description(timestamp):
    """Convert timestamp to human-readable relative time."""
    now = datetime.now(timezone.utc)
    delta = now - timestamp
    
    if delta < timedelta(minutes=1):
        return "Just now"
    elif delta < timedelta(hours=1):
        minutes = delta.seconds // 60
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    elif delta < timedelta(days=1):
        hours = delta.seconds // 3600
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif delta < timedelta(days=7):
        days = delta.days
        return f"{days} day{'s' if days > 1 else ''} ago"
    elif delta < timedelta(days=30):
        weeks = delta.days // 7
        return f"{weeks} week{'s' if weeks > 1 else ''} ago"
    else:
        return timestamp.strftime("%b %d, %Y")

def get_random_shark_fact():
    """Return a random shark fact from the collection."""
    return random.choice(SHARK_FACTS)

def update_shark_sightings(content: str, activities: List[Dict[str, Any]]) -> str:
    """Update the Recent Shark Sightings section with new activities."""
    # Define patterns to find the shark sightings section
    start_pattern = r'<table>[\s\S]*?<tr>[\s\S]*?<td><b>🌊 Recent Shark Sightings 🌊</b></td>[\s\S]*?</tr>'
    end_pattern = r'</table>'
    
    # Find the start and end of the sightings section
    start_match = re.search(start_pattern, content)
    if not start_match:
        print("Could not find the start of shark sightings section")
        return content
    
    # Find the end of the table from the start position
    content_after_start = content[start_match.end():]
    end_match = re.search(end_pattern, content_after_start)
    if not end_match:
        print("Could not find the end of shark sightings section")
        return content
    
    # Build the new sightings section
    header = start_match.group(0)
    new_rows = ""
    
    for activity in activities:
        time_desc = get_time_description(activity["created_at"])
        new_rows += f"""    <tr>
      <td>
        <a href="{activity['url']}">
          {activity['message']} - <i>{time_desc}</i>
        </a>
      </td>
    </tr>
"""
    
    # Combine header, new rows, and footer
    new_section = header + new_rows + end_pattern
    
    # Replace the old section with the new one
    return content[:start_match.start()] + new_section + content[start_match.end() + end_match.end():]

def update_shark_fact(content: str) -> str:
    """Update the Daily Shark Fact section with a new random fact."""
    fact_pattern = r'<b>🦈 Daily Shark Fact 🦈</b><br>\s*<i>".*?"</i>'
    new_fact = f'<b>🦈 Daily Shark Fact 🦈</b><br>\n  <i>"{get_random_shark_fact()}"</i>'
    
    # Replace the old fact with the new one
    updated_content = re.sub(fact_pattern, new_fact, content)
    
    return updated_content

def update_readme():
    """Main function to update the README.md file."""
    try:
        # Initialize GitHub client
        gh = get_github_client()
        if not gh:
            return False
        
        # Read the current README content
        with open(README_PATH, "r") as f:
            content = f.read()
        
        # Get recent GitHub activities
        activities = get_recent_activities(gh, GITHUB_ACTOR)
        if activities:
            content = update_shark_sightings(content, activities)
        
        # Update shark fact
        content = update_shark_fact(content)
        
        # Write the updated content back to the README
        with open(README_PATH, "w") as f:
            f.write(content)
        
        print(f"README.md updated successfully at {datetime.now(timezone.utc).isoformat()} UTC")
        return True
    except Exception as e:
        print(f"Error updating README: {e}")
        return False

if __name__ == "__main__":
    success = update_readme()
    exit(0 if success else 1)
