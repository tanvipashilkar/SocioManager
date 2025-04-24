from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB = 'socio.db'

def query_db(query, args=(), one=False):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    con.commit()
    con.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def home():
    return render_template("dashboard.html")

@app.route('/connect/<platform>', methods=['POST'])
def connect_platform(platform):
    query_db("INSERT INTO channels (user_id, platform) VALUES (?, ?)", (1, platform))
    return jsonify({"message": f"{platform} connected"})

@app.route('/channels')
def get_channels():
    result = query_db("SELECT platform FROM channels WHERE user_id = 1")
    return jsonify([dict(row) for row in result])

@app.route('/post', methods=['POST'])
def create_post():
    data = request.get_json()
    query_db(
        "INSERT INTO posts (user_id, content, schedule_time, status) VALUES (?, ?, ?, ?)",
        (1, data['content'], data['schedule_time'], "queued")
    )
    return jsonify({"message": "Post scheduled"})

@app.route('/posts/<status>')
def get_posts(status):
    result = query_db("SELECT * FROM posts WHERE status = ? AND user_id = 1", (status,))
    return jsonify([dict(row) for row in result])

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    query_db("INSERT INTO feedback (user_id, message) VALUES (?, ?)", (1, data['feedback']))
    return jsonify({"message": "Feedback received"})

@app.route('/calendar')
def calendar():
    posts = query_db("SELECT content, schedule_time FROM posts WHERE user_id = 1")
    return jsonify([dict(row) for row in posts])

if __name__ == '__main__':
    app.run(debug=True)
