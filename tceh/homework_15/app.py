from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

import config as config
#from models import *
#from forms import ArticleForm, CommentForm

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)
# app.config.update(
#     DEBUG = True,
#     SECRET_KEY = 'The secret key',

#     # Database settings:
#     SQLALCHEMY_DATABASE_URI = 'postgresql://tceh:123@localhost:5432/blog',
#     SQLALCHEMY_TRACK_MODIFICATIONS = False,

#     WTF_CSRF_ENABLE = False
# )

db = SQLAlchemy(app)


@app.route('/article', methods=['GET', 'POST'])
def add_article():
    from models import Article
    from forms import ArticleForm

    if request.method == 'POST':
        form = ArticleForm(request.form)

        if form.validate():
            article = Article(**form.data)
            db.session.add(article)
            db.session.commit()
            return ('OK!', 200)
        
        else:
            return ('The form has mistakes!', 400)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()

    app.run()
    
    # a = Article(
    #     title = 'First article.',
    #     article = 'This is the first article.'
    #     )
    
    # db.session.add(a)

    # c = Comment(
    #     article = a,
    #     comment = 'This is the first comment'
    # )

    # db.session.add(c)
    # db.session.commit()

    # all_comments = Comment.query.all()
    # for comment in all_comments:
    #     print(comment.id, comment.article_id, comment.comment)
    #     print(comment.article.id, comment.article.title, comment.article.article)
    #     print()