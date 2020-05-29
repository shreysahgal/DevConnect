from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

from forms import LoginForm, RegisterForm
from models import User, db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
Bootstrap(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect('/dashboard')
        return "wrong again bitch"
        # return "<p>%s</p><p>%s</p>" % (form.username.data, form.password.data)
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_pass = generate_password_hash(form.password.data, method="sha256")
        new_user = User(
            email = form.email.data,
            username = form.username.data,
            password = hashed_pass)
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
        return 'new user has been created'
        # return  "<p>%s</p><p>%s</p><p>%s</p>" % (form.email.data, form.username.data, form.password.data)
    return render_template('signup.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)