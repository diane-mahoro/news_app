from flask import Flask
from flask import Blueprint


# from . import views,errors
# from config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap=Bootstrap()



# # app.config.from_object(DevConfig)
# # app.config.from_pyfile('config.py')
# from .main import views

def create_app(config_name):
    #....
    # Registering the blueprint
    app =Flask(__name__)
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)

    return app