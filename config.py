class Config:
    SECRET_KEY = 'alejandro'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123123@localhost/project_web'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}