# coding: utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SSL_DISABLE = False
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_MAX_OVERFLOW = 100
    PAGE_SIZE = 40
    ALERT_PAGE_SIZE = 5
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ECHO = True
    SLOW_DB_QUERY_TIME = 0.5
    # other
    LOGICAL_USER = 'tidbuser'
    LOGICAL_AUTH = 'tidbHrfjYM3cA'
    # template
    STATIC_PATH = '../../dist/static/'
    TEMPLATE_PATH = '../../dist/'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    #
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://tidbhachathon:tidbhachathon2019@hostname/tidbops?charset=utf8mb4'
    SQLALCHEMY_BINDS = {
        'tidbops': 'mysql+pymysql://tidbhachathon:tidbhachathon2019@hostname/tidbops?charset=utf8mb4'
    }


class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    #    'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False
    #
    DEBUG = True
    SQLALCHEMY_ECHO = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #   'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://tidbhachathon:tidbhachathon2019@hostname/tidbops?charset=utf8mb4'
    SQLALCHEMY_BINDS = {
        'tidbops': 'mysql+pymysql://tidbhachathon:tidbhachathon2019@hostname/tidbops?charset=utf8mb4'
    }

class ProductionConfig(Config):
    # database
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://tidbhachathon:xxxxxxx@hostname/tidbops?charset=utf8mb4'
    SQLALCHEMY_BINDS = {
        'tidbops': 'mysql+pymysql://tidbhachathon:xxxxxxx@hostname/tidbops?charset=utf8mb4'
    }

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
