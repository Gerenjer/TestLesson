from flask import Blueprint, render_template, redirect, url_for, flash, request
from backend.database.models.task import Task
from backend.database.db_settings import db
from backend.database.crud import *

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def get_all_tasks():
    tasks = get_tasks()
    return render_template('tasks.html', tasks=tasks)

@tasks_bp.route('/<int:task_id>')
def get_task(task_id):

    task = get_task_or_404(task_id)
    return render_template('task_info.html', task=task)


@tasks_bp.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':

        title = request.form.get('title')
        description = request.form.get('description')

        create_task(title=title, description=description)

        flash('Задача была добавлена!', 'success')

        return redirect(url_for('home.index'))
    
    return render_template('add_task.html')


@tasks_bp.route('/delete/<int:task_id>', methods=['POST'])
def delete_task_route(task_id):

    delete_tasks(task_id)

    flash('Вы успешно удалии задачу!', 'success')

    return redirect(url_for('tasks.get_all_tasks'))