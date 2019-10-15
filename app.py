from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html', msg = 'Welcome!')

@app.route('/workout/create_account')
def create_account():
    return render_template('create_account.html')


if __name__ == '__main__':
    app.run(debug=True)
