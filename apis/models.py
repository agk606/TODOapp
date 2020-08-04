import datetime
from peewee import *

db = SqliteDatabase('tasks.db')


class BaseModel(Model):
    class Meta:
        database = db


class Task(BaseModel):
    title = CharField(150, unique=True)
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    def task_info(self):
        data = {
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at,
        }
        return data
