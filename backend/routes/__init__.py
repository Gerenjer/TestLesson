from backend.routes.tasks_routes import tasks_bp

def init_routes(app):
    app.register_blueprints(tasks_bp, url_prefix='/tasks')