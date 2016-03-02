m2m
===

flask-sqlalchemy 多对多关系的最佳实践
<hr/>
官方文档采用<code>db.Table</code>的形式定义中间表, 但是很难再使用
flask-sqlalchemy对中间表作出: insert, delete, update 操作.
<hr/>
这个示例程序测试使用<code>类</code>的形式创建中间表。是完全可行的。

    class TeachUser(db.Model):
    """
    老师和用户多对多关系的中间表
    """
    __tablename__ = 'teachusers'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    count = db.Column(db.Integer)

双向查询:

    [student.users for student in teacher.student.all()]
    [teacher.teachers for teacher in student.teacher.all()]

