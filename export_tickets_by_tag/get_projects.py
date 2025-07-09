# get_projects.py
import requests
import json
from env import API_BASE_URL
from datetime import datetime
import sys

# Basic no error handling version

# def fetch_projects(token):
#     url = f"{API_BASE_URL}/projects"
#     headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()
#     projects = response.json()['data']
#     filename = datetime.now().strftime("%y%m%d - %H%M%S") + " - Projects.json"
#     with open(filename, 'w') as f:
#         json.dump(projects, f, indent=2)
#     return projects

# # With Error Handling and Debugging

def fetch_projects(token):
    url = f"{API_BASE_URL}/projects"
    headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    try:
        response.raise_for_status()
        if response.ok == True:
            projects = response.json()['data']
            filename = datetime.now().strftime("%y%m%d - %H%M%S") + " - Projects.json"
            with open(filename, 'w') as f:
                json.dump(projects, f, indent=2)
            return projects
    except requests.exceptions.RequestException as e:
        error_detail = response.json()
        print(f"Error details: HTTP {response.status_code}: {error_detail}")
        sys.exit(1)
        return None
