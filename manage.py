from flask import redirect, render_template, url_for
from auth.login import login_api
from auth.register_student import register_student
from setting.config import app
from auth.register_company import register_company
from reviews.reviews_students import get_info_about_student
from users.update_company import update_company

@app.route('/')
def first_go():
    return app.send_static_file('static/index.html')


app.register_blueprint(register_student)
app.register_blueprint(login_api)
app.register_blueprint(register_company)
app.register_blueprint(get_info_about_student)
app.register_blueprint(update_company)

if __name__ == '__main__':
    app.run(debug=True)
