import uuid

__author__ = 'Martin Chukaleski '

from database import Database
import datetime

class Post(object):

    def __init__(self,blog_id,title,content,author,date=datetime.datetime.utcnow(),id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id
        self.date = date

    def save_in_mongo(self):
        Database.insert('posts',self.json())

    def json(self):
        return {
            'id':self.id,
            'blog_id':self.blog_id,
            'author':self.author,
            'content': self.content,
            'title':self.title,
            'created_date':self.date
        }

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts',query={'id': id})

    @staticmethod
    def from_blog(id):
        return[post for post in Database.find(collection='posts', query={'blod_id': id})]


