
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Miked'}
    posts = [
        {
            'author': {'username': '张三'}, 'body': 'Beautiful day!'
        },
        {
            'author': {'username': '李四'}, 'body': 'The Avengers movie'
        },

        {
            'author': {'username': '李四'}, 'body': 'The Avengers movie'
        },
        {
            'author': {'username': '李四'}, 'body': 'The Avengers movie'
        },
        {
            'author': {'username': '李四'}, 'body': 'The Avengers movie'
        },
        {
            'author': {'username': '李四'}, 'body': 'The Avengers movie'
        }
    ]
    return render_template('index.html', title= 'Home',  user=user, posts= posts)


@app.route('/login', methods = [ 'GET', 'POST'])
def login():
    form =LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remeber_me = {}'.format(
            form.username.date, form.remeber_me.date))
        return redirect(usr_for('/index'))
    return render_template('login.html', title = 'Sign In', form = form)


