from flask import Flask
from flask_migrate import Migrate
from app import create_app, db  # Import your app instance and db

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()

