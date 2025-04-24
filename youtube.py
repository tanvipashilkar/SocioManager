from flask import Blueprint, redirect, request
from requests_oauthlib import OAuth2Session
import os

youtube_oauth = Blueprint('youtube_oauth', __name__)

YT_CLIENT_ID = os.getenv("YT_CLIENT_ID")
YT_CLIENT_SECRET = os.getenv("YT_CLIENT_SECRET")
YT_REDIRECT_URI = "http://localhost:5000/youtube/callback"

SCOPE = ["https://www.googleapis.com/auth/youtube.readonly"]
AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"

@youtube_oauth.route('/youtube')
def login():
    youtube = OAuth2Session(YT_CLIENT_ID, redirect_uri=YT_REDIRECT_URI, scope=SCOPE, prompt='consent')
    authorization_url, state = youtube.authorization_url(AUTH_URL, access_type="offline")
    return redirect(authorization_url)

@youtube_oauth.route('/youtube/callback')
def callback():
    youtube = OAuth2Session(YT_CLIENT_ID, redirect_uri=YT_REDIRECT_URI)
    token = youtube.fetch_token(TOKEN_URL,
                                client_secret=YT_CLIENT_SECRET,
                                authorization_response=request.url)
    return "YouTube Connected!"
