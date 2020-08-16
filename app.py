from flask import Flask, request, render_template, url_for, redirect
from models import user
from connect import db
from sqlalchemy import or_, desc

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)

@app.route('/', endpoint='index', methods=['post','get'])
def index():
    user_info = user.query.all()
    return render_template('index.html',user_info=user_info)

@app.route('/adds/', endpoint='adds', methods=['post','get'])
def adds():
    if request.method == 'POST':
        get_name = request.form.get('name')
        get_gender = request.form.get('gander')
        get_age = request.form.get('age')
        get_english = request.form.get('english')
        get_language = request.form.get('language')
        get_math = request.form.get('math')
        if get_name and get_gender and get_age and get_english and get_language and get_math:
            get_total = int(get_english) + int(get_language) + int(get_math)
            data = user(name=get_name, gender=get_gender, age=get_age, english=get_english, language=get_language, math=get_math, total=get_total)
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('add_alter.html',alter='请填写完整')
    return render_template('add_alter.html')

@app.route('/dels/', endpoint='dels', methods=['post','get'])
def dels():
    dels_id = request.args.get('dels_id')
    if dels_id:
        user.query.filter(user.id == dels_id).delete()
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/alter/', endpoint='alter', methods=["GET", "POST"])
def alter():
    alter_id = request.args.get('alter_id')
    if alter_id:
        data = user.query.filter(user.id == alter_id)
        if request.method == 'POST':
            get_name = request.form.get('name')
            get_gender = request.form.get('gander')
            get_age = request.form.get('age')
            get_english = request.form.get('english')
            get_language = request.form.get('language')
            get_math = request.form.get('math')
            if get_name and get_gender and get_age and get_english and get_language and get_math:
                get_total = int(get_english) + int(get_language) + int(get_math)
                data.update({'name':get_name, 'gender':get_gender, 'age':get_age, 'english':get_english, 'language':get_language, 'math':get_math, 'total':get_total})
                db.session.commit()
                return redirect(url_for('index'))
            else:
                return render_template('add_alter.html', alter='*请填写完整')
        return render_template('add_alter.html', data=data)

@app.route('/find/', endpoint='find', methods=["GET", "POST"])
def find():
    if request.method == 'POST':
        info = request.form.get('info')
        if info:
            data = user.query.filter(or_(user.id == info, user.name.like('%' + info + '%'))).all()
            if data:
                return render_template('index.html', data=data)
            else:
                return render_template('index.html', alter='未找到相关信息')
    return render_template('index.html')

@app.route('/sortord/', endpoint='sortord', methods=["GET", "POST"])
def sortord():
    sort_id = request.args.get('sort_id')
    print(sort_id)
    if sort_id:
        data1 = user.query.order_by(desc(sort_id))
        print(data1)
        return render_template('index.html', data1=data1)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
