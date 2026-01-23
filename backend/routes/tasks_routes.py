from flask import Blueprint, render_template, redirect, url_for, flash, request
from database.models.task import Task
from database.db_settings import db
from database.crud import *

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def get_all_tasks():
    tasks = get_all_tasks()
    return render_template('templates/index.html', tasks=tasks)

@tasks_bp.route('/<int:task_id>')
def get_task(task_id):

    tasks = get_task_or_404(task_id)
    return render_template('templates/task_info.html', tasks=tasks)


@tasks_bp.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':

        title = request.form.get('title')
        description = request.form.get('description')

        task = create_task(title, description)

        db.session.add(task)
        db.session.commit()

        flash('Задача была добавлена!')

        return redirect(url_for('tasks.get_all_tasks'))
    
    return render_template('templates/add_task.html')


@tasks_bp.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):

    task = delete_task(task_id)

    db.session.delete(task)
    db.session.commit()

    flash('Вы успешно удалии задачу!')

    return redirect(url_for('tasks.get_all_tasks'))