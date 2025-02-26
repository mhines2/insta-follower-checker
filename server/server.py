from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # enable CORS for React frontend

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok = True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

