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

# Extended Shark facts with more tech focus
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

# Shark Achievements definitions
ACHIEVEMENTS = {
    "Deep Sea Explorer": {
        "description": "Made significant contributions to core repository code",
        "icon": "🌊",
        "threshold": 100  # lines changed
    },
    "Swift Shark": {
        "description": "Quick to review and merge PRs",
        "icon": "⚡",
        "threshold": 5  # PRs reviewed
    },
    "Code Hunter": {
        "description": "Found and fixed critical bugs",
        "icon": "🎯",
        "threshold": 10  # issues closed
    },
    "Territory Guardian": {
        "description": "Maintains multiple active repositories",
        "icon": "🛡️",
        "threshold": 3  # active repos
    },
    "Night Stalker": {
        "description": "Active in late-night coding sessions",
        "icon": "🌙",
        "threshold": 10  # commits after hours
    }
}

def get_github_client():
    """Initialize and return a GitHub client."""
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN environment variable not set.")
        return None
    
    return Github(GITHUB_TOKEN)

def get_project_status(gh, repo_name: str) -> Dict[str, Any]:
    """Get detailed status of a specific project."""
    try:
        repo = gh.get_repo(repo_name)
        
        # Get branch information
        branches = list(repo.get_branches())
        active_branches = [b for b in branches if b.commit.commit.author.date > 
                         (datetime.now(timezone.utc) - timedelta(days=30))]
        
        # Get PR information
        open_prs = list(repo.get_pulls(state='open'))
        
        # Get recent commits
        commits = list(repo.get_commits(since=datetime.now(timezone.utc) - timedelta(days=7)))
        
        return {
            "active_branches": len(active_branches),
            "open_prs": len(open_prs),
            "recent_commits": len(commits),
            "watchers": repo.watchers_count,
            "stars": repo.stargazers_count
        }
    except Exception as e:
        print(f"Error getting project status: {e}")
        return {}

def get_tech_stack_status(gh, username: str) -> Dict[str, int]:
    """Calculate technology usage based on recent activity."""
    try:
        user = gh.get_user(username)
        repos = user.get_repos()
        
        language_stats = Counter()
        for repo in repos:
            if repo.language:
                language_stats[repo.language] += 1
        
        return dict(language_stats.most_common(5))
    except Exception as e:
        print(f"Error getting tech stack status: {e}")
        return {}

def calculate_achievements(gh, username: str) -> List[str]:
    """Calculate earned achievements based on GitHub activity."""
    try:
        user = gh.get_user(username)
        earned = []
        
        # Check Deep Sea Explorer
        commits = list(user.get_events())
        commit_count = sum(1 for e in commits if e.type == "PushEvent")
        if commit_count >= ACHIEVEMENTS["Deep Sea Explorer"]["threshold"]:
            earned.append("Deep Sea Explorer")
        
        # Check Swift Shark
        reviews = list(user.get_user_reviews())
        if len(reviews) >= ACHIEVEMENTS["Swift Shark"]["threshold"]:
            earned.append("Swift Shark")
        
        # Check Territory Guardian
        active_repos = len(list(user.get_repos()))
        if active_repos >= ACHIEVEMENTS["Territory Guardian"]["threshold"]:
            earned.append("Territory Guardian")
        
        return earned
    except Exception as e:
        print(f"Error calculating achievements: {e}")
        return []

def update_project_section(content: str, status: Dict[str, Any]) -> str:
    """Update the project status section in README."""
    project_pattern = r'(### 🔥 \[Dragon Threats \(abuse_pipeline\)\].*?)\n\n'
    if not status:
        return content
    
    new_status = f"""### 🔥 [Dragon Threats (abuse_pipeline)](https://github.com/sharkBLN/abuse_pipeline)
*Taming digital dragons: A comprehensive security monitoring system that breathes fire on system threats*

![](https://img.shields.io/badge/active_branches-{status['active_branches']}-blue?style=flat-square)
![](https://img.shields.io/badge/open_prs-{status['open_prs']}-yellow?style=flat-square)
![](https://img.shields.io/badge/recent_commits-{status['recent_commits']}-green?style=flat-square)
![](https://img.shields.io/badge/watchers-{status['watchers']}-purple?style=flat-square)
![](https://img.shields.io/badge/stars-{status['stars']}-gold?style=flat-square)

"""
    
    return re.sub(project_pattern, new_status, content, flags=re.DOTALL)

def update_tech_stack(content: str, stats: Dict[str, int]) -> str:
    """Update the tech stack section with current usage statistics."""
    stack_pattern = r'(## 🔱 Weapons in My Arsenal.*?)</p>'
    if not stats:
        return content
    
    new_stack = '## 🔱 Weapons in My Arsenal\n\n<p align="center">\n'
    for lang, count in stats.items():
        color = "blue" if lang == "Python" else "grey" if lang == "JavaScript" else "red" if lang == "Go" else "purple"
        new_stack += f'  <img src="https://img.shields.io/badge/{lang}-{count}_repos-{color}?style=for-the-badge&logo={lang.lower()}" />\n'
    new_stack += '</p>'
    
    return re.sub(stack_pattern, new_stack, content, flags=re.DOTALL)

def update_achievements(content: str, achievements: List[str]) -> str:
    """Update the achievements section in README."""
    achievements_pattern = r'(## 🏆 Shark Achievements.*?)\n\n'
    if not achievements:
        return content
    
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
            return
        
        # Read the current README content
        with open(README_PATH, "r") as f:
            content = f.read()
        
        # Get project status
        status = get_project_status(gh, "sharkBLN/abuse_pipeline")
        if status:
            content = update_project_section(content, status)
        
        # Get and update tech stack
        tech_stats = get_tech_stack_status(gh, GITHUB_ACTOR)
        if tech_stats:
            content = update_tech_stack(content, tech_stats)
        
        # Calculate and update achievements
        earned_achievements = calculate_achievements(gh, GITHUB_ACTOR)
        if earned_achievements:
            content = update_achievements(content, earned_achievements)
        
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

# Keep existing functions (get_recent_activities, update_shark_sightings, etc.)
# ... [previous function implementations remain the same] ...

if __name__ == "__main__":
    update_readme()
