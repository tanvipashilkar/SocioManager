import os
from flask import Flask, redirect, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/static/index.html')

@app.route('/auth/<platform>')
def auth(platform):
    redirect_uris = {
        "facebook": "https://www.facebook.com/v17.0/dialog/oauth?client_id=YOUR_FACEBOOK_APP_ID&redirect_uri=http://localhost:5000/callback/facebook&scope=email,public_profile",
        "instagram": "https://api.instagram.com/oauth/authorize?client_id=YOUR_INSTAGRAM_APP_ID&redirect_uri=http://localhost:5000/callback/instagram&scope=user_profile,user_media&response_type=code",
        "youtube": "https://accounts.google.com/o/oauth2/auth?client_id=YOUR_GOOGLE_CLIENT_ID&redirect_uri=http://localhost:5000/callback/youtube&scope=https://www.googleapis.com/auth/youtube.readonly&response_type=code&access_type=offline",
        "pinterest": "https://www.pinterest.com/oauth/?response_type=code&client_id=YOUR_PINTEREST_APP_ID&redirect_uri=http://localhost:5000/callback/pinterest&scope=read_public",
        "google": "https://accounts.google.com/o/oauth2/auth?client_id=YOUR_GOOGLE_CLIENT_ID&redirect_uri=http://localhost:5000/callback/google&scope=https://www.googleapis.com/auth/business.manage&response_type=code&access_type=offline",
    }
    return redirect(redirect_uris.get(platform, '/'))

@app.route('/callback/<platform>')
def callback(platform):
    code = request.args.get('code')
    return f"<h2>{platform.title()} connected successfully! Code: {code}</h2>"

if __name__ == '__main__':
    app.run(debug=True)
