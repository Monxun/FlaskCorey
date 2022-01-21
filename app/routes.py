from app.models import User, Post
from app.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, flash, redirect
from app import app

posts = [
    {
        'author': 'Michael Gibney',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 12, 2022'
    },
    {
        'author': 'Connor Gibney',
        'title': 'Naruto is AWESOME!',
        'content': 'Doo Doo',
        'date_posted': 'April 14, 2022'
    },
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)