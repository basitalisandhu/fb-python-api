"""
Main Application package.
"""
from flask import Flask

def register_blueprints(app):
  """
  This function registers flask blueprints to flask application
  """
  from .views import main as main_blueprint
  app.register_blueprint(main_blueprint)
  return None


def create_app():
    """
    this function create Flask Application
    """
    app = Flask(__name__)
    register_blueprints(app)
    return app