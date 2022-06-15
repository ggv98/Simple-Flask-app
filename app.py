from flask import Flask
from database import db
from error_handler import errors
from image_controller import images_app
from executor import executor
from flask_swagger_ui import get_swaggerui_blueprint

# Create Flask application
app = Flask("Images")

# Register configurations
app.config.from_object("config.Config")

# Register blueprints
app.register_blueprint(errors)
app.register_blueprint(images_app)

# initialize database and executor
executor.init_app(app)
db.init_app(app)

# Create swagger endpoint
swaggerui_blueprint = get_swaggerui_blueprint(
    "/api/docs",
    "/static/swagger.json",
    config={"app_name": "Flask API"},
)
app.register_blueprint(swaggerui_blueprint)

if __name__ == "__main__":
    # create database and tables if missing
    with app.app_context():
        db.create_all()
        db.session.commit()

    # run application
    app.run("0.0.0.0", port=5000, debug=True)
