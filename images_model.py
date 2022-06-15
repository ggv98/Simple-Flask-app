from database import db


class Images(db.Model):
    """
    Define images data model
    """

    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    sha1 = db.Column(db.String(64), nullable=False)
    width = db.Column(db.Integer(), nullable=False)
    height = db.Column(db.Integer(), nullable=False)
    type = db.Column(db.String(64), nullable=False)

    def __init__(self, sha1, width, height, type):
        self.sha1 = sha1
        self.width = width
        self.height = height
        self.type = type

    def serialize(self):
        """
        Serialize image object
        """
        return {
            "id": self.id,
            "sha1": self.sha1,
            "width": self.width,
            "height": self.height,
            "type": self.type,
        }
