from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from blog.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from blog import routes, models

if __name__ == '__main__':
    app.run()


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Entry": models.Entry
    }