import os


class Config:

    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = '6facf481366edef0220e0f6dd103dad6'
    SECRET_KEY =   'kepha'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rkepha:kr@localhost/watchlist'


class ProdConfig(Config):
    pass




class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
