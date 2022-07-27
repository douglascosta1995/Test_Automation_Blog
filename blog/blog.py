
class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.post = []

    def __repr__(self):
        pass

    def create_post(self, title, content):
        self.title = title
        self.post = content

    def json(self):
        pass