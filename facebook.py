from flask import Blueprint, redirect, request
import os
from requests_oauthlib import OAuth2Session

facebook_oauth = Blueprint('facebook_oauth', __name__)

FB_CLIENT_ID = os.getenv("FB_CLIENT_ID")
FB_CLIENT_SECRET = os.getenv("FB_CLIENT_SECRET")
FB_REDIRECT_URI = "http://localhost:5000/facebook/callback"

@facebook_oauth.route('/facebook')
def login():
    facebook = OAuth2Session(FB_CLIENT_ID, redirect_uri=FB_REDIRECT_URI, scope=["pages_manage_posts", "pages_read_engagement"])
    authorization_url, state = facebook.authorization_url("https://www.facebook.com/dialog/oauth")
    return redirect(authorization_url)

@facebook_oauth.route('/facebook/callback')
def callback():
    facebook = OAuth2Session(FB_CLIENT_ID, redirect_uri=FB_REDIRECT_URI)
    facebook.fetch_token("https://graph.facebook.com/v12.0/oauth/access_token",
                         client_secret=FB_CLIENT_SECRET,
                         authorization_response=request.url)
    # Store access token or fetch user data
    return "Facebook Connected!"
