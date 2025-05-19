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

# [Previous configurations remain the same]
# ... [SHARK_FACTS and other configurations] ...

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

# [Other functions remain the same]
# ... [Previous function implementations] ...

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
