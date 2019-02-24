from .instagram import process_data, scrape
from pathlib import Path

class Account:
    def __init__(self, handle):
        self.handle = handle
        try:
            self.posts = self.populate()
        except Exception:
            raise Exception("Account not found")
    
    def populate(self):
        p = Path("data/{}.json".format(self.handle))
        if p.exists():
            return process_data(p)
        else:
            res, ok = scrape(self.handle, p)
            if not ok:
                raise Exception("Account not found")
            return res

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
