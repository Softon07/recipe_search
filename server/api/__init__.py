from flask import Flask
from firebase_admin import credentials, initialize_app

cred = credentials.Certificate('server/api/key.json')
default_app = initialize_app(cred)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'j4jizkQKmLB3QNptm0BPGRMxOC6Ev3iiI4yqRoJU'
    
    from .userAPI import userAPI
    from .recipeAPI import recipeAPI
    from .categoryAPI import categoryAPI
    from .allergenAPI import allergenAPI
    
    app.register_blueprint(userAPI, url_prefix = '/users')
    app.register_blueprint(recipeAPI, url_prefix = '/recipes')
    app.register_blueprint(categoryAPI, url_prefix = '/categories')
    app.register_blueprint(allergenAPI, url_prefix = '/allergens')
    
    return app