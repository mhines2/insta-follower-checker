from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import os
from flask_cors import CORS

app = Flask(__name__) 
CORS(app) # enable CORS for React frontend

# Create folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def extract_usernames_from_html(file_path):
    """
    Extracts Instagram usernames from a downloaded HTML file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

        # Extract usernames
        usernames = set()
        for tag in soup.find_all("a"): # Instagram stores usernames in <a> tags
            username = tag.text.strip() 
            if username:
                usernames.add(username)

        return usernames

def save_uploaded_file(uploaded_file, filename):
    """
    Saves uploaded file to the designated upload folder.
    """
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    uploaded_file.save(file_path)
    return file_path

@app.route('/upload', methods=['POST']) # POST request to upload file
def upload_files():
    # Check if POST request has file parts
    if 'followers' not in request.files or 'following' not in request.files: 
        return jsonify({"error": "Both followers.html and following.html must be uploaded."}), 400
    
    # Save uploaded files
    followers_file = request.files['followers']
    following_file = request.files['following']

    followers_path = save_uploaded_file(followers_file, "followers.html")
    following_path = save_uploaded_file(following_file, "following.html")

    # Extract usernames from uploaded files
    followers = extract_usernames_from_html(followers_path)
    following = extract_usernames_from_html(following_path)

    not_following_back = list(following - followers)

    return jsonify({"not_following_back": not_following_back}) 

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001) # run Flask server

    