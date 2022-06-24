
from recursion import db
from datetime import datetime

class Role(db.EmbeddedDocument):
    name = db.StringField(required=True)

class User(db.Document):
    name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    phone = db.StringField()
    password = db.StringField()
    role = db.EmbeddedDocumentField(Role)
    date = db.DateTimeField(default=datetime.utcnow)

    meta = { 'allow_inheritance': True }

class Direction(db.EmbeddedDocument):
    name = db.StringField(required=True)

class Homework(db.EmbeddedDocument):
    title = db.StringField()
    description = db.StringField()
    start_date = db.DateTimeField(default=datetime.utcnow)
    end_date = db.DateTimeField(required=True)

class Subscription(db.EmbeddedDocument):
    current_lesson = db.IntField(default=1)
    max_lesson = db.IntField(default=10)

class Student(User):
    teacher = db.ReferenceField(User)
    subscription = db.EmbeddedDocumentField(Subscription)
    direction = db.EmbeddedDocumentField(Direction)
    homeworks = db.ListField(db.EmbeddedDocumentField(Homework))

class Teacher(User):
    students = db.ListField(db.ReferenceField(Student))


class Event(db.DynamicDocument):
    User = db.ReferenceField(User)
    StartTime = db.StringField()
    EndTime = db.StringField()
    Subject = db.StringField()
    
