from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy


import config as config
#from models import *
#from forms import ArticleForm, CommentForm

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)


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
            return render_template(
                'article.txt',
                title=article.title,
                article=article.article
            )
        
        else:
            return ('The form has mistakes!', 400)
    else:
        return 'This page is for POST requests only'


@app.route('/comment', methods=['GET', 'POST'])
def add_comment():
    from models import Comment
    from forms import CommentForm

    if request.method == 'POST':
        form = CommentForm(request.form)

        if form.validate():
            comment = Comment(**form.data)
            db.session.add(comment)
            db.session.commit()
            return render_template(
                'one_comment.txt',
                title=comment.article.title,
                article=comment.article.article,
                comment=comment.comment
            )
        
        else:
            return ('The form has mistakes!', 400)
    else:
        return 'This page is for POST requests only'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()

    app.run()
