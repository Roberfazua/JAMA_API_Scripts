# get_token.py
import requests
import sys
from env import TOKEN_URL, CLIENT_ID, CLIENT_SECRET

# Basic no error handling version

def get_token():
    data = {'grant_type': 'client_credentials'}
    response = requests.post(
        TOKEN_URL,
        data=data,
        auth=(CLIENT_ID, CLIENT_SECRET)  # This sets HTTP Basic Auth
    )
    response.raise_for_status()
    return response.json()['access_token']


# TEST
# print("Token fetched successfully.")
# print(get_token())


# # With Error Handling and Debugging
# def get_token():
#     data = {
#         'grant_type': 'client_credentials',
#     }
#     try:
#         response = requests.post(TOKEN_URL, data=data, auth=(CLIENT_ID, CLIENT_SECRET))
#         if response.ok and response.status_code == 200:
#             return response.json()['access_token']
#         else:
#             # Try to get error message from Jama's response
#             try:
#                 error_detail = response.json()
#                 print(f"Error details: HTTP {response.status_code}: {error_detail}")
#                 sys.exit(1)
#             except Exception:
#                 error_detail = response.text
#                 print(f"Error details: HTTP {response.status_code}: {error_detail}")
#                 sys.exit(1)
                
#             return None, f"HTTP {response.status_code}: {error_detail}"
#     except requests.exceptions.RequestException as e:
#         return None, f"Request failed: {e}"
