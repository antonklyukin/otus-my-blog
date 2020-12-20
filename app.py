from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('posts'))


@app.route('/posts', methods=['GET'])
def posts():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='localhost',
            port=5000,
            debug=True)
