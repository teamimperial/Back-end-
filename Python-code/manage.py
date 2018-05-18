from flask import redirect, send_from_directory, render_template, Flask, session, request, jsonify
from auth.login import login_api
from auth.register_student import register_student
from auth.register_company import register_company
from reviews.reviews_students import get_info_about_student
from users.update_company import update_company
from reviews.reviews_company import get_info_about_company
from users.update_student import update_students
from security.session_student import StudentSession
from security.session_company import CompanySession
from reviews.edit_redirect import GetSessionStudent, GetSessionCompany
from courses.create_courses import create_course
from courses.get_courses import get_courses
from courses.get_courses_all import get_all_courses
from courses.get_one_course import get_one_course
from courses.search_courses import search_courses
from courses.courses_apply import apply_on_course
from courses.courses_studnet import courses_student
from courses.approve_students import approve_student, set_status_students_on_course
from reviews.comment_about_student import comment_about_student
from reviews.comment_about_course import comment_about_course
from reviews.delete_comment import delete_comment_company

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


@app.route('/sign_up_company', methods=['GET'])
def sign_company_api():
    return render_template('sign-up-c.html')


@app.route('/about_us', methods=['GET'])
def about_us_url():
    if 'student' in session or 'company' in session:
        return render_template('about-us.html')
    else:
        return render_template('about-us-unlog.html')


@app.route('/sign_up_student', methods=['GET'])
def sign_students_api():
    return render_template('sign-up-s.html')


@app.route('/company/logout', methods=['GET'])
def api_logout_company():
    CompanySession.delete_session_company()
    return redirect('/')


@app.route('/edit/student', methods=['GET'])
def api_edit_student():
    return render_template('edit-s.html')


@app.route('/edit/company', methods=['GET'])
def api_edit_company():
    return render_template('edit-c.html')


@app.route('/student/logout', methods=['GET'])
def api_logout_student():
    StudentSession.delete_session()
    return redirect('/')


@app.route('/company/return')
def api_redirect_company():
    result = GetSessionCompany.api_get_company_session()
    return redirect('/user/company/' + result)


@app.route('/student/return')
def api_redirect_student():
    result = GetSessionStudent.api_get_student_session()
    return redirect('/user/student/' + result)


@app.route('/logout')
def api_logout():
    if 'student' in session:
        return redirect('/student/logout')
    if 'company' in session:
        return redirect('/company/logout')


@app.route('/returnToProfile')
def api_return_to_profile():
    if 'student' in session:
        result = GetSessionStudent.api_get_student_session()
        if result != 0:
            return redirect('/user/student/' + result)
        else:
            return 'Please log in'
    if 'company' in session:
        result = GetSessionCompany.api_get_company_session()
        if result != 0:
            return redirect('/user/company/' + result)
        else:
            return 'Please log in'


@app.route('/error/<message>')
def api_error(message):
    return render_template('error.html', message=message)


@app.route('/courses')
def api_redirect_courses():
    if 'student' in session:
        return redirect('/student/course')
    if 'company' in session:
        return redirect('/company/course')


app.register_blueprint(register_student)
app.register_blueprint(login_api)
app.register_blueprint(register_company)
app.register_blueprint(get_info_about_student)
app.register_blueprint(update_company)
app.register_blueprint(get_info_about_company)
app.register_blueprint(update_students)
app.register_blueprint(create_course)
app.register_blueprint(get_courses)
app.register_blueprint(get_all_courses)
app.register_blueprint(get_one_course)
app.register_blueprint(search_courses)
app.register_blueprint(apply_on_course)
app.register_blueprint(courses_student)
app.register_blueprint(approve_student)
app.register_blueprint(set_status_students_on_course)
app.register_blueprint(comment_about_student)
app.register_blueprint(comment_about_course)
app.register_blueprint(delete_comment_company)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(debug=True, port=90)
