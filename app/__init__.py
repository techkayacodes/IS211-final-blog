from flask import Flask
from .extensions import db
from werkzeug.security import generate_password_hash
from .auth import auth_bp  # Import the auth blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        # Import models here
        from .models import User

        db.create_all()  # Create database tables
        
        app.register_blueprint(auth_bp)  # Register the auth blueprint
        # Create the root user if it doesn't exist
        if not User.query.filter_by(username='pythonadmin').first():
            root_user = User(
                username='pythonadmin',
                password=generate_password_hash('pythonP@ss!')
            )
            db.session.add(root_user)
            db.session.commit()

        # Import routes here
        from .routes import main_bp
        app.register_blueprint(main_bp)

    return app
