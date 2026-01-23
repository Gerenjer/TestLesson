from flask import Flask
from config import _config
from database.db_settings import db
from routes.tasks_routes import tasks_bp

def create_app():

    app = Flask(__name__)

    app.config.from_object(_config)

    db.init_app(app)

    app.register_blueprint(tasks_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context(): 
        db.create_all()

    app.run(debug=True)