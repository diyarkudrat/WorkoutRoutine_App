from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.User
users = db.users

app = Flask(__name__)

@app.route('/workout')
def index():
    return render_template('homepage.html', msg = 'Welcome!')

@app.route('/workout/create_user')
def create_user():
    return render_template('create_account.html')

@app.route('/workout/new_user', methods = ['POST'])
def submit_user():
    user = {
        'name': request.form.get('name'),
        'username': request.form.get('username'),
        'password': request.form.get('password')
    }
    users.insert_one(user)
    return redirect(url_for('create_user'))


if __name__ == '__main__':
    app.run(debug=True)
