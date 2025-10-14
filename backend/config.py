import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/medingen'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecretkey'
