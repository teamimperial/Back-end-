from flask import redirect, send_from_directory, render_template, Flask, url_for
from auth.login import login_api
from auth.register_student import register_student
from auth.register_company import register_company
from reviews.reviews_students import get_info_about_student
from users.update_company import update_company
from reviews.reviews_company import get_info_about_company
from users.update_student import update_students
from security.session_student import StudentSession

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


@app.route('/sign_up_company', methods=['GET'])
def sign_company_api():
    return render_template('sign-up-c.html')


@app.route('/sign_up_student', methods=['GET'])
def sign_students_api():
    return render_template('sign-up-s.html')


@app.route('/student/logout', methods=['GET'])
def api_logout_student():
    StudentSession.delete_session()
    return redirect('/')


app.register_blueprint(register_student)
app.register_blueprint(login_api)
app.register_blueprint(register_company)
app.register_blueprint(get_info_about_student)
app.register_blueprint(update_company)
app.register_blueprint(get_info_about_company)
app.register_blueprint(update_students)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True)
