from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_home():
    return send_from_directory('integrations.html')

@app.route('/api/integrations')
def get_integrations():
    platforms = [
        {"name": "Facebook", "url": "https://www.facebook.com/yourPage"},
        {"name": "Instagram", "url": "https://www.instagram.com/yourUsername"},
        {"name": "LinkedIn", "url": "https://www.linkedin.com/in/yourProfile"},
        {"name": "YouTube", "url": "https://www.youtube.com/c/yourChannel"},
        {"name": "Google Business", "url": "https://www.google.com/search?q=your+business+name"},
    ]
    return jsonify({"platforms": platforms})

if __name__ == '__main__':
    app.run(debug=True)
