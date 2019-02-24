from .instagram import process_data, scrape
from pathlib import Path

class Account:
    def __init__(self, handle):
        self.handle = handle
        self.posts, self.ok = self.populate()
        self.posts.sort(key=lambda x: x["timestamp"])
    
    def populate(self):
        p = Path("data/{}.json".format(self.handle))
        if p.exists():
            return process_data(p)
        else:
            return scrape(self.handle, p)

    @property
    def url(self):
        return "https://www.instagram.com/{}".format(self.handle)

    def to_json(self):
        return {"url":self.url, "handle":self.handle, "posts":self.posts}

def load_all():
    paths = Path("data").glob("*.json")
    d = {}
    for p in paths:
        d[p.stem] = Account(p.stem)
    return d
