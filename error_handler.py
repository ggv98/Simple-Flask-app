from flask import Blueprint
from flask_api import status
from messages import *

errors = Blueprint("errors", __name__)

# error handler used to handle all unhandled Exceptions
@errors.app_errorhandler(Exception)
def handle_exception(e: Exception):
    return SERVER_UNAVALIABLE, status.HTTP_503_SERVICE_UNAVAILABLE
