from app import app
from flask import request, render_template, url_for

from app.util import response, common


@app.route('/')
@app.route('/index')
def index():
    return 'hello world ~~'


@app.route('/user')
@app.route('/user/<int:uid>')
def user(uid=None):
    return 'user id: %d' % uid


@app.route('/user/profile/<int:uid>')
def user_profile(uid=None):
    return render_template('user/profile.html', uid=uid)


@app.route('/post', methods=['POST', 'GET'])
def post():
    if request.method == 'GET':
        return render_template('post/add.html')
    else:
        common.log('post-add').info(request)
        return response.success({
            'name': request.form['name'],
            'age': request.form['age'],
        })


@app.route('/css-test')
def static_test():
    return url_for('static', filename='css/style.css')


@app.route('/test_json', methods=['GET'])
def test_json():
    return {'name': 'tim'}
