import requests
from messages import *
from flask import jsonify
from flask_api import status
from images_model import Images
from PIL import Image, UnidentifiedImageError
from hashlib import sha1
from database import db


def extract_image_data(url):
    """
    Extract image from url and upload image detail to tha database

    Parametes:
    ---------
    url: URL to the resource (string)
    """
    response = requests.get(url, stream=True)

    if response.status_code != 200:
        return URL_NOT_FOUND, status.HTTP_400_BAD_REQUEST

    if "image" in response.headers["content-type"]:
        try:
            im = Image.open(response.raw)
        except UnidentifiedImageError:
            return UNSUPPORTED_URL_CONTENT_TYPE, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE

        image_sha1 = sha1(im.tobytes()).hexdigest()
        entry = Images(image_sha1, im.size[0], im.size[1], im.format)

        db.session.add(entry)
        db.session.commit()
        return jsonify(entry.serialize()), status.HTTP_200_OK

    return UNSUPPORTED_URL_CONTENT_TYPE, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE


def get_images_data():
    """
    Get last 100 records from Images table

    Returns:
    -------
    database image records as json and response status code
    """
    images = Images.query.all()[-100:]
    response = [image.serialize() for image in images]

    return jsonify(response), status.HTTP_200_OK
