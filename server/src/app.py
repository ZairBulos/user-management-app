from flask import Flask
from config import config
from routes import User
from src.db import db

def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(environment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    app.register_blueprint(User.main, url_prefix='/api/users')

    return app

environment = config['development']
app = create_app(environment)

if __name__ == '__main__':
    app.run()
