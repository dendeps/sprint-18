from django.urls import path
from . views import book_list, add_book



urlpatterns = [
    path('book/', add_book,name='add_book'),
    path('book/<int:id>/',add_book,name='book_update'),
    path('book/list/', book_list,name='book_list')
]