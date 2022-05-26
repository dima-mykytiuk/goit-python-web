"""Imports for models"""
from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField
from mongoengine.fields import ListField, StringField, DateField


class Tag(EmbeddedDocument):
    """Model for tag"""

    name = StringField()


class Record(EmbeddedDocument):
    """Model for record"""

    description = StringField()
    done = BooleanField(default=False)


class Note(Document):
    """Model for note"""

    name = StringField()
    created = DateTimeField(default=datetime.now())
    records = ListField(EmbeddedDocumentField(Record))
    tags = ListField(EmbeddedDocumentField(Tag))
    meta = {"allow_inheritance": True}


class Contacts(Document):
    """Model for contacts"""

    name = StringField(max_length=25, null=False)
    phone = StringField(max_length=30, null=False)
    birthday = DateField(null=False)
    email = StringField(max_length=30, null=True)
    address = StringField(max_length=30, null=True)
