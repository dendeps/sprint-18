from django.db import models
from author.models import Author



class Book(models.Model):
    """
        This class represents an Author. \n
        Attributes:
        -----------
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        param authors: list of Authors
        type authors: list->Author
    """
    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)
    count = models.IntegerField(default=10)
    year=models.IntegerField(default=1900)
    issue_date = models.DateField(null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='book')

    def __str__(self):
        """
        Magic method is redefined to show all information about Book.
        :return: book id, book name, book description, book count, book authors
        """
        return str(self.to_dict())[1:-1]

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f'{self.__class__.__name__}(id={self.pk})'

    @staticmethod
    def get_by_id(book_id):
        """
        :param book_id: SERIAL: the id of a Book to be found in the DB
        :return: book object or None if a book with such ID does not exist
        """
        try:
            return Book.objects.get(pk = book_id)
        except Book.DoesNotExist:
            return None

    @staticmethod
    def delete_by_id(book_id):
        """
        :param book_id: an id of a book to be deleted
        :type book_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        try:
            delete_book = Book.objects.get(pk = book_id)
            delete_book.delete()
            return True
        except Book.DoesNotExist:
            return False

    @staticmethod
    def create(name, description, count=10, authors=None):
        """
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        param authors: list of Authors
        type authors: list->Author
        :return: a new book object which is also written into the DB
        """
        if len(name) <= 128:
            book_created = Book.objects.create(name = name, description = description, count = count)
            if authors:
                book_created.add_authors(authors)
            return book_created

    def to_dict(self):
        """
        :return: book id, book name, book description, book count, book authors
        :Example:
        | {
        |   'id': 8,
        |   'name': 'django book',
        |   'description': 'bla bla bla',
        |   'count': 10',
        |   'authors': []
        | }
        """
        book_dict = {'id': self.pk,
                    'name': self.name,
                    'description': self.description,
                    'count': self.count,
                    'authors': [author.pk for author in self.authors.all()]}
        return book_dict

    def update(self, name=None, description=None, count=None):
        """
        Updates book in the database with the specified parameters.\n
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        :return: None
        """
        if name and len(name) <= 128:
            self.name = name
            self.save()
        if description:
            self.description = description
            self.save()
        if count and count <= 10:
            self.count = count
            self.save()

    def add_authors(self, authors):
        """
        Add  authors to  book in the database with the specified parameters.\n
        param authors: list authors
        :return: None
        """
        for author in authors:
            self.authors.add(author)

    def remove_authors(self, authors):
        """
        Remove authors to  book in the database with the specified parameters.\n
        param authors: list authors
        :return: None
        """
        for author in authors:
            self.authors.remove(author)

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all books
        """
        return [book for book in Book.objects.all()]

    def display_author(self):
        return ''.join(authors.name for authors in self.authors.all()) + ' ' + \
               ''.join(authors.surname for authors in self.authors.all())

    display_author.short_description = 'author'

