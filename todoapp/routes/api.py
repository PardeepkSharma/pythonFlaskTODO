from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from sqlalchemy import or_
from todoapp.models.task import Task
from ..extentions import db

api = Blueprint('api', __name__)
@api.route('/home', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        newTask = request.form['task']
        newDesc = request.form['desc']
        todo = Task(task=newTask, desc=newDesc)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for("api.home_page"))  # updated

    username = session.get('username')
    allTask = Task.query.all()
    return render_template('content.html', task_list=allTask, username=username)

@api.route('/delete/<int:id>')
def delete_todo(id):
    task = Task.query.filter_by(id=id).first_or_404()  # updated for 404 handling
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("api.home_page"))  # updated

@api.route('/update/<int:id>', methods=['GET', 'POST'])
def update_todo(id):
    task = Task.query.filter_by(id=id).first_or_404()  # updated for 404 handling

    if request.method == 'POST':
        updatedTask = request.form['task']
        updatedDesc = request.form['desc']
        task.task = updatedTask
        task.desc = updatedDesc
        db.session.commit()  # No need to add; commit updates it
        return redirect(url_for("api.home_page"))  # updated

    return render_template('update.html', task=task)

@api.route('/search', methods=['POST'])
def search_todo():
    if request.method == 'POST':
        text = request.form['search']
        results = Task.query.filter(
            or_(
                Task.task.like(f'%{text}%'),
                Task.desc.like(f'%{text}%')
            )
        ).all()
        return render_template('content.html', task_list=results)
    return redirect(url_for("api.home_page"))  # updated

@api.route('/about')
def about_page():
    return render_template('about.html')
