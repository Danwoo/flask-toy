import os

Base_DIR = os.path.dirname(__file__)

# 데이터 베이스 접속 주소(sqlite 데이터베이스가 사용됨)
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(Base_DIR, 'pybo.db'))

# SQLAlchemy의 이벤트를 처리하는 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False

# CSRF 위협에 대비하는 토큰
SECRET_KEY = "dev"