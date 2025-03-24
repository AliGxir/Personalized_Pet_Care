from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    api = Api(app)

    # Register routes
    from routes.user_routes import UserRegister, UserLogin
    api.add_resource(UserRegister, "/register")
    api.add_resource(UserLogin, "/login")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
