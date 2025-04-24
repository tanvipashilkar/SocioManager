from flask import Blueprint, redirect, request
import os
from requests_oauthlib import OAuth2Session

instagram_oauth = Blueprint('instagram_oauth', __name__)

IG_CLIENT_ID = os.getenv("INSTA_CLIENT_ID")
IG_CLIENT_SECRET = os.getenv("INSTA_CLIENT_SECRET")
IG_REDIRECT_URI = "http://localhost:5000/instagram/callback"
AUTH_URL = "https://www.facebook.com/v18.0/dialog/oauth"
TOKEN_URL = "https://graph.facebook.com/v18.0/oauth/access_token"

@instagram_oauth.route('/instagram')
def login():
    instagram = OAuth2Session(IG_CLIENT_ID, redirect_uri=IG_REDIRECT_URI, scope=[
        "instagram_basic", "pages_show_list", "instagram_manage_insights"
    ])
    authorization_url, state = instagram.authorization_url(AUTH_URL)
    return redirect(authorization_url)

@instagram_oauth.route('/instagram/callback')
def callback():
    instagram = OAuth2Session(IG_CLIENT_ID, redirect_uri=IG_REDIRECT_URI)
    token = instagram.fetch_token(TOKEN_URL,
                                  client_secret=IG_CLIENT_SECRET,
                                  authorization_response=request.url)
    # Example: token['access_token']
    return "Instagram Connected!"
