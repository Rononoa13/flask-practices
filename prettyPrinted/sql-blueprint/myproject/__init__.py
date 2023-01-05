from flask import Flask
from . extensions import db
from .routes import main


def create_app():
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    db.init_app(app)

    app.register_blueprint(main)
    # from . import models

    with app.app_context():
        db.create_all()

    return app