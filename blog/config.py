import os


class Config:
    SECRET_KEY = 'ca9e7fe2226f618bd2910a09318da40f'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER= 'smtp.office365.com'
    MAIL_USERNAME= os.environ.get('EMAIL_USER')
    MAIL_PASSWORD= os.environ.get('EMAIL_PASS')
    MAIL_PORT = 587
    MAIL_USE_TLS= True
