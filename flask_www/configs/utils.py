import os

from flask import g, request, abort

from flask_www.configs.config import BASE_DIR, NOW


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif'}


def random_word(length):  # 같은 이름의 파일을 다른 이름으로 랜덤하게 만든다.
    import random, string
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def filename_format(now, filename):
    return "{random_word}-{date}-{microsecond}-{extension}".format(
        random_word=random_word(20),
        date=str(now.date()),
        microsecond=now.microsecond,
        extension=os.path.splitext(filename)[1],
    )


def base_file_path(filename):
    """ 앞에 붙는 공통 path 의 역슬래시 때문에 썸머노트 이미지 삭제시 찾지를 못한다.
    static 앞에 / 을 넣으면 이미지가 저장이 안된다. path 는 만들어지지만...."""
    # base_relative_path = "{request_path}/{year}/{month}/{day}/{user_id}/{username}/{filename}".format(
    from flask_www.configs import app
    # base_relative_path = "media/user_images/{request_path}/{year}/{month}/{day}/{filename}".format(
    base_relative_path = "static/media/user_images/{request_path}/{year}/{month}/{day}/{filename}".format(
        request_path=request.path.split('/')[2],  # /로 나누고 2번째(첫번째는 아무값도 없다.)
        year=NOW.year,
        month=NOW.month,
        day=NOW.day,
        random_word=random_word(10),
        filename=filename_format(NOW, filename),
    )
    return base_relative_path


def save_file(now, file):
    if file.filename == '':
        abort(400)
    if file and allowed_file(file.filename):
        filename = filename_format(now, file.filename)#secure_filename(file.filename)
        # relative_path = os.path.join(os.path.relpath(USER_IMG_ROOT), base_file_path(filename))
        relative_path = base_file_path(filename)
        upload_path = os.path.join(BASE_DIR, relative_path)
        os.makedirs(os.path.dirname(upload_path), exist_ok=True)
        file.save(upload_path)
        return relative_path, upload_path   # 템플릿단에서는 relative_path가 사용된다. static 폴더가 있어야 찾아간다.
    else:
        abort(400)

