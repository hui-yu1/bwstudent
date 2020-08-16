# 数据库配置
HOSTNAME = '127.0.0.1'
POST = 3306
USERNAME = 'root'
PASSWORD = '010205'
DATABASE = 'bwstudent'

# 连接数据库
db_url = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8mb4" \
    .format(USERNAME,PASSWORD,HOSTNAME,POST,DATABASE)


SQLALCHEMY_DATABASE_URI = db_url
SQLALCHEMY_TRACK_MODIFICATIONS = True