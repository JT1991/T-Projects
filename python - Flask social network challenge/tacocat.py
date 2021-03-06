from flask import (Flask, g, render_template, flash, redirect, url_for,
                   abort)
from flask.ext.login import (LoginManager, login_user, logout_user,
                             login_required, current_user)
from flask.ext.bcrypt import check_password_hash
import models
import forms



DEBUG = True
PORT = 8060
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'sdgedyh75ew463452r1ascfsadasd@@D:E@:WR@P/*2>x'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
  try:
    return models.User.get(models.User.id == userid)
  except model.DoesNotExist:
    return None

@app.before_request
def before_request():
  g.db = models.DATABASE
  g.db.connect()
  g.user = current_user

@app.after_request
def after_request(response):
  g.db.close()
  return response

@app.route('/register', methods=('GET', 'POST'))
def register():
  form = forms.RegisterForm()
  if form.validate_on_submit():
    flash("Registration sucessful", "success")
    models.User.create_user(
      email = form.email.data,
      password = form.password.data
    )
    return redirect(url_for('index'))
  return render_template('register.html', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
  form = forms.LoginForm()
  if form.validate_on_submit():
    try:
      user = models.User.get(models.User.email == form.email.data)
    except models.DoesNotExist:
      flash('Email or password does not match', 'error')
    else:
      if check_password_hash(user.password, form.password.data):
        login_user(user)
        flash('Login successful.', 'success')
        return redirect(url_for('index'))
      else:
        flash('Email or password does not match.', 'error')
  return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
  logout_user()
  flash('Logged out.', 'success')
  return redirect(url_for('index'))

@app.route('/taco', methods=('GET', 'POST'))
@login_required
def taco():
  form = forms.TacoForm()
  if form.validate_on_submit():
    models.Taco.create(protein = form.protein.data,
                       shell = form.shell.data,
                       cheese = form.cheese.data,
                       extras = form.extras.data.strip(),
                       user = g.user._get_current_object()
                      )
    flash('Taco posted.', 'successs')
    return redirect(url_for('index'))
  return render_template('taco.html', form=form)
  

@app.route('/')
def index():
  tacos= models.Taco.select().limit(100)
  return render_template('index.html', tacos = tacos)


if __name__ == '__main__':
  models.initialize()
  try:
      models.User.create_user(
        email='joshthorn91@gmail.com',
        password='mhlover',
        admin=True
      )
  except ValueError:
    pass
  app.run(debug=DEBUG, host=HOST, port=PORT) 
