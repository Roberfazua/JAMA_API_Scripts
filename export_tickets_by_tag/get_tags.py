# get_tags.py
import requests
import json
from env import API_BASE_URL
from datetime import datetime

# Basic no error handling version

# def fetch_tags(token, projects):
#     headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}
#     all_tags = []
#     for project in projects:
#         pid = project['id']
#         url = f"{API_BASE_URL}/tags?project={pid}"
#         resp = requests.get(url, headers=headers)
#         if resp.status_code == 200:
#             tags = resp.json().get('data', [])
#             for tag in tags:
#                 tag['project_id'] = pid
#             all_tags.extend(tags)
#     filename = datetime.now().strftime("%y%m%d - %H%M%S") + " - Tags.json"
#     with open(filename, 'w') as f:
#         json.dump(all_tags, f, indent=2)
#     return all_tags

# print("Tags fetched and saved successfully.")

# Example usage (replace with actual token and projects)
# token = "your_api_token"
# projects = [{"id": 123}, {"id": 456}]
# tags = fetch_tags(token, projects)
# print(tags)


# With Error Handling and Debugging
import requests
import json
from env import API_BASE_URL
from datetime import datetime

def fetch_tags(token, projects):
    headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}
    all_tags = []
    page_size = 50  # Jama's max page size

    for project in projects:
        pid = project['id']
        start_at = 0
        while True:
            url = f"{API_BASE_URL}/tags?project={pid}&startAt={start_at}&maxResults={page_size}"
            resp = requests.get(url, headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                tags = data.get('data', [])
                for tag in tags:
                    tag['project_id'] = pid
                all_tags.extend(tags)
                # Check if we've fetched all tags for this project
                if len(tags) < page_size:
                    break
                start_at += page_size
            else:
                print(f"Failed to fetch tags for project {pid}: {resp.status_code}")
                break

    filename = datetime.now().strftime("%y%m%d - %H%M%S") + " - Tags.json"
    print(filename)
    with open(filename, 'w') as f:
        json.dump(all_tags, f, indent=2)
    return all_tags

