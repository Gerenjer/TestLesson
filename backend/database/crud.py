from typing import List, Optional, Dict, Any
from sqlalchemy.exc import SQLAlchemyError

from database.db_settings import db
from database.models.task import Task



def create_task(title, description) -> Task:
    title = (title or "").strip()
    description = (description or "").strip()

    if not title:
        raise ValueError("Title is required")
    
    task = Task(title, description)

    try:
        db.session.add(task)
        db.session.commit()
        return task
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e


def get_task_or_404(task_id) -> Task:
    return Task.query.get_or_404(task_id)


def get_all_tasks() -> List[Task]:
    return Task.query.all()


def update_task(task_id, title, description) -> Task:
    task = Task.query.get_or_404(task_id)

    if title is not None:
        new_title = (title or "").strip()
        if not new_title:
            raise ValueError("Title cannot be empty")
        task.title = new_title

    if description is not None:
        task.description = (description or "").strip()

    try:
        db.session.commit()
        return task
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e

def delete_task(task_id) -> None:
    task = Task.query.get_or_404(task_id)

    try:
        db.session.delete(task)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        raise e

def update_task_from_dict(task_id, data) -> Task:
    title = data.get("title")
    description = data.get("description")
    return update_task(task_id, title=title, description=description)
