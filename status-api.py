import os
import json

from flask import Flask, jsonify, request

status_file = "./data/status.json"

app = Flask(__name__)

class StatusUpdate:
    def __init__(self, status_message: str):
        self.status_message = status_message

def ensure_directory_exists(directory_path):
    if not os.path.exists(directory_path):
        print("Creating directory...")
        os.makedirs(directory_path)
    else:
        print("Directory exists")

def file_exists(file_path):
    if (os.path.exists(file_path)):
        print("File exists")
        return True
    else:
        print("File does not exist")
        return False

# Define API endpoints
@app.route('/api/status', methods=['GET'])
def get_items():
    print("GET Request received...")
    if file_exists(status_file):
        with open(status_file, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    else:
        return jsonify({"error": "File not found"}), 404

@app.route('/api/status', methods=['POST'])
def create_item():
    print("POST Request received...")
    status_request = request.get_json()
    
    ensure_directory_exists(os.path.dirname(status_file))

    if file_exists(status_file):
        print("File exists, deleting...")
        os.remove(status_file)

    with open(status_file, 'w') as file:
        json.dump(status_request, file, indent=4)

    return jsonify(status_request), 201

if __name__ == '__main__':
    app.run(debug=True)