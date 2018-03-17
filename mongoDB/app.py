__author__ = 'Martin Chukaleski '


from database import Database
from models.post import Post

Database.initialize()

post1 = Post(blog_id="123",title="Some random post",content="some random content",author="Martin CH")


post1.save_in_mongo()
