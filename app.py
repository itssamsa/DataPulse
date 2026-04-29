import os

from flask import Flask
from pymongo import MongoClient

from routers.empleados_router import empleados_bp


def create_app():
    app = Flask(__name__)

    mongo_uri = os.environ.get("MONGODB_URI", "mongodb://localhost:27017")
    mongo_db = os.environ.get("MONGODB_DB", "DataPulse")

    client = MongoClient(mongo_uri)
    app.db = client[mongo_db]

    app.register_blueprint(empleados_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
