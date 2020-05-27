from flask import current_app
import traceback


class Logger(object):
    @property
    def extra(self):
        return {'trace_id': None}

    @property
    def info(self):
        return current_app.logger.info

    @property
    def info_exception(self):
        return current_app.logger.info

    @property
    def error(self):
        return current_app.logger.error

    @property
    def exception(self):
        return current_app.logger.exception

    @property
    def traceback(self):
        return traceback.format_exc


logger = Logger()

if __name__ == '__main__':
    pass
