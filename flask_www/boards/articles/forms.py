from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length


class ArticleForm(FlaskForm):
    image_path = FileField("이미지", validators=[DataRequired()], render_kw={"placeholder": "이미지"})
    subject = StringField("타이틀", validators=[DataRequired('제목은 필수입력 항목입니다.'), Length(min=4, max=100)], render_kw={"placeholder": "타이틀"})
    content = TextAreaField("내용", validators=[DataRequired('내용은 필수입력 항목입니다.')], render_kw={"placeholder": "내용"})
