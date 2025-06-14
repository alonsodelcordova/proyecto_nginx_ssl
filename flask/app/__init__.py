from flask import Flask
from .db import db


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    
    app.config['SECRET_KEY'] = 'secret!111'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    db.init_app(app)
    
    
    from .routes.public_routes import router_app
    from .routes.admin_route import router_app as admin_router_app
    app.register_blueprint(router_app)
    app.register_blueprint(admin_router_app)
    
    
    
    # static files
    @app.route('/static/<path:path>')
    def send_static(path):
        return app.send_static_file(path)
    


    with app.app_context():
        db.create_all()

    return app