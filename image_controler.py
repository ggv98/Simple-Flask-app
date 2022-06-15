from flask import Blueprint, request
from flask_api import status
from messages import *
from executor import executor
from image_manager import extract_image_data, get_images_data

images_app = Blueprint("images_app", __name__)


@images_app.route("/api/v1/images", methods=["POST"])
def upload_image_data_from_payload():
    requests_json = request.get_json(force=True)
    if "url" not in requests_json:
        return "URL is missing", status.HTTP_400_BAD_REQUEST

    url = requests_json["url"]

    if "confirm" in requests_json:
        confirm = requests_json["confirm"]
    else:
        confirm = True

    if confirm == True:
        return extract_image_data(url)

    executor.submit(extract_image_data, url)
    return "Accepted", status.HTTP_202_ACCEPTED


@images_app.route("/api/v1/images", methods=["GET"])
def get_image_data():
    return get_images_data()
