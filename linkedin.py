from flask import Blueprint, redirect, request
import os
from requests_oauthlib import OAuth2Session

linkedin_oauth = Blueprint('linkedin_oauth', __name__)

LINKEDIN_CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID")
LINKEDIN_CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET")
LINKEDIN_REDIRECT_URI = "http://localhost:5000/linkedin/callback"

AUTH_URL = "https://www.linkedin.com/oauth/v2/authorization"
TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"
SCOPE = ["r_liteprofile", "r_emailaddress", "w_member_social"]

@linkedin_oauth.route('/linkedin')
def login():
    linkedin = OAuth2Session(LINKEDIN_CLIENT_ID, redirect_uri=LINKEDIN_REDIRECT_URI, scope=SCOPE)
    authorization_url, state = linkedin.authorization_url(AUTH_URL)
    return redirect(authorization_url)

@linkedin_oauth.route('/linkedin/callback')
def callback():
    linkedin = OAuth2Session(LINKEDIN_CLIENT_ID, redirect_uri=LINKEDIN_REDIRECT_URI)
    token = linkedin.fetch_token(TOKEN_URL,
                                 client_secret=LINKEDIN_CLIENT_SECRET,
                                 authorization_response=request.url)
    return "LinkedIn Connected!"
