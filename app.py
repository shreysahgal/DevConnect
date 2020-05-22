from flask import Flask, g, sessions, render_template, flash, redirect, url_for
from flask_login import LoginManager

import models
import forms

DEBUG = True
PORT = 5000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = ';aklsdfj.DF.JSHD;ksvamnKJALSDKF'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.before_request
def before_request():
    # connect to db before each request
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    # close db connection after request
    g.db.close()
    return response

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None


@app.route('/')
def index():
    return 'yeah'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        flash("Registration complete!", "success")
        models.User.create_user(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data
        )
        return redirect(Url_for('index'))
    render_template('register.html', form=form)


if __name__ == '__main__':
    models.initialize()

    # models.User.create_user(
    #     username='shreysahgal',
    #     email='shreysahgal@gmail.com',
    #     password='password'
    # )

    app.run(debug=DEBUG, host=HOST, port=PORT)