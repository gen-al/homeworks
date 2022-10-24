from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from wtforms_alchemy import ModelForm
from flask_wtf import FlaskForm
from wtforms import StringField, validators

app = Flask(__name__)
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'The secret key',
    SQLALCHEMY_DATABASE_URI = 'postgresql://tceh:123@localhost:5432/blog',
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Users\\andre\\Documents\\Projects\\homeworks\\tceh\\homework_15\\blog.db',
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)
app.config['WTF_CSRF_ENABLED'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)

class UserForm(FlaskForm):
    username = StringField(label='username', validators=[
        validators.InputRequired()
    ])

@app.route('/user', methods=['GET', 'POST'])
def add_user():

    if request.method == 'POST':
        form = UserForm(request.form)

        if form.validate():
            user = User(**form.data)
            db.session.add(user)
            db.session.commit()
            return ('OK!', 200)
        
        else:
            return form.data
    else:
        return 'The page is for POST-request only.', 200


with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    app.run()