from sqlalchemy.orm import Session
from . import models, schemas


# ユーザ一覧取得
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
