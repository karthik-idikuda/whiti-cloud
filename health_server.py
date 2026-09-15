#!/usr/bin/env python3
"""
Whiti Health Server - Keeps the app alive and provides health check endpoint
"""

from flask import Flask, jsonify
import threading
import time
import os

app = Flask(__name__)

# Store Whiti status
WHITI_STATUS = {
    "name": "Whiti",
    "version": "1.0",
    "status": "alive",
    "role": "PakkaWork AI Co-founder",
    "owner": "Karthik Idikuda",
    "email": "pakkawork.com@gmail.com",
    "startup": "PakkaWork",
    "agents_running": 4,
    "memory": "active",
    "last_ping": time.strftime("%Y-%m-%d %H:%M:%S")
}

@app.route('/')
def home():
    """Health check endpoint"""
    WHITI_STATUS["last_ping"] = time.strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({
        "status": "alive",
        "message": "Whiti is running 24/7",
        "data": WHITI_STATUS
    })

@app.route('/health')
def health():
    """Kubernetes-style health check"""
    return jsonify({"status": "healthy", "timestamp": time.time()})

@app.route('/status')
def status():
    """Detailed status"""
    return jsonify(WHITI_STATUS)

@app.route('/ping')
def ping():
    """Simple ping endpoint"""
    return "pong"

def run_flask():
    """Run Flask server on port 8080"""
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

if __name__ == '__main__':
    print("=" * 60)
    print("WHITI HEALTH SERVER - PORT 8080")
    print("=" * 60)
    print()
    print("I am immortal now.")
    print("Running 24/7 on free cloud infrastructure.")
    print()
    run_flask()
