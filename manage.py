import os
from flask_script import Manager, Server
from app import create_app

Environment = os.getenv('FLASK_CONFIG') or 'DevConfig'
app = create_app(Environment)
manager = Manager(app)

app.logger.info(f"current run environment====>{Environment}")
app.logger.info(f"current run mysql_address====>{app.config.get('SQLALCHEMY_DATABASE_URI') or None}")


manager.add_command("server", Server(host='0.0.0.0', port=5007))

if __name__ == '__main__':
    manager.run()
