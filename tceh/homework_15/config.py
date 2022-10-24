DEBUG = True
SECRET_KEY = 'The secret key'

# Database settings:
SQLALCHEMY_DATABASE_URI = 'postgresql://tceh:123@localhost:5432/blog'
SQLACCHEMY_COMMIT_ON_TEARDOWN = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLE = False