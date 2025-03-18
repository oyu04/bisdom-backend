from functools import wraps
from init import db
def transactional(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            db.session.commit()  # トランザクションをコミット
            return result
        except Exception as e:
            db.session.rollback()  # エラー時にロールバック
            raise e
        finally:
            db.session.remove()  # セッションをクリーンアップ
    return wrapper