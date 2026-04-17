# Fake in-memory storage

posts_db = []

def save_post(post):
    posts_db.append(post)

def get_posts():
    return posts_db