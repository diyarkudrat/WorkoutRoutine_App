from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import loads, dumps
from bson.objectid import ObjectId
import os


host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
users = db.users
logs = db.logs

app = Flask(__name__)

# logs = [
#     { 'name': 'Bench Press', 'sets': '4', 'reps': '10', 'weight': '225 lbs' },
#     { 'name': 'Squat', 'sets': '4', 'reps': '8', 'weight': '315 lbs' },
# ]

@app.route('/')
def logs_index():
    return render_template('logs_index.html', logs=logs.find())

@app.route('/logs/new')
def logs_new():
    return render_template('logs_new.html', log = {}, title = 'New Log')

@app.route('/logs', methods=['POST'])
def logs_submit():
    log = {
        'date': request.form.get('date'),
        'body_part': request.form.get('body_part'),
        'time_length': request.form.get('time_length'),
        'name': request.form.get('name'),
        'sets': request.form.get('sets'),
        'reps': request.form.get('reps'),
        'weight': request.form.get('weight')
    }
    log_id = logs.insert_one(log).inserted_id
    return redirect(url_for('logs_show', log_id=log_id))

@app.route('/logs/<log_id>')
def logs_show(log_id):
    log = logs.find_one({'_id': ObjectId(log_id)})
    return render_template('logs_show.html', log=log)

@app.route('/logs/<log_id>/edit')
def logs_edit(log_id):
    log = logs.find_one({'_id': ObjectId(log_id)})
    return render_template('logs_edit.html', log=log, title = 'Edit Log')

@app.route('/logs/<log_id>', methods=['POST'])
def logs_update(log_id):
    updated_log = {
        'date': request.form.get('date'),
        'body_part': request.form.get('body_part'),
        'time_length': request.form.get('time_length'),
        'name': request.form.get('name'),
        'sets': request.form.get('sets'),
        'reps': request.form.get('reps'),
        'weight': request.form.get('weight')
    }
    logs.update_one(
        {'_id': ObjectId(log_id)},
        {'$set': updated_log})
    return redirect(url_for('logs_show', log_id=log_id))

@app.route('/logs/<log_id>/delete', methods=['POST'])
def logs_delete(log_id):
    logs.delete_one({'_id': ObjectId(log_id)})
    return redirect(url_for('logs_index'))



@app.route('/workout')
def user_index():
    return render_template('homepage.html')

@app.route('/workout/chest')
def chest():
    return render_template('chest.html')

@app.route('/workout/arms')
def arms():
    return render_template('arms.html')

@app.route('/workout/shoulders')
def shoulders():
    return render_template('shoulders.html')

@app.route('/workout/legs')
def legs():
    return render_template('legs.html')

@app.route('/workout/back')
def back():
    return render_template('back.html')

# @app.route('/workout/create_user')
# def create_user():
#     return render_template('create_account.html')
#
# @app.route('/workout/new_user', methods = ['GET','POST'])
# def register():
#     user = {
#         'name': request.form.get('name'),
#         'username': request.form.get('username'),
#         'password': request.form.get('password')
#     }
#     users.insert_one(user)
#     return redirect(url_for('user_index'))
#
# @app.route('/workout/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         login_user = users.find_one({'username': request.form['username']})
#         if login_user:
#                 data = {
#                     'username': request.form['username'],
#                     'user_id': login_user['_id']
#                 }
#
#                 session['user'] = json.loads(json_util.dumps(data))
#                 return redirect(url_for('user_index'))
#
#     return render_template('login.html')
















if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
