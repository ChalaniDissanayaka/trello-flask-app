from init import db, ma
from marshmallow import fields

class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    date = db.Column(db.Date) # Date Created
    status = db.Column(db.String)
    priority = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship('User', back_populates='cards')

    # {
    #     id: 1,
    #     title: "Card 1",
    #     description: "Card 1 desc",
    #     date: "..",
    #     status: "..",
    #     priority: "..",
    #     user_id: 1,
    #     user: {
    #       id: 1,
    #       name: "User 1",
    #       email: "user1@email.com",
    #   }
    # }

class CardSchema(ma.Schema):

    user = fields.Nested('UserSchema', only=["id", "name", "email"])

    class Mete:
        fields = ( "id", "title", "description", "date", "status", "priority", "user")

card_schema = CardSchema()
cards_schema = CardSchema(many=True)