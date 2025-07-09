# env.py
# How to get this data:
# https://porsche-ep.atlassian.net/wiki/spaces/TEAMPROCESS/pages/3842670598/JAMA+-+API+-+Automatization#API-RES-CREDENTIALS-CREATION

JAMA_SUBDOMAIN = "porscheebike"
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
TOKEN_URL = f"https://{JAMA_SUBDOMAIN}.jamacloud.com/rest/oauth/token"
API_BASE_URL = f"https://{JAMA_SUBDOMAIN}.jamacloud.com/rest/latest"

