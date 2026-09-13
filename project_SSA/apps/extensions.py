from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

db=SQLAlchemy()

# 3. [추가] 빈 소켓 객체를 선언해 둡니다. (app.py와 views.py에서 공유하여 사용)
socketio = SocketIO() 