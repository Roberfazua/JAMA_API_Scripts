# main.py
import argparse
import sys
from env import *
from get_token import get_token
from get_projects import fetch_projects
from get_tags import fetch_tags
from find_tag_id import find_tag_id
from get_tickets import fetch_tickets
from export_data import export_all

# main.py

# Step	File Name	Purpose
# 0	main.py	Main entry point, user interaction
# 1	env.py	Stores credentials and API URLs
# 2	get_token.py	Handles OAuth2 token retrieval
# 3	get_projects.py	Fetches and stores all projects
# 4	get_tags.py	Fetches and stores all tags from projects
# 5	find_tag_id.py, get_tickets.py	Finds tag ID, fetches tickets
# 6	export_data.py	Exports tickets to CSV/JSON
# 7	requirements.txt	Lists required Python packages

# Basic no Error Handling
# def main():
#     print("Jama API Data Export Utility")
#     tag_name = input("Enter the tag name to search: ").strip()
#     token = get_token()
#     projects = fetch_projects(token)
#     tags = fetch_tags(token, projects)
#     tag_id = find_tag_id(tags, tag_name)
#     tickets = fetch_tickets(token, tag_id)
#     export_all(projects, tags, tag_id, tickets)
#     print("Export complete!")



def parse_args():
    parser = argparse.ArgumentParser(
        description="Jama API Data Export Utility"
    )
    parser.add_argument(
        "--tag", required=True, help="Tag name to search for"
    )
    parser.add_argument(
        "--tagsfile", help="Path to Tags.json file (optional, will use latest if not provided)"
    )
    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    # Basic error control: check if tag is empty
    if not args.tag.strip():
        print("ERROR: --tag parameter is required and cannot be empty.")
        sys.exit(1)

    print("Jama API Data Export Utility")
    tag_name = args.tag

    # 1. Get token
    token = get_token()

    # 2. Get all projects
    projects = fetch_projects(token)

    # 3. Get all tags
    tags = fetch_tags(token, projects)

    # 4. Find tag ID (pass file if provided, otherwise use latest)
    if args.tagsfile:
        import json
        try:
            with open(args.tagsfile, "r", encoding="utf-8") as f:
                tags_data = json.load(f)
        except Exception as e:
            print(f"ERROR: Could not open or parse tags file '{args.tagsfile}': {e}")
            sys.exit(1)
        tag_id = find_tag_id(tags_data, tag_name)
    else:
        tag_id = find_tag_id(tags, tag_name)

    if not tag_id:
        print(f"Tag '{tag_name}' not found. Exiting.")
        sys.exit(1)

    # 5. Get tickets by tag ID
    tickets = fetch_tickets(token, tag_id)

    # 6. Export data
    export_all(projects, tags, tag_id, tickets)
    print("Export complete!")

if __name__ == "__main__":
    main()
