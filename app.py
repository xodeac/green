from flask import Flask , escape, url_for, render_template ,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Feature')
def baby():
    return 'feature'


@app.route('/pricing')
def profile():
    return "pricing"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/save', methods=['GET','POST'])
def save():
    if request.method == 'POST':
        fullname = request.form['fullname']
        cnic = request.form['cnic']
        age = request.form['age']
        datalist = [fullname,cnic,age]
        return render_template('index.html' , datalist=datalist)



if __name__ == '__main__':
    app.run()
