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

# Shark facts remain the same...
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

# Updated achievements with metrics we can actually track
ACHIEVEMENTS = {
    "Deep Sea Explorer": {
        "description": "Made significant contributions to core repository code",
        "icon": "🌊",
        "threshold": 10  # number of recent commits
    },
    "Swift Shark": {
        "description": "Maintains multiple active repositories",
        "icon": "⚡",
        "threshold": 3  # number of active repos
    },
    "Code Hunter": {
        "description": "Active across different projects",
        "icon": "🎯",
        "threshold": 5  # different repos committed to
    },
    "Territory Guardian": {
        "description": "Creates and maintains project branches",
        "icon": "🛡️",
        "threshold": 3  # number of active branches
    },
    "Night Stalker": {
        "description": "Active in late-night coding sessions",
        "icon": "🌙",
        "threshold": 5  # commits outside normal hours
    }
}

def get_github_client():
    """Initialize and return a GitHub client."""
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN environment variable not set.")
        return None
    
    return Github(GITHUB_TOKEN)

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
                
                # Add type-specific details
                if event.type == "PushEvent":
                    activity["message"] = f"Hunting bugs in {event.repo.name.split('/')[-1]}"
                    if hasattr(event.payload, 'commits') and event.payload.commits:
                        activity["message"] = f"🦈 {event.payload.commits[0].message[:50]}"
                        if len(event.payload.commits[0].message) > 50:
                            activity["message"] += "..."
                
                elif event.type == "CreateEvent" and event.payload.get("ref_type") == "branch":
                    activity["message"] = f"Created hunting ground {event.payload.get('ref')} in {event.repo.name.split('/')[-1]}"
                    activity["url"] = f"https://github.com/{event.repo.name}/tree/{event.payload.get('ref')}"
                
                elif event.type == "PullRequestEvent":
                    activity["message"] = f"Circling PR waters: {event.payload.get('pull_request').title[:50]}"
                    if len(event.payload.get('pull_request').title) > 50:
                        activity["message"] += "..."
                    activity["url"] = event.payload.get('pull_request').html_url
                
                elif event.type == "IssuesEvent":
                    activity["message"] = f"Tracking prey: {event.payload.get('issue').title[:50]}"
                    if len(event.payload.get('issue').title) > 50:
                        activity["message"] += "..."
                    activity["url"] = event.payload.get('issue').html_url
                
                activities.append(activity)
                count += 1
        
        return activities
    
    except Exception as e:
        print(f"Error retrieving activities: {e}")
        return []

def calculate_achievements(gh, username: str) -> List[str]:
    """Calculate earned achievements based on GitHub activity."""
    try:
        user = gh.get_user(username)
        earned = []
        
        # Count recent events
        events = list(user.get_events())
        recent_commits = len([e for e in events if e.type == "PushEvent"])
        
        # Check Deep Sea Explorer
        if recent_commits >= ACHIEVEMENTS["Deep Sea Explorer"]["threshold"]:
            earned.append("Deep Sea Explorer")
        
        # Check Swift Shark (active repos)
        active_repos = [repo for repo in user.get_repos() if not repo.archived]
        if len(active_repos) >= ACHIEVEMENTS["Swift Shark"]["threshold"]:
            earned.append("Swift Shark")
        
        # Check Code Hunter (different repos committed to)
        committed_repos = set(event.repo.name for event in events if event.type == "PushEvent")
        if len(committed_repos) >= ACHIEVEMENTS["Code Hunter"]["threshold"]:
            earned.append("Code Hunter")
        
        # Check Territory Guardian (active branches)
        branch_count = 0
        for repo in active_repos[:5]:  # Check only first 5 repos for performance
            branch_count += len(list(repo.get_branches()))
        if branch_count >= ACHIEVEMENTS["Territory Guardian"]["threshold"]:
            earned.append("Territory Guardian")
        
        # Check Night Stalker (late night commits)
        night_commits = 0
        for event in events:
            if event.type == "PushEvent":
                hour = event.created_at.hour
                if hour < 6 or hour > 22:  # Between 10PM and 6AM
                    night_commits += 1
        if night_commits >= ACHIEVEMENTS["Night Stalker"]["threshold"]:
            earned.append("Night Stalker")
        
        return earned
    except Exception as e:
        print(f"Error calculating achievements: {e}")
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

def update_achievements_section(content: str, achievements: List[str]) -> str:
    """Update the achievements section in README."""
    achievements_pattern = r'(## 🏆 Shark Achievements.*?)\n\n'
    
    new_achievements = '## 🏆 Shark Achievements\n\n'
    for achievement in achievements:
        info = ACHIEVEMENTS[achievement]
        new_achievements += f"{info['icon']} **{achievement}** - {info['description']}\n"
    new_achievements += '\n'
    
    if re.search(achievements_pattern, content):
        return re.sub(achievements_pattern, new_achievements, content, flags=re.DOTALL)
    else:
        # If section doesn't exist, add it before "Recent Updates"
        return content.replace('## Recent Updates', new_achievements + '## Recent Updates')

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
        
        # Calculate and update achievements
        earned_achievements = calculate_achievements(gh, GITHUB_ACTOR)
        if earned_achievements:
            content = update_achievements_section(content, earned_achievements)
        
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
