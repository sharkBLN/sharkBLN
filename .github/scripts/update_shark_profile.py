#!/usr/bin/env python3

import os
import re
import random
import traceback
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

# Shark facts and emojis
SHARK_FACTS = [
    "Unlike most GitHub users, SharkBLN doesn't need coffee to code - the thrill of the hunt sustains it.",
    "SharkBLN can detect a security vulnerability from a mile away, just as sharks can detect blood in water from great distances.",
    "Just like real sharks never sleep, SharkBLN's monitoring systems run 24/7.",
    "SharkBLN writes code with the same precision a shark uses to hunt its prey - no bugs escape!",
    "While sharks have existed for 450 million years, SharkBLN's code is built to last even longer with proper documentation.",
    "Some sharks can lose up to 30,000 teeth in a lifetime. SharkBLN has squashed even more bugs!",
    "SharkBLN's code reviews are like a shark's bite - thorough and leaving a lasting impression.",
    "Just as the Great White can detect one drop of blood in 25 gallons of water, SharkBLN can spot one bug in 25,000 lines of code.",
    "Sharks can swim up to 45 mph. SharkBLN's CI/CD pipeline is even faster!",
    "Like sharks have electroreception, SharkBLN has a sixth sense for detecting inefficient algorithms.",
    "SharkBLN's git branches are like shark fins - always visible above the surface, warning others of activity below.",
    "While sharks use their ampullae of Lorenzini, SharkBLN uses logging and monitoring to detect disturbances in the system.",
    "SharkBLN's code deployment strategy: silent, efficient, and precise - just like a shark's hunting pattern.",
    "In the vast ocean of code, SharkBLN is the apex debugger.",
    "SharkBLN's keyboard has no ESC key - just like there's no escaping a determined shark!"
]

def get_github_client():
    """Initialize and return a GitHub client."""
    try:
        if not GITHUB_TOKEN:
            print("Error: GITHUB_TOKEN environment variable not set.")
            return None
        
        gh = Github(GITHUB_TOKEN)
        # Test the connection
        gh.get_user().login
        return gh
    except Exception as e:
        print(f"Error initializing GitHub client: {e}")
        print(f"Traceback: {traceback.format_exc()}")
        return None

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
                    "url": f"https://github.com/{event.repo.name}",
                    "message": ""
                }
                
                if event.type == "PushEvent":
                    if hasattr(event.payload, 'commits') and event.payload.commits:
                        activity["message"] = f"🦈 {event.payload.commits[0].message[:50]}"
                        if len(event.payload.commits[0].message) > 50:
                            activity["message"] += "..."
                    else:
                        activity["message"] = f"🦈 Hunting in {event.repo.name.split('/')[-1]}"
                
                elif event.type == "CreateEvent":
                    ref_type = event.payload.get("ref_type", "")
                    ref = event.payload.get("ref", "")
                    if ref_type == "branch":
                        activity["message"] = f"🌊 Created branch `{ref}` in {event.repo.name.split('/')[-1]}"
                        activity["url"] = f"https://github.com/{event.repo.name}/tree/{ref}"
                    else:
                        activity["message"] = f"🏰 Created {ref_type} in {event.repo.name.split('/')[-1]}"
                
                elif event.type == "PullRequestEvent":
                    title = event.payload.get("pull_request", {}).get("title", "")
                    action = event.payload.get("action", "")
                    activity["message"] = f"🎣 {action.capitalize()} PR: {title[:50]}"
                    if len(title) > 50:
                        activity["message"] += "..."
                    activity["url"] = event.payload.get("pull_request", {}).get("html_url", activity["url"])
                
                elif event.type == "IssuesEvent":
                    title = event.payload.get("issue", {}).get("title", "")
                    action = event.payload.get("action", "")
                    activity["message"] = f"👁️ {action.capitalize()}: {title[:50]}"
                    if len(title) > 50:
                        activity["message"] += "..."
                    activity["url"] = event.payload.get("issue", {}).get("html_url", activity["url"])
                
                activities.append(activity)
                count += 1
        
        return activities
    
    except Exception as e:
        print(f"Error retrieving activities: {e}")
        print(f"Traceback: {traceback.format_exc()}")
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
    try:
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
    except Exception as e:
        print(f"Error updating shark sightings: {e}")
        print(f"Traceback: {traceback.format_exc()}")
        return content

def update_shark_fact(content: str) -> str:
    """Update the Daily Shark Fact section with a new random fact."""
    try:
        fact_pattern = r'<b>🦈 Daily Shark Fact 🦈</b><br>\s*<i>".*?"</i>'
        new_fact = f'<b>🦈 Daily Shark Fact 🦈</b><br>\n  <i>"{get_random_shark_fact()}"</i>'
        
        # Replace the old fact with the new one
        updated_content = re.sub(fact_pattern, new_fact, content)
        
        return updated_content
    except Exception as e:
        print(f"Error updating shark fact: {e}")
        print(f"Traceback: {traceback.format_exc()}")
        return content

def update_readme():
    """Main function to update the README.md file."""
    try:
        print("Starting README update process...")
        
        # Initialize GitHub client
        print("Initializing GitHub client...")
        gh = get_github_client()
        if not gh:
            print("Failed to initialize GitHub client")
            return False
        
        # Read the current README content
        print("Reading README.md...")
        try:
            with open(README_PATH, "r", encoding='utf-8') as f:
                content = f.read()
            print("Successfully read README.md")
        except Exception as e:
            print(f"Error reading README.md: {e}")
            print(f"Current directory: {os.getcwd()}")
            print(f"Directory contents: {os.listdir('.')}")
            return False
        
        # Get recent GitHub activities
        print("Fetching recent activities...")
        activities = get_recent_activities(gh, GITHUB_ACTOR)
        if activities:
            print(f"Found {len(activities)} recent activities")
            content = update_shark_sightings(content, activities)
        else:
            print("No recent activities found")
        
        # Update shark fact
        print("Updating shark fact...")
        content = update_shark_fact(content)
        
        # Write the updated content back to the README
        print("Writing updated content to README.md...")
        try:
            with open(README_PATH, "w", encoding='utf-8') as f:
                f.write(content)
            print("Successfully wrote updated content to README.md")
        except Exception as e:
            print(f"Error writing to README.md: {e}")
            return False
        
        print(f"README.md updated successfully at {datetime.now(timezone.utc).isoformat()} UTC")
        return True
    except Exception as e:
        print(f"Error updating README: {e}")
        print(f"Traceback: {traceback.format_exc()}")
        return False

if __name__ == "__main__":
    try:
        print("Starting script execution...")
        success = update_readme()
        if success:
            print("Script completed successfully")
            exit(0)
        else:
            print("Script failed")
            exit(1)
    except Exception as e:
        print(f"Unexpected error in main: {e}")
        print(f"Traceback: {traceback.format_exc()}")
        exit(1)
