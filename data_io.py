import json

def load_posts() -> dict:
    with open("data/posts.json", mode='r') as json_file:
        posts = json.load(json_file)
    return posts
