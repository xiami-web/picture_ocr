import logging
import os
from conf.conf_log import ConfLog


class Config():
    APP_NAME = "picture_ocr"
    DEBUG = True
    URL_PREFIX_API = f'/api/{APP_NAME}'
    FLASK_POSTS_PER_PAGE = 10
    FLASK_TOKEN_EXPIRE = 86400

    # 中文输出真正的中文，而不是ascii 字符码
    JSON_AS_ASCII = False
    # 如果设置为True，则关闭浏览器session就失效
    SESSION_PERMANENT = False
    # 是否对发送到浏览器上session的cookie值进行加密
    SESSION_USE_SIGNER = False
    SESSION_KEY_PREFIX = 'session:'
    # session长期有效，则设定session生命周期，整数秒
    PERMANENT_SESSION_LIFETIME = 3600
    SESSION_REFRESH_EACH_REQUEST = True

    # mysql配置
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI') or 'mysql+pymysql://?charset=utf8'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # log about
    # _LOG_PATH_ERROR = '/var/log/{}/error'.format(APP_NAME)
    # _LOG_PATH_INFO = '/var/log/{}/info'.format(APP_NAME)

    # log xiami
    _LOG_PATH_ERROR = '/Users/mac/var/log/{}/error'.format(APP_NAME)
    _LOG_PATH_INFO = '/Users/mac/var/log/{}/info'.format(APP_NAME)

    os.path.exists(_LOG_PATH_ERROR) or os.makedirs(_LOG_PATH_ERROR)
    os.path.exists(_LOG_PATH_INFO) or os.makedirs(_LOG_PATH_INFO)
    LOG_PATH_ERROR = os.path.join(_LOG_PATH_ERROR, '{}.error.log'.format(APP_NAME))
    LOG_PATH_INFO = os.path.join(_LOG_PATH_INFO, '{}.info.log'.format(APP_NAME))
    LOG_FILE_MAX_BYTES = 100 * 1024 * 1024
    LOG_FILE_BACKUP_COUNT = 10
    LOG_FORMATTER = logging.Formatter('%(asctime)s!%(levelname)s!%(process)d!%(thread)d!'
                                      '%(pathname)s!%(lineno)s!%(message)s!')

    def load_conf(self, app):
        app.config.from_object(self)
        ConfLog(app, self.LOG_PATH_ERROR, self.LOG_PATH_INFO, self.LOG_FILE_MAX_BYTES,
                self.LOG_FILE_BACKUP_COUNT, self.LOG_FORMATTER, self.LOG_FORMATTER).init()


class DevConfig(Config):
    pass


class LocalConfig(Config):
    pass


class SitConfig(Config):
    pass


class PreConfig(Config):
    DEBUG = False

    def load_conf(self, app):
        app.logger.handlers = []
        super(PreConfig, self).load_conf(app)


class ProdConfig(PreConfig):
    pass


CONFIG = {
    DevConfig.__name__: DevConfig,
    LocalConfig.__name__: LocalConfig,
    SitConfig.__name__: SitConfig,
    PreConfig.__name__: PreConfig,
    ProdConfig.__name__: ProdConfig
}
