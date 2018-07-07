from pymongo import MongoClient
mongodb_client = MongoClient()

db = mongodb_client.mongodb_test

posts = db.posts
db.posts.delete_many({}) # Delete posts from a previous test session from the database

post_1 = {
    "Title" : "First Test with Python and MongoDB",
    "Content" : "This was done for day 8 of #100DaysOfCode",
    "Author" : "Yashas Lokesh"  
}

post_2 = {
    "Title" : "Gotham needs a hero",
    "Content" : "Gotham needs someone to hunt, for someone to be the bad guy. I can be that guy.",
    "Author" : "Bruce Wayne"
}

post_3 = {
    "Title" : "#100DaysOfCode",
    "Content" : "Follow me on my first #100DaysOfCode journey as I learn python and all of its capabilities for incredible computing",
    "Author" : "Yashas Lokesh"
}

post_4 = {
    "Entry Name" : " My first MongoDB project",
    "Date" :  "July 6th, 2018",
    "Author" : "Yashas Lokesh"
}

post_5 = {
    "Description" : "Some statistics",
    "Stat_One" : "5/4 of people hate fractions!",
    "Stat_Two" : "200% of people say this treatment works for them!",
    "Author" : "Clark Kent"
}

single_insert = posts.insert_one(post_1)
many_inserts = posts.insert_many([post_2, post_3, post_4, post_5])

karens_post = posts.find_one({"Author" : "Karen"})
print(karens_post)

yashas_posts = posts.find({"Author" : "Yashas Lokesh"})
for post in yashas_posts:
    print(post)

from mongoengine import *
connect("mongodb_test")

import datetime

class BlogPost(Document):
    title = StringField(required = True, max_length=50)
    subtitle = StringField(required = True, max_length=100)
    author = StringField(required = True, max_length=20)
    language_used = StringField(required = True, max_length=20)
    content = StringField(required = True)
    published_date = DateTimeField(default=datetime.datetime.now)

blog_post_1 = BlogPost(
    title = "First MongoDB supported blog post...",
    subtitle = "This is my first attempt at using mongoengine",
    author = "Yashas Lokesh",
    language_used = "Python",
    content = "I used pymongo to first add posts and retrieve posts from a local MongoDB instance. Then I started to "
            "learn how to use mongoengine and classes to easily store and retrieve data following certain pre-defined "
            "models. The only downside I see currently for using MongoDB is that we can't take back a 'save' call after"
            " it has been performed, so SQL databases may be more useful if you would like to take back changes that "
            "have been made."
)

blog_post_1.save()
blog_post_1.title = "First-time local MongoDB usage" # Using a more mature title
blog_post_1.save()



