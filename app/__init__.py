from flask import Flask
from config import config_options

def create_app(config_name):

# Initializing application
    app = Flask(__name__)

# Setting up configuration
    app.config.from_object(config_options[config_name])


#Registering the blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

        # setting config
    # from .request import configure_request
    # configure_request(app)

    return app