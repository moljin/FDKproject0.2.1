from flask_www.commons.models import BaseModel
from flask_www.configs import db


class Article(BaseModel):
    __tablename__ = 'articles'
    image_path = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
