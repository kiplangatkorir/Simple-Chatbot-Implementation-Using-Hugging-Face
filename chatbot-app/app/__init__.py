from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fdcfaf580caf1dee241c83f5c181dbf7'

    with app.app_context():
        from . import routes

    return app
