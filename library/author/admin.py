from django.contrib import admin
from author.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'patronymic', 'get_all')
    #fields = [('name', 'surname', 'patronymic'), 'all_books']

admin.site.register(Author, AuthorAdmin)
