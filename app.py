from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import loads, dumps
from bson.objectid import ObjectId
import os

SECRET_KEY = os.getenv('SECRET_KEY')

client = MongoClient()
db = client.User
users = db.users
logs = db.logs

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

logs = [
    { 'name': 'Bench Press', 'sets': '4', 'reps': '10', 'weight': '225 lbs' },
    { 'name': 'Squat', 'sets': '4', 'reps': '8', 'weight': '315 lbs' },
]

@app.route('/logs')
def logs_index():
    return render_template('logs_index.html', logs=logs)
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

@app.route('/workout/create_user')
def create_user():
    return render_template('create_account.html')

@app.route('/workout/new_user', methods = ['GET','POST'])
def register():
    user = {
        'name': request.form.get('name'),
        'username': request.form.get('username'),
        'password': request.form.get('password')
    }
    users.insert_one(user)
    return redirect(url_for('user_index'))

@app.route('/workout/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login_user = users.find_one({'username': request.form['username']})
        if login_user:
                data = {
                    'username': request.form['username'],
                    'user_id': login_user['_id']
                }

                session['user'] = json.loads(json_util.dumps(data))
                return redirect(url_for('user_index'))

    return render_template('login.html')
















if __name__ == '__main__':
    app.run(debug=True)
