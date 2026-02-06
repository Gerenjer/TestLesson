from flask import Blueprint, render_template
from backend.database.crud import get_tasks

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():

    tasks = get_tasks()
    tasks_count = len(tasks)

    return render_template('index.html', tasks=tasks, tasks_count=tasks_count)