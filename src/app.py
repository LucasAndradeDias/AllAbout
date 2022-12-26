from flask import Flask



def create_app():
    app = Flask(__name__)
    # existing code omitted

    # from . import blog
    # app.register_blueprint(blog.bp)
    # app.add_url_rule('/', endpoint='index')

    from .search import search
    app.register_blueprint(search.search_bp)

    return app

