from wtforms_alchemy import ModelForm
from app import db

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    article = db.Column(db.String(1000), nullable=False)
    is_visible = db.Column(db.Boolean, default=True)

    def __str__(self):
        return '<article {}>'.format(self.title)


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_id = db.Column(
        db.Integer,
        db.ForeignKey('article.id'),
        nullable=False,
        index=True
    )

    article = db.relationship(Article, foreign_keys=[article_id, ])

    comment = db.Column(db.String(500), nullable=False)
    is_visible = db.Column(db.Boolean, default=True)

    def __str__(self):
        return '<comment {}>'.format(self.comment)