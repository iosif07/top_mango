from .. import db

class Item(db.Document):
    item_id = db.SequenceField()
    name = db.StringField()
    cost = db.StringField()
    category = db.StringField()
    description = db.StringField(default="")
    photo_hash = db.StringField()

class Categories(db.Document):
    categ_id = db.SequenceField()
    name = db.StringField()
    count =  db.StringField()

class Orders(db.Document):
    order_id = db.SequenceField()
    description = db.StringField()
    name = db.StringField()
    adress = db.StringField()
    items_id = db.ListField(db.EmbeddedDocumentField('Item'))
