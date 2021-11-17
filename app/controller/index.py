from app import app
from flask import request, render_template, url_for


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
    return 'Hello World!'


@app.route('/static-test')
def static_test():
    # return url_for('static', filename='style.css')
    return url_for('static', filename='style1.css')


@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'GET':
        return render_template('post/add.html')
    else:
        app.logger.debug(request.json)
        print(request.is_json)
        return 'post'


@app.route('/test_json', methods=['GET'])
def test_json():
    return {'name': 'tim'}


@app.route('/test_json2', methods=['GET'])
def test_json2():
    return {'name': 'tim2'}
