from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField, DateField


class Tag(EmbeddedDocument):
    name = StringField()


class Record(EmbeddedDocument):
    description = StringField()
    done = BooleanField(default=False)


class Note(Document):
    name = StringField()
    created = DateTimeField(default=datetime.now())
    records = ListField(EmbeddedDocumentField(Record))
    tags = ListField(EmbeddedDocumentField(Tag))
    meta = {'allow_inheritance': True}
    
    
class Contacts(Document):
    name = StringField(max_length=25, null=False)
    phone = StringField(max_length=30, null=False)
    birthday = DateField(null=False)
    email = StringField(max_length=30, null=True)
    address = StringField(max_length=30, null=True)
    