# get_tickets.py
import requests
import json
from env import API_BASE_URL
from datetime import datetime

def fetch_tickets(token, tag_id):
    url = f"{API_BASE_URL}/tags/{tag_id}/items"
    headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    tickets = response.json()['data']
    filename = datetime.now().strftime("%y%m%d - %H%M%S") + " - Tickets.json"
    with open(filename, 'w') as f:
        json.dump(tickets, f, indent=2)
    return tickets