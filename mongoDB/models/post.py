import uuid

__author__ = 'Martin Chukaleski '

from database import Database
import datetime


class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id
        self.date = date

    def save_in_mongo(self):
        Database.insert('posts', self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.date
        }

    @classmethod
    def from_mongo(cls, id):
        # return Database.find_one('posts', {'id': id})
        post_data = Database.find_one('posts', {'id': id})
        return cls(blog_id=post_data['blog_id'], title=post_data['title'], content=post_data['content'],
                   author=post_data['author'], date=post_data['created_date'],
                   id=post_data['id'])

    @staticmethod
    def from_blog(blog_id):
        return [post for post in Database.find('posts', {'blog_id': blog_id})]
