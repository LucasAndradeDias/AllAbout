from flask import Flask



def create_app():
    app = Flask(__name__)

    #app config


    #register blueprints

    from .search import search
    app.register_blueprint(search.search_bp)



    return app

