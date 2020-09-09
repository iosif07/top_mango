from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB':'Shop'}
app.config["SECRET_KEY"] = "secret"

db = MongoEngine(app)

from .shop import shop as shop_blueprint
app.register_blueprint(shop_blueprint)


