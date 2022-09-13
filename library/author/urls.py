from django.urls import path
from . views import author_list, add_author



urlpatterns = [
    path('author/', add_author,name='add_author'),
    path('author/<int:id>/',add_author,name='author_update'),
    path('author/list/', author_list,name='author_list')

]