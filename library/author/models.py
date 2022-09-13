from django.db import models

class Author(models.Model):
    """
        This class represents an Author. \n
        Attributes:
        -----------
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes last name of the author
        type surname: str max_length=20
        param patronymic: Describes middle name of the author
        type patronymic: str max_length=20

    """
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,default=None)
    surname = models.CharField(max_length=20,default=None)
    patronymic = models.CharField(max_length=20,default=None)


    def __str__(self):
        """
        Magic method is redefined to show all information about Author.
        :return: author id, author name, author surname, author patronymic
        """
        return f"'id': {self.id}, 'name': '{self.name}', 'surname': '{self.surname}', 'patronymic': '{self.patronymic}'"


    def __repr__(self):
        """
        This magic method is redefined to show class and id of Author object.
        :return: class, id
        """

        return f'{Author.__name__}(id={self.id})'

    @staticmethod
    def get_by_id(author_id):
        """
        :param author_id: SERIAL: the id of a Author to be found in the DB
        :return: author object or None if a user with such ID does not exist
        """

        try:
            return Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return None



    @staticmethod
    def delete_by_id(author_id):
        """
        :param author_id: an id of a author to be deleted
        :type author_id: int
        :return: True if object existed in the db and was removed or False if it didn't exist
        """
        try:
            user=Author.objects.get(id=author_id)
            user.delete()
            return True
        except:
            return False


    @staticmethod
    def create(name, surname, patronymic):
        """
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes surname of the author
        type surname: str max_length=20
        param patronymic: Describes patronymic of the author
        type patronymic: str max_length=20
        :return: a new author object which is also written into the DB
        """
        if (len(name)<=20 and isinstance(name,str)) and \
           (len(surname)<=20 and isinstance(surname,str)) and \
            (len(patronymic)<=20 and isinstance(patronymic,str)):
            return Author.objects.get_or_create(name=name,surname=surname,patronymic=patronymic)[0]



    def to_dict(self):
        """
        :return: author id, author name, author surname, author patronymic
        :Example:
        | {
        |   'id': 8,
        |   'name': 'fn',
        |   'surname': 'mn',
        |   'patronymic': 'ln',
        | }
        """

        return {'id': self.id,
                'name': self.name,
                'surname': self.surname,
                'patronymic': self.patronymic}

    def update(self,
               name=None,
               surname=None,
               patronymic=None):
        """
        Updates author in the database with the specified parameters.\n
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes surname of the author
        type surname: str max_length=20
        param patronymic: Describes patronymic of the author
        type patronymic: str max_length=20
        :return: None
        """

        if name is not None and len(name)<=20 and isinstance(name,str):
            Author.objects.filter(id=self.id).update(name=name)

        if surname is not None and len(surname)<=20 and isinstance(surname,str):
            Author.objects.filter(id=self.id).update(surname=surname)

        if patronymic is not None and len(patronymic)<=20 and isinstance(patronymic,str):
            Author.objects.filter(id=self.id).update(patronymic=patronymic)

    @staticmethod
    def get_all():
        """
        returns data for json request with QuerySet of all authors
        """
        user=Author.objects.all()
        return user


