from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import os
from apifairy import APIFairy

load_dotenv()

database = SQLAlchemy()
db_migrate = Migrate()
ma = Marshmallow()
apifairy = APIFairy()

def create_app(config_type=os.getenv("CONFIG_TYPE")):
    app = Flask(__name__)
    app.config.from_object(config_type)
    database.init_app(app)
    db_migrate.init_app(app, database)
    import core.models # noqa: F401
    from core.inventory_api import inventory_category_api_blueprint
    app.register_blueprint(blueprint=inventory_category_api_blueprint)
    ma.init_app(app)
    apifairy.init_app(app)
    return app