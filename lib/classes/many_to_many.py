class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Names must be of type str and longer than 0 characters")
        self._name = name

    @property
    def name(self):
        return self._name    


    def articles(self):
        return []

    def magazines(self):
        magazines = set()
        for article in self.articles():
            magazines.add(article.magazine)
        return magazines

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        # Store the article in the list of articles for the author
        self.articles().append(article)
        return article

    def topic_areas(self):
        category_set = set()
        for magazine in self.magazines():
            category_set.add(magazine.category)
        return list(category_set)
        

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or (len(new_name) < 2 or len(new_name) > 16):
            raise ValueError("Names must be between 2 and 16 characters, inclusive")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Categories must be of type str and longer than 0 characters")
        self._category = new_category

    def articles(self):
        return []

    def contributors(self):
        authors = set()
        for article in self.articles():
            authors.add(article.author)
        return authors

    def article_titles(self):
        titles = []
        for article in self.articles():
            titles.append(article.title)
        return titles if titles else None
        

    def contributing_authors(self):
        authors = set()
        for article in self.articles():
            if self.articles().count(article) > 2:
                authors.add(article.author)
        return list(authors) if authors else None