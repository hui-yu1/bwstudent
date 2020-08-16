from connect import db

class user(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)          # ID
    name = db.Column(db.String(20), nullable=False)                           # 姓名
    gender = db.Column(db.String(3), nullable=False)                          # 性别
    age = db.Column(db.Integer, nullable=False)                               # 年龄
    english = db.Column(db.Integer, nullable=False)                           # 英语成绩
    language = db.Column(db.Integer, nullable=False)                          # 语文成绩
    math = db.Column(db.Integer, nullable=False)                              # 数学成绩
    total = db.Column(db.Integer, nullable=False)                             # 总成绩

    def __repr__(self):
        return "<user id:{} name:{} gender:{} age:{} english:{} language:{} math:{} total:{}>".format(
            self.id, self.name, self.gender, self.age, self.english, self.language, self.math, self.total)