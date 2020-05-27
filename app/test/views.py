from flask import jsonify
from utils.logger import logger
from . import test
from datetime import datetime

@test.route('/test/<string:name>')
def test1(name):
    logger.info(f"request name is {name}, localtime is {datetime.now()}")
    return jsonify(f"hello {name}")