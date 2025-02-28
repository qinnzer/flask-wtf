from flask import Flask, url_for, request, render_template, redirect

app = Flask(__name__)


@app.route('/<titl>')
@app.route('/index/<titl>')
def index(titl):
    return render_template('base.html', title=titl)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
