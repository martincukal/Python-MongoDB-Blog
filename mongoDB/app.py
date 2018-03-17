__author__ = 'Martin Chukaleski '


from database import Database
from models.post import Post



Database.initialize()

#post1 = Post(blog_id="123",title="Some other random post",content="some random content",author="Martin CH")
#post1.save_in_mongo()

id = '82db07b779874834b8db9859c26483a5'
#posts1 = Database.DATABASE['posts'].find_one({'id': id})

post1 = Post.from_mongo(id)
post2 = Post.from_blog('123')
print(post1)
print('----------------------------')
for post in post2:
    print(post)




#post = Post.from_mongo('e7067252fc7249c7b9e6a1f7c7b6be2c')
#print(post)


