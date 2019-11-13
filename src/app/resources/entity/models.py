from mongoengine import (
    Document, EmbeddedDocument, StringField, 
    IntField, FloatField, EmbeddedDocumentField
)


class Region(EmbeddedDocument):
    state = StringField()
    start_zipcode = IntField()
    end_zipcode = IntField()
    max_base_items = IntField()
    extra_item_tax = FloatField()


class ZipcodeFee(Document):
    base_price = IntField()
    num_days = IntField()
    region = EmbeddedDocumentField(Region)

