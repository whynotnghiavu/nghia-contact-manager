import os
from flask import Flask
from modules.config import Config


app = Flask(__name__)
app.config.from_object(Config)


if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
