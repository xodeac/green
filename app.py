from flask import Flask , escape, url_for, render_template ,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('auth/login.html')







if __name__ == '__main__':
    app.run()
