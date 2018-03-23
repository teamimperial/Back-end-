from flask import session, render_template


class StudentSession:
    @classmethod
    def check_in_session_student(cls):
        value = 0
        if 'student' in session:
            login_student = session['student']
            return login_student
        else:
            return value

    @classmethod
    def delete_session(cls):
        session.pop('student', None)