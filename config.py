import os

class Config:
    SECRET_KEY = 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///products.db'
    UPLOADED_PHOTOS_DEST = os.path.join(os.getcwd(), 'static', 'uploads')
