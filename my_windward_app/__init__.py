import os
from flask import Flask, render_template

def create_app():
    """
    Application Factory.
    Configures the Flask app, database, and registers all blueprints.
    """
    # create and configure the app
    # instance_relative_config=True tells the app that configuration files are
    # relative to the instance folder.
    app = Flask(__name__, instance_relative_config=True)

    from . import teacher
    app.register_blueprint(teacher.bp)
    
    # This sets up a default configuration for the app.
    # The DATABASE path points to a file inside the 'instance' folder, which Flask creates.
    app.config.from_mapping(
        # a secret key is needed to keep session data safe
        SECRET_KEY = 'dev', # this should be a random secret value in production
        DATABASE=os.path.join(app.instance_path, 'my_windward_app.sqlite'),
    )

    # a route to serve our main login page
    @app.route('/')
    def index():
        return render_template('index.html')

    # import and register the blueprint from the factory
    # Blueprints allow us to split our code into multiple files (modules)
    from . import announcements
    app.register_blueprint(announcements.bp, url_prefix='/api/announcements')
    
    from . import rotation
    app.register_blueprint(rotation.bp)

    from . import profiles
    app.register_blueprint(profiles.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import dashboard
    app.register_blueprint(dashboard.bp)

    from . import chat
    app.register_blueprint(chat.bp)

    # Pro Level Security: Add Security Headers to every response
    @app.after_request
    def add_security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        return response

    return app