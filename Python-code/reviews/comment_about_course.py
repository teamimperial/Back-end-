from flask import Blueprint, request, abort

comment_about_course = Blueprint('comment_about_course', __name__)


@comment_about_course.route('/comment/course', methods=['POST'])
def comment_about_course_request():
    if not request.json:
        return abort(400)
    if 'company_login' not in request.json:
        return abort(400)
    if 'review' not in request.json:
        return abort(400)
    company_login= request.json['company_login']
    review = request.json['review']
