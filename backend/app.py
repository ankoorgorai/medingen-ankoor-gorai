from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from database import db
from routes import api
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
JWTManager(app)
db.init_app(app)
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def home():
    return {"message": "Medingen API running!"}

if __name__ == '__main__':
    app.run(debug=True)
