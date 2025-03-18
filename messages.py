from enum import Enum
from dataclasses import dataclass

class ApplicationException(Exception):
    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {'message': self.message, 'status_code': self.status_code}

@dataclass
class Messages:
    id:str
    error_code:int
    message:str

class ErrorMessages(Enum):
    ERROR_ID_001E = {'message':"test","id":"01E"}
    ERROR_ID_002E = '{0}が埋め込んでない'
    ERROR_ID_003E = 'ナレッジが見つかりませんでした'
    ERROR_ID_004E = '検索キーワードを入力してください。'
    ERROR_ID_005E = 'ナレッジID不正'
    ERROR_ID_006E = 'htmlのサニタイジングが失敗しました'
    ERROR_ID_007E = 'ユーザーが未設定'
    ERROR_ID_008E = 'タイトルが未設定'
    ERROR_ID_009E = '送信内容が存在していません'
    ERROR_ID_010E = Messages("010E","テスト",404)

    def to_json(self):
        if isinstance(self.value, dict):
            return self.value
        elif isinstance(self.value, Messages):
            return {
                "id": self.value.id,
                "message": self.value.message,
                "error_code": self.value.error_code
            }
        return {"message": str(self.value)}

    def __str__(self):
        if isinstance(self.value, dict):
            return str(self.value.get('message', ''))
        elif isinstance(self.value, Messages):
            return str(self.value.message)
        return str(self.value)

class CreateBy(Enum):
    SYSTEM = "system"
    def __str__(self):
        return self.value