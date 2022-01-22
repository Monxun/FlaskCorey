from fileinput import filename
from app.models import User, Post
from app.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, flash, redirect, request, make_response
from app import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

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
    return render_template('home.html', title='Home', posts=posts, icon='fa-blog')


@app.route("/about")
def about():
    return render_template('about.html', title='About', icon='fa-info')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return render_template('home.html', title='Home', posts=posts)


@app.route("/account")
@login_required
def account():
    image_file = url_for('static', filename='images/profile/' + current_user.image_file)
    return render_template('account.html', title='Account', icon='fa-user-circle', image_file=image_file)


@app.route("/cookies")
def cookies():
    cookies = request.cookies
    flavor = cookies.get('flavor')
    res = make_response(render_template('cookies.html', cookies=cookies, flavor=flavor, icon='fa-cookie'))
    res.set_cookie(
        'flavor', 
        value='mint chocolate chip',
        max_age=10,
        expires=None,
        path=request.path,
        domain=None,
        secure=False,
        httponly=False
        )
    return res