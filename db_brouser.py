import os
import uuid
from main import app, config, psycopg2, SQLAlchemy, Bcrypt, UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from datetime import datetime
from sqlalchemy.orm import deferred
from sqlalchemy import UUID

# --- Инициализация БД ---
DB_USER = os.environ.get('DB_USER', config.DB_USER)
DB_PASS = os.environ.get('DB_PASS', config.DB_PASS)
DB_HOST = os.environ.get('DB_HOST', config.DB_HOST)
DB_PORT = os.environ.get('DB_PORT', str(config.DB_PORT))
DB_NAME = os.environ.get('DB_NAME', config.DB_NAME)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_pre_ping": True,
}
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)



#-----------------------------------  ACOUNTS ----------------------------------- #
class people(db.Model, UserMixin):
    id = db.Column(db.UUID, unique=True, primary_key=True, default=db.func.gen_random_uuid())
    name = db.Column(db.string(20), nullable=False)
    lastname =db.Column(db.string(20))
    group_number = db.Column(db.Integer, nullable=False)
    group_letter = db.Column(db.String(2), nullable=False)
    campus = db.Column(db.string(30), default="khodynka") # Khodynka - ходынка, Kaplya = Капля #
    level_dostup = db.Column(db.Integer, default=1) # 1 - Обыный пользователь, 2 Админ/Охрана, 3 - Личный аккунт #


    def get_id(self):
        return f"people-{self.id}"