import os


basedir = os.path.abspath(os.path.dirname(__file__))
output = os.path.join(basedir, 'output')


class Config:
    SECRET_KEY = os.urandom(24)

    UPLOAD_FOLDER = os.path.join(output, 'uploads')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(output, 'nghia_contact_manager.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
