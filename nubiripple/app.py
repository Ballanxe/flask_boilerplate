
from flask import Flask, abort

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery

from .config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
# silence the deprecation warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def testdb():

    try:
        db.engine.connect()
        return '<h1>It works.</h1>'

    except Exception as e:
        abort(500, e)


if __name__ == '__main__':
    app.run()
