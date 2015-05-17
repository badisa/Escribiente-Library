from django.db import models


class BookManager(models.Manager):
    def new_book(self, isbn, note=False):
        isbn = str(isbn)
        if len(isbn) == 10 or len(isbn) == 13:
            data = Book.get_data(isbn)
            book = self.create(
                title=data.get('title'),
                published=data.get('published'),
                cover=data.get('cover'),
                descript=data.get('description'),
                isbn_10=data.get('isbn_10'),
                isbn_13=data.get('isbn_13')
            )
            if note:
                book.note = note
                book.save()
            return book
        else:
            raise self.IsbnException(
                'Not 10 or 13 Chars Long: %s Chars' % len(isbn))

    class IsbnException(Exception):
        pass


class Book(models.Model):
    title = models.CharField(max_length=80, blank=True, default='')
    published = models.CharField(max_length=30)
    copies = models.IntegerField(default=0)
    checked_out = models.IntegerField(default=0)
    isbn_10 = models.CharField(max_length=10)
    isbn_13 = models.CharField(max_length=10)
    cover = models.TextField(blank=True, null=True)
    descript = models.TextField(default='No Description')
    note = models.TextField(blank=True, null=True)

    objects = BookManager()

    # def authors(self):
    #     return Author.objects.filter(
    #         content=self)

    @staticmethod
    def get_data(isbn):
        import urllib
        import json
        isbn = str(isbn)
        base_url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
        url = base_url + isbn
        response = urllib.urlopen(url).read()
        json_data = json.loads(response)
        json_data = json_data['items'][0]['volumeInfo']
        book_data = {}
        book_data['authors'] = json_data['authors']
        book_data['title'] = json_data['title']
        book_data['published'] = json_data['publishedDate']
        book_data['description'] = json_data['description']
        book_data['cover'] = json_data['imageLinks']['thumbnail']
        book_data['isbn_10'] = json_data['industryIdentifiers'][0]['identifier']
        book_data['isbn_13'] = json_data['industryIdentifiers'][1]['identifier']
        return book_data
