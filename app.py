from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# secret key from secrets.random_hex(16)
app.config['SECRET_KEY'] = '1f10cf6f94cd63cf79c7ba2ce62ea502'

posts = [
    {'author': 'William Robert Murphy',
     'title': 'Blog Post 1',
     'content': 'First Blog Post',
     'date_posted': 'September 25, 2019'},

    {'author': 'William Robert Murphy',
     'title': 'Blog Post 2',
     'content': 'Second Blog Post',
     'date_posted': 'September 25, 2019'
     }
]



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template("about.html", title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account has been created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)