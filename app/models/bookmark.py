from ..extensions import db

class Bookmark(db.Model):
    __tablename__ = "bookmarks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(1024), nullable=False)
    description = db.Column(db.Text)

    def to_dict(self):
        return {"id": self.id, "title": self.title, "url": self.url, "description": self.description}
