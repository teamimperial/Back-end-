from flask import redirect, send_from_directory
from auth.login import login_api
from auth.register_student import register_student
from setting.config import app
from auth.register_company import register_company


@app.route('/')
def hello_world():
    return redirect('static/index.html')


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


app.register_blueprint(register_student)
app.register_blueprint(login_api)
app.register_blueprint(register_company)

if __name__ == '__main__':
    app.run(debug=True)
