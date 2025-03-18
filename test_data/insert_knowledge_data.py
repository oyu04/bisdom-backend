import requests

def test_add_new_knowledge_success():
    url = "http://127.0.0.1:8080/add-knowledge"
    payload = {
        "title": "テスト題目",
        "contents": "<p>これはテストです。</p>",
        "author_id": "test_author"
    }

    response = requests.post(url, json=payload)

    print("Status code:", response.status_code)
    print("Response:", response.json())

if __name__ == '__main__':
    test_add_new_knowledge_success()