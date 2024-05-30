from flask import render_template, request, jsonify
from threading import Thread
import time

from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_timer', methods=['POST'])
def set_timer():
    data = request.json
    duration = data.get('duration')
    sets = data.get('sets')
    rest = data.get('rest')

    thread = Thread(target=run_timer, args=(duration, sets, rest))
    thread.start()
    
    return jsonify(status="success")

def run_timer(duration, sets, rest):
    for _ in range(sets):
        for t in range(duration, -1, -1):
            time.sleep(1)
        time.sleep(rest)
