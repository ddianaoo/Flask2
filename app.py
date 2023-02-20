from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About this site')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f"<h1>user {name} {id} </h1>"

if __name__ == '__main__':
    app.run(debug=True)