from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The avengers movie was sweet!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)