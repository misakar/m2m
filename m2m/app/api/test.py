# coding: utf-8

"""
--> test api

    测试flask-sqlalchemy定义的m2m

"""

from . import api
from app.models import Teacher, User
import json


@api.route('/teacher/<int:id>/students/', methods=['GET'])
def get_teacher_id_students(id):
    """获取特定老师的所有学生数据"""
    teacher = Teacher.query.get_or_404(id)
    users = teacher.student.all()
    return json.dumps([
        user.users.to_json() for user in users
    ], indent=1), 200


@api.route('/student/<int:id>/teachers/', methods=['GET'])
def get_student_id_teachers(id):
    """反向同上"""
    pass


