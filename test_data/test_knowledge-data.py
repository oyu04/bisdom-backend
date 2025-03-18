import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'backend')))

from utils import add_new_knowledge
from main import create_app  # アプリケーション工場関数をインポート
from init import db  # データベースインスタンスをインポート

class TestAddNewKnowledge(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name='testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        
        # データベースを初期化
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_new_knowledge_success(self):
        test_data = {
            "title": "テスト題目",
            "contents": "<p>これはテストです。</p>",
            "author_id": "test_author"
        }
        with self.app.app_context():
            result, exit_code = add_new_knowledge(test_data)
        print('result', result)
        self.assertEqual(exit_code, 0)
        self.assertIn("登録完了した", result.get("message", ""))

if __name__ == '__main__':
    unittest.main()