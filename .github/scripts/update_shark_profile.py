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

# Extended Shark facts with more tech and security focus
SHARK_FACTS = [
    # Original facts
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
    "SharkBLN's keyboard has no ESC key - just like there's no escaping a determined shark!",
    # New security-focused facts
    "Just as sharks can sense electromagnetic fields, SharkBLN can detect security vulnerabilities in the codebase.",
    "While sharks have multiple rows of teeth, SharkBLN has multiple layers of security.",
    "SharkBLN's security patches are like a shark's immune system - always ready to fight off threats.",
    "In the digital ocean, SharkBLN is the guardian of secure code practices.",
    "SharkBLN's code review process is like a shark's sensory system - nothing gets past undetected.",
    # New coding-focused facts
    "While sharks adapt through evolution, SharkBLN adapts through continuous integration.",
    "SharkBLN's repositories are like shark territories - well-maintained and fiercely protected.",
    "Like a shark's streamlined body, SharkBLN's code is optimized for performance.",
    "SharkBLN's debugging skills are like a shark's hunting instincts - precise and effective.",
    "Just as sharks never stop swimming, SharkBLN never stops improving code quality.",
    # New automation facts
    "SharkBLN's automated tests are like a shark's lateral line - detecting disturbances before they become problems.",
    "While sharks patrol the oceans, SharkBLN's monitoring systems patrol the networks.",
    "SharkBLN's deployment scripts strike as fast as a shark attacking its prey.",
    "Like a shark's powerful sensory system, SharkBLN's logging captures every important detail.",
    "SharkBLN's error handling is like a shark's survival instinct - always prepared for the unexpected.",
]

# Activity emoji mapping
ACTIVITY_EMOJIS = {
    "PushEvent": {
        "prefix": "🦈 Hunting bugs",
        "security": "🛡️ Security patch",
        "feat": "✨ New feature",
        "fix": "🔧 Bug fix",
        "docs": "📚 Documentation",
        "refactor": "♻️ Refactoring",
        "test": "🧪 Testing",
    },
    "CreateEvent": {
        "branch": "🌊 New hunting ground",
        "repository": "🏰 New territory",
        "tag": "🎯 New milestone",
    },
    "PullRequestEvent": {
        "opened": "🎣 Started hunt",
        "closed": "🔱 Successful hunt",
        "reopened": "🔄 Resumed hunt",
    },
    "IssuesEvent": {
        "opened": "👁️ Spotted prey",
        "closed": "✅ Captured prey",
        "reopened": "🔍 Tracking resumed",
    },
}

# Keep existing functions but update the activity formatting...

def get_activity_emoji(event_type: str, payload: Dict[str, Any] = None) -> str:
    """Get appropriate emoji for the activity type and content."""
    if event_type == "PushEvent" and payload and "commits" in payload:
        commit_msg = payload["commits"][0]["message"].lower()
        if any(keyword in commit_msg for keyword in ["security", "vuln", "cve"]):
            return ACTIVITY_EMOJIS["PushEvent"]["security"]
        elif any(keyword in commit_msg for keyword in ["feat", "feature"]):
            return ACTIVITY_EMOJIS["PushEvent"]["feat"]
        elif any(keyword in commit_msg for keyword in ["fix", "bug"]):
            return ACTIVITY_EMOJIS["PushEvent"]["fix"]
        elif any(keyword in commit_msg for keyword in ["doc", "readme"]):
            return ACTIVITY_EMOJIS["PushEvent"]["docs"]
        elif any(keyword in commit_msg for keyword in ["refactor", "clean"]):
            return ACTIVITY_EMOJIS["PushEvent"]["refactor"]
        elif any(keyword in commit_msg for keyword in ["test", "spec"]):
            return ACTIVITY_EMOJIS["PushEvent"]["test"]
        return ACTIVITY_EMOJIS["PushEvent"]["prefix"]
    
    elif event_type == "CreateEvent" and payload:
        ref_type = payload.get("ref_type", "")
        return ACTIVITY_EMOJIS["CreateEvent"].get(ref_type, "🌊")
    
    elif event_type == "PullRequestEvent" and payload:
        action = payload.get("action", "")
        return ACTIVITY_EMOJIS["PullRequestEvent"].get(action, "🎣")
    
    elif event_type == "IssuesEvent" and payload:
        action = payload.get("action", "")
        return ACTIVITY_EMOJIS["IssuesEvent"].get(action, "👁️")
    
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
        return f"{emoji} in {repo_short_name}"
    
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

# Update the get_recent_activities function to use the new formatting
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

# Keep the rest of the existing functions...
# [Previous function implementations remain the same]

if __name__ == "__main__":
    success = update_readme()
    exit(0 if success else 1)
