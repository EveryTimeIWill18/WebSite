from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {'author': ' William Robert Murphy',
     'title': 'Blog Post 1',
     'content': 'First Blog Post',
     'date_posted': 'September 25, 2019'}
]



@app.route('/')
def home():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template("about.html", posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
