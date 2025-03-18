from init import db

class Users(db.Model):
    __tablename__ = 'users'

    # ユーザー情報
    id = db.Column(db.String, primary_key=True, nullable=False, comment="社員番号 (ユーザーIDとして使用)")
    type = db.Column(db.String, nullable=False, default="users", comment="ドキュメントタイプ (固定値: 'users')")
    name = db.Column(db.String, nullable=False, comment="ユーザーの氏名")
    display_name = db.Column(db.String, nullable=True, comment="システム上で表示される名前")
    email = db.Column(db.String, nullable=False, unique=True, comment="社内メールアドレス")
    password_hash = db.Column(db.String, nullable=False, comment="ハッシュ化されたパスワード")
    
    # ストレージ関連
    storage_quota = db.Column(db.Integer, nullable=False, default=-1, comment="ストレージ制限値 (MB) (-1: 無制限)")
    storage_used = db.Column(db.Integer, nullable=False, default=0, comment="現在のストレージ使用量 (0以上)")

    # その他
    affiliation = db.Column(db.JSON, nullable=True, default=[], comment="所属グループの配列 (例: ['営業', 'admin'])")
    last_login_at = db.Column(db.String, nullable=True, comment="最後にログインした日時 (ISO 8601形式)")
    likes = db.relationship('Like', back_populates='user', lazy=True)

    # 論理削除関連
    is_deleted = db.Column(db.Boolean, nullable=False, default=False, comment="論理削除フラグ (true/false)")
    deleted_at = db.Column(db.String, nullable=True, comment="論理削除日時 (ISO 8601形式)")
    deleted_by = db.Column(db.String, nullable=True, comment="論理削除を実行したユーザーのID")

    # 基本項目
    create_at = db.Column(db.String, nullable=False, default="(システム日時)", comment="レコード作成日時 (ISO 8601形式)")
    create_by = db.Column(db.String, nullable=False, comment="レコード作成者")
    update_at = db.Column(db.String, nullable=False, default="(システム日時)", comment="レコード更新日時 (ISO 8601形式)")
    update_by = db.Column(db.String, nullable=False, comment="レコード更新者")
    version = db.Column(db.Integer, nullable=False, default=0, comment="更新回数 (初期値: 0)")
    _ts = db.Column(db.Integer, nullable=False, comment="CosmosDBの内部タイムスタンプ")
    _etag = db.Column(db.String, nullable=False, comment="CosmosDBの排他制御トークン")

    def __repr__(self):
        return f"<User {self.id} - {self.name}>"

class Group(db.Model):
    __tablename__ = 'groups'

    # 基本項目
    create_at = db.Column(db.String, nullable=False, default="(システム日時)", comment="レコード作成日時")
    create_by = db.Column(db.String, nullable=False, comment="レコード作成者")
    update_at = db.Column(db.String, nullable=False, default="(システム日時)", comment="レコード更新日時")
    update_by = db.Column(db.String, nullable=False, comment="レコード更新者")
    version = db.Column(db.Integer, nullable=False, default=0, comment="更新回数 (初期値: 0)")
    _ts = db.Column(db.Integer, nullable=False, comment="CosmosDBの内部タイムスタンプ")
    _etag = db.Column(db.String, nullable=False, comment="CosmosDBの排他制御トークン")

    # 論理削除関連
    is_deleted = db.Column(db.Boolean, nullable=False, default=False, comment="論理削除フラグ (true/false)")
    deleted_at = db.Column(db.String, nullable=True, comment="論理削除日時")
    deleted_by = db.Column(db.String, nullable=True, comment="論理削除を実行したユーザーのID")

    # グループ情報
    id = db.Column(db.String, primary_key=True, nullable=False, comment="グループID (パーティションキー)")
    type = db.Column(db.String, nullable=False, default="groups", comment="ドキュメントタイプ (固定値: 'groups')")
    name = db.Column(db.String, nullable=False, unique=True, comment="グループの名称")
    administrators = db.Column(db.JSON, nullable=False, default=[], comment="グループ管理者の配列")

    def __repr__(self):
        return f"<Group {self.id} - {self.name}>"

class Knowledge(db.Model):
    __tablename__ = 'knowledge'

    # 基本項目
    create_at = db.Column(db.String, nullable=False, default="(システム日時)", comment="レコード作成日時")
    create_by = db.Column(db.String, nullable=False, comment="レコード作成者")
    update_at = db.Column(db.String, nullable=False, default="(システム日時)", comment="レコード更新日時")
    update_by = db.Column(db.String, nullable=False, comment="レコード更新者")
    version = db.Column(db.Integer, nullable=False, default=0, comment="更新回数")
    _ts = db.Column(db.Integer, nullable=False, default=0, comment="CosmosDBの内部タイムスタンプ")
    _etag = db.Column(db.String, nullable=False, default="", comment="CosmosDBの排他制御トークン")

    # 論理削除関連
    is_deleted = db.Column(db.Boolean, nullable=False, default=False, comment="論理削除フラグ")
    deleted_at = db.Column(db.String, nullable=True, comment="論理削除日時")
    deleted_by = db.Column(db.String, nullable=True, comment="論理削除を実行したユーザーのID")

    # ナレッジ情報
    id = db.Column(db.String, primary_key=True, nullable=False, comment="ナレッジID (パーティションキー)")
    type = db.Column(db.String, nullable=False, default="knowledge", comment="ドキュメントタイプ (固定値)")
    title = db.Column(db.String, nullable=False, comment="ナレッジのタイトル")
    content = db.Column(db.String, nullable=False, comment="ナレッジの本文")
    author_id = db.Column(db.String, nullable=False, comment="ナレッジ作成者(パーティションキー)")
    visibility = db.Column(db.String, nullable=False, default="private", comment="公開範囲")
    visible_to_groups = db.Column(db.JSON, nullable=True, default=[], comment="公開先グループ")
    tags = db.Column(db.JSON, nullable=False, default=[], comment="ナレッジのタグ")
    image_path = db.Column(db.JSON, nullable=True, default=[], comment="画像パス")
    links = db.Column(db.JSON, nullable=True, default=[], comment="ナレッジに埋め込まれているリンク")
    editors = db.Column(db.JSON, nullable=False, default=[], comment="共同編集者")
    viewer_count = db.Column(db.Integer, nullable=False, default=0, comment="閲覧数")
    bookmark_count = db.Column(db.Integer, nullable=False, default=0, comment="ブックマーク数")

    def __repr__(self):
        return f"<Knowledge {self.id} - {self.title}>"

# Like model to track user-blogpost likes
class Like(db.Model):
    __tablename__ = 'like'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    knowledge_id = db.Column(db.Integer, db.ForeignKey('knowledge.id'), primary_key=True)
    user = db.relationship('Users', back_populates='likes')
    # knowledge = db.relationship('Knowledge', back_populates='likes')

    def __repr__(self):
        return f"<Likes {self.user_id} - {self.knowledge_id}>"