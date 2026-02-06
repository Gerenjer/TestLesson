from flask import Flask
from .config import _config
from backend.database.db_settings import db
from backend.routes.home_routes import home_bp
from backend.routes.tasks_routes import tasks_bp

def create_app():

    app = Flask(__name__, template_folder='templates')

    app.config.from_object(_config)

    db.init_app(app)

    with app.app_context():
        from backend.database.models.task import Task  # noqa: F401
        db.create_all()

    app.register_blueprint(home_bp)
    app.register_blueprint(tasks_bp, url_prefix='/api/tasks')

    return app

